import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AIService:
    @staticmethod
    def get_llm_analysis(df, total_sum):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        road_name = df.iloc[0].get('Наименование', 'объект')
        road_status = df.iloc[0].get('Значение автомобильной дороги', 'региональное')
        road_cat = df.iloc[0].get('Категория', 'V')

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system", 
                        "content": "Ты — технический писатель. Твоя задача — писать сухие, официальные аналитические резюме для дорожных отчетов. Не используй вводные фразы, не фантазируй и не давай оценок."
                    },
                    {
                        "role": "user", 
                        "content": f"Сформируй ОДНО предложение для отчета. Данные: {road_name}, статус: {road_status}, категория: {road_cat}, длина: {total_sum} км."
                    }
                ],
                temperature=0, 
                max_tokens=100
            )
            
            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"OpenAI Error: {e}")
            return f"Объект {road_name} ({road_status}) протяженностью {total_sum} км соответствует категории {road_cat}."
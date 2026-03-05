
1. Клонируйте репозиторий
   
2. Создайте и активируйте виртуальное окружение:

   ```bash
    python -m venv venv
    venv\Scripts\activate 

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Настройте переменные окружения:
    Создайте файл .env в корневой директории и добавьте:

    ```bash
        DJANGO_SECRET_KEY=ваш_ключ
        DJANGO_DEBUG=True
        OPENAI_API_KEY=ваш_ключ_openai

5. Запустите сервер:
    ```bash
    python manage.py runserver

---

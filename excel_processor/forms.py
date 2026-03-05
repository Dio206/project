from django import forms
from django.core.validators import FileExtensionValidator

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        label="Выберите Excel файл",
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])]
    )
from django import forms
from .models import User_report
from django.forms import ModelForm, Textarea, TextInput, FileInput


class User_reportForm(ModelForm):
    class Meta:
        model = User_report
        fields = ['status','priority', 'seriousness', 'title', 'description', 'playback_steps', 'actual_result', 'expected_result', 'context', 'attachments', 'file', 'more_information',]

        widgets = {
            'title': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Заголовок'}),
            'description': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Описание'}),
            'playback_steps': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Шаги воспроизведения'}),
            'actual_result': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Фактический результат'}),
            'expected_result': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Ожидаемый результат'}),
            'context': TextInput(attrs={'class': 'text_boxes_input', 'placeholder': 'Окружение'}),
            'attachments': FileInput(attrs={'class': 'form-control'}),
            'file': FileInput(attrs={'class': 'form-control'}),
            'more_information': Textarea(attrs={'class': 'text_boxes', 'placeholder': 'Дополнительная информация'}),

        }
        labels = {
            'title': '',
            'description': '',
            'playback_steps': '',
            'actual_result': '',
            'expected_result': '',
            'context': '',
            'attachments': 'Прикрепить скриншот',
            'file': 'Прикрепить лог файл',
            'more_information': '',

        }


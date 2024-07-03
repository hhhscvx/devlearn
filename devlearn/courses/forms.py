from django import forms
from .models import LessonComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = LessonComment
        fields = ['comment']
        labels = {'comment': 'Комментарий'}
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Введите комментарий'})
        }

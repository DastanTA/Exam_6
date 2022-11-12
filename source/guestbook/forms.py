from django import forms
from django.forms import widgets


STATUS_CHOICES = [('active', 'активно'), ('blocked', 'заблокировано')]


class NoteForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор')
    email = forms.EmailField(required=True, label='Почта')
    note = forms.CharField(max_length=3000, required=True, label='Запись', widget=widgets.Textarea(attrs={"cols":24, "rows":5}))

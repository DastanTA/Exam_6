from django.db import models


STATUS_CHOICES = [('active', 'активно'), ('blocked', 'заблокировано')]


class NoteModel(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, verbose_name='имя автора')
    email = models.EmailField(null=False, blank=False, verbose_name='почта автора')
    note = models.TextField(max_length=3000, null=False, blank=False, verbose_name='запись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время редактирования')
    status = models.CharField(max_length=30, null=False, blank=False, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='статус')

    def __str__(self):
        return f'{self.pk}. {self.author}'

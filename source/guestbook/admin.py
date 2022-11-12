from django.contrib import admin
from guestbook.models import NoteModel


class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['author']
    readonly_fields = ['created_at', 'updated_at']
    exclude = []


admin.site.register(NoteModel, NotesAdmin)

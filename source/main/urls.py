from django.contrib import admin
from django.urls import path
from guestbook.views import main_page, note_create_view, note_update_view, delete_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('add/', note_create_view, name='create_note'),
    path('<int:pk>/update', note_update_view, name='update_note'),
    path('<int:pk>/delete', delete_note, name='delete_note'),
]

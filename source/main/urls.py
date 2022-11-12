from django.contrib import admin
from django.urls import path
from guestbook.views import main_page, note_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('add/', note_create_view, name='create_note'),
]

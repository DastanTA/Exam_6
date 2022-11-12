from django.shortcuts import render, get_object_or_404
from guestbook.models import NoteModel, STATUS_CHOICES


def main_page(request):
    notes = NoteModel.objects.all().order_by('-created_at').filter(status='active')
    context = {'notes': notes}
    return render(request, 'index.html', context)

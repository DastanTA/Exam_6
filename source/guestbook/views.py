from django.shortcuts import render, get_object_or_404, redirect
from guestbook.models import NoteModel, STATUS_CHOICES
from guestbook.forms import NoteForm


def main_page(request):
    notes = NoteModel.objects.all().order_by('-created_at').filter(status='active')
    context = {'notes': notes}
    return render(request, 'index.html', context)


def note_create_view(request, *args, **kwargs):
    if request.method == "GET":
        form = NoteForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == "POST":
        form = NoteForm(data=request.POST)
        if form.is_valid():
            NoteModel.objects.create(
                author=form.cleaned_data.get('author'),
                email=form.cleaned_data.get('email'),
                note=form.cleaned_data.get('note')
            )
            return redirect('main')
        else:
            return render(request, 'create.html', context={'form': form})


def note_update_view(request, pk, *args, **kwargs):
    note = get_object_or_404(NoteModel, pk=pk)
    if request.method == "GET":
        form = NoteForm(initial={
            'author': note.author,
            'email': note.email,
            'note': note.note
        })
        return render(request, 'update.html', context={'form': form, 'note': note})
    elif request.method == "POST":
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.author = form.cleaned_data.get('author')
            note.email = form.cleaned_data.get('email')
            note.note = form.cleaned_data.get('note')
            note.save()
            return redirect('main')
        else:
            return render(request, 'update.html', context={'form': form, 'note': note})
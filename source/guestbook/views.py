from django.shortcuts import render, get_object_or_404, redirect
from guestbook.models import NoteModel
from guestbook.forms import NoteForm, SearchForm


def main_page(request):
    if request.method == "POST":
        form_search = SearchForm(data=request.POST)
        form = NoteForm()
        if form_search.is_valid():
            notes = NoteModel.objects.all().order_by('-created_at').filter(status='active', author=form_search.cleaned_data.get('author'))
            context = {'notes': notes, 'form_search': form_search, 'form': form}
            return render(request, 'index.html', context)
    form_search = SearchForm()
    form = NoteForm()
    notes = NoteModel.objects.all().order_by('-created_at').filter(status='active')
    context = {'notes': notes, 'form_search': form_search, 'form': form}
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


def delete_note(request, pk, *args, **kwargs):
    note = get_object_or_404(NoteModel, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'note': note})
    elif request.method == 'POST':
        note.delete()
        return redirect('main')

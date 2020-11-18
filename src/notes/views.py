from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Note


@login_required
def HomeView(request):
    note_list = Note.objects.filter(user=request.user)
    context = {'notes': note_list}

    return render(request, 'notes/home.html', context)


def RegisterView(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        user_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=user_password)
        login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'notes/register.html', {'form': form})


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'notes/note_create.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'notes/note_detail.html'


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'notes/note_update.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'

    def get_success_url(self):
        return reverse('home')

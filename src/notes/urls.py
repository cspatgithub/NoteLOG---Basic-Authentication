from django.urls import path
from .views import HomeView, NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView, RegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView, name='home'),
    path('register', RegisterView, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='notes/logout.html'), name='logout'),
    path('note/create', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]

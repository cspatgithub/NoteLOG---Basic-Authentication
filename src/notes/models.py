from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import  User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

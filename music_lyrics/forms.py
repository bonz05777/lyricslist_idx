# music_lyrics/forms.py

from django import forms
from .models import Lyrics

class LyricsForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        fields = ['title', 'artist', 'lyrics']
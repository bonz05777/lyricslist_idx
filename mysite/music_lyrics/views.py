# music_lyrics/views.py
from django.shortcuts import render, get_object_or_404
from .models import Lyrics
from .forms import LyricsForm
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import LyricsSerializer
from django.utils import timezone


class LyricsViewSet(viewsets.ModelViewSet):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer


def lyrics_list(request):
    lyrics = Lyrics.objects.all()
    artists_with_songs = []

    # Hottest Songs: Top 5 based on visit count
    hottest_songs = Lyrics.objects.order_by('-visit_count')[:5]
    
    # Latest Songs: Top 5 most recently added
    latest_songs = Lyrics.objects.order_by('-date_added')[:5]

    # Group songs by artist
    artists = Lyrics.objects.values_list('artist', flat=True).distinct()
    for artist in artists:
        songs = Lyrics.objects.filter(artist=artist)
        artists_with_songs.append({
            'artist': artist,
            'songs': songs
        })

    return render(request, 'music_lyrics/lyrics_list.html', {
        'lyrics': lyrics,
        'artists_with_songs': artists_with_songs,
        'hottest_songs': hottest_songs,
        'latest_songs': latest_songs
    })

def lyrics_detail(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)

     # Increment the visit count each time the detail page is accessed
    lyric.visit_count += 1
    lyric.save()
    return render(request, 'music_lyrics/lyrics_detail.html', {'lyric': lyric})

def lyrics_create(request):
    form = LyricsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/lyrics/')  # Redirect to the lyrics list
    return render(request, 'music_lyrics/lyrics_form.html', {'form': form})

def lyrics_update(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)
    form = LyricsForm(request.POST or None, instance=lyric)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/lyrics/')  # Redirect to the lyrics list
    return render(request, 'music_lyrics/lyrics_form.html', {'form': form})

def lyrics_delete(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)
    lyric.delete()
    return HttpResponseRedirect('/lyrics/')  # Redirect back to the lyrics list

def about(request):
    return render(request, 'music_lyrics/about.html') 

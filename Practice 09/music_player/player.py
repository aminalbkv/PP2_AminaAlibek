
import pygame
from pathlib import Path
import time
import wave

pygame.mixer.init()

MUSIC_FOLDER = Path(__file__).parent / "music"

playlist = [
    MUSIC_FOLDER / "track1.mp3",
    MUSIC_FOLDER / "track2.mp3"
]

current_track = 0
start_time = 0
playing = False
duration = 0


def get_duration(path):
    # Read the track duration
    try:
        from mutagen import File
        audio = File(str(path))
        if audio is not None and audio.info:
            return audio.info.length
    except Exception:
        pass
    return 0


def play_music():
    global start_time, playing, duration

    path = playlist[current_track]
    pygame.mixer.music.load(str(path))
    pygame.mixer.music.play()

    duration = get_duration(path)
    start_time = time.monotonic()
    playing = True


def stop_music():
    global playing, start_time
    pygame.mixer.music.stop()
    playing = False
    start_time = 0


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()


def get_track_name():
    return playlist[current_track].stem


def get_progress():
    if not playing:
        return 0

    if not pygame.mixer.music.get_busy():
        return duration

    return min(time.monotonic() - start_time, duration)


def get_duration_seconds():
    return duration

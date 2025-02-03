"""Module for processing mp3 files"""

#import os
from pathlib import Path
from pydub import AudioSegment
from mutagen import MutagenError
from mutagen.mp3 import EasyMP3


def get_mp3_files(directory) -> list:
    """Processes all .mp3 files in the specified directory."""
    mp3_files = list(Path(directory).glob("*.mp3"))
    file_names = [str(file) for file in mp3_files]  # Collecting file names
    return file_names


def combine_mp3_files(input_files: list, output_file: str):
    """Combines mp3 files in folder into a single MP3 file."""
    print('Combing MP3 files...')
    combined_audio = AudioSegment.empty()
    for file in input_files:
        audio = AudioSegment.from_mp3(file)
        combined_audio += audio
    combined_audio.export(output_file, format="mp3")
    return

def write_intro_mp3_tags(file_path, tags):
    """Writes MP3 metadata tags to the intro MP3 using EasyMP3."""
    try:
        audio = EasyMP3(file_path)
        #for tag, value in tags.items():
        #    audio[tag] = value
        audio['tracknumber'] = '0'
        audio['title'] = 'DJ Pyle Intro'
        audio['artist'] = tags['artist']
        audio['album'] = tags['album']
        audio['genre'] = tags['genre']
        audio['date'] = tags['date']
        audio.save()
        print(f"Tags updated successfully for {file_path}")
    except Exception as e:
        print(f"Error writing tags: {e}")


def write_mp3_tags(file_path, tags):
    """Writes MP3 metadata tags using EasyMP3."""
    try:
        audio = EasyMP3(file_path)
        for tag, value in tags.items():
            audio[tag] = value
        audio.save()
        print(f"Tags updated successfully for {file_path}")
    except Exception as e:
        print(f"Error writing tags: {e}")


def read_mp3_tags(file_path):
    """Reads MP3 metadata tags using EasyMP3."""
    try:
        print(f'Reading tags for file {file_path}')
        audio = EasyMP3(file_path)
        return dict(audio)  # Convert tags to dictionary
    except (OSError, IOError) as file_error:
        print(f"File access error: {file_error}")
    except MutagenError as tag_error:
        print(f"Error reading MP3 tags: {tag_error}")
        return {}

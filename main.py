import os
import argparse
from djpyle import genai_utils, mp3_utils


def validate_directory(directory):
    """Validates the MP3 directory."""
    if not os.path.isdir(directory):
        raise ValueError(f"Error: Provided directory '{directory}' does not exist.")
    return directory


def text_generation(directory):
    """Generate introduction text using MP3 tags."""
    mp3_files = mp3_utils.get_mp3_files(directory)
    if not mp3_files:
        raise ValueError("No MP3 files found in the provided directory.")

    tags = mp3_utils.read_mp3_tags(mp3_files[0])
    output = genai_utils.generate_intro_text(
        genre=tags['genre'][0],
        album=tags['album'][0],
        artist=tags['artist'][0],
        year=tags['date'][0]
    )
    return output, tags


def text_to_speech(directory, text, tags):
    """Convert text to speech and save as MP3 with tags."""
    intro_mp3_file = os.path.join(directory, "00 DJ Pyle Intro.mp3")
    genai_utils.generate_text_to_speech(text=text, mp3_file=intro_mp3_file)
    mp3_utils.write_intro_mp3_tags(file_path=intro_mp3_file, tags=tags)
    return intro_mp3_file


def combine_mp3s(directory, tags):
    """Combine the intro and individual MP3s into a full album."""
    mp3_files = mp3_utils.get_mp3_files(directory)
    #mp3_files.insert(0, intro_mp3_file)  # Insert intro as the first track

    output_file = os.path.join(directory, f"{tags['artist'][0]}-{tags['album'][0]}.mp3")
    mp3_utils.combine_mp3_files(mp3_files, output_file)
    print(f"Combined album saved as: {output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(
        prog="DJ Pyle",
        description="Generates an intro MP3 with album details for the Pyle PBMSPG1BK MP3 player.",
        epilog="Rock on with DJ Pyle! 🤘"
    )
    parser.add_argument("directory", type=validate_directory, help="Path to the directory containing MP3 files")
    parser.add_argument("--tgen", action="store_true", help="Run Text Generation only")
    parser.add_argument("--tts", action="store_true", help="Run Text Generation and Text-to-Speech only")

    args = parser.parse_args()

    # Control flow based on arguments
    if args.tgen:
        output, tags = text_generation(args.directory)
        print(f"Generated Intro Text: {output}")

    elif args.tts:
        output, tags = text_generation(args.directory)
        intro_mp3 = text_to_speech(args.directory, output, tags)
        print(f"Intro MP3 created: {intro_mp3}")

    else:
        output, tags = text_generation(args.directory)
        intro_mp3 = text_to_speech(args.directory, output, tags)
        combine_mp3s(args.directory, tags)


if __name__ == "__main__":
    main()

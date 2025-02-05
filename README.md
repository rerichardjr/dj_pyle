# DJ Pyle

<div align="center">
  <img src="assets/images/dj_pyle_logo.png" alt="DJ Pyle Logo">
</div>

DJ Pyle is a Python application designed to combine individual MP3 tracks into a single full album MP3. This is specifically tailored for use with the [Pyle PBMSPG1BK](https://pyleusa.com/products/pbmspg1bk) MP3 player, which lacks a navigation menu and relies solely on forward and back buttons. By merging tracks into one continuous album file, the app reduces the need for excessive button presses. Additionally, DJ Pyle generates an introduction MP3, providing album details to the listener before the music starts.

## Summary

DJ Pyle reads metadata tags from individual MP3 files (artist, album, year) and creates an introduction prompt using a Radio DJ persona. This prompt is processed using LangChain to interact with Huggingface's API, generating an introduction to be used as a bumper track for artist and album indentification. The output is then converted to speech using ElevenLabs and saved as an MP3 file. Finally, the introduction and individual tracks are merged into a single MP3 for seamless playback.

### Storage Efficiency

| **Type of MP3**        | **Average File Size** | **Approximate Number on 16GB SD Card** |
|------------------------|-----------------------|-----------------------------------------|
| Individual MP3 (5 MB)  | 5 MB                  | ~3,200 files                            |
| Full Album MP3 (100 MB)| 100 MB                | ~160 albums                             |

*Note: These estimates vary based on bitrates and track lengths.*

## Example output

🤖 LLM response

Hey headbangers. I'm DJ Pyle on Pure Metal 1 O 1 .9 FM. Next track takes us back to the heart of thrash metal: it's the legendary 1986 release - Metallica's iconic masterpiece, Master of Puppets! Crank it up!

🎧 [Listen to an Example Introduction MP3](https://soundcloud.com/drahcirer/dj-pyle-intro?si=dcf41b01e17b49f29da22083427529ea&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing)

## Features
- Basic pronunciation adjustment of words in LLM responses using exact or fuzzy matching.
- Emoji removal in LLM response.

*Note: The LLM prompt explicity states no emojis in response.*

## Setting Up the Environment

### 1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

### 2. **Activate the Virtual Environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

### 3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```


## API Keys Configuration

You will need API keys for both HuggingFace and ElevenLabs:

1. Sign up and obtain your API keys from [HuggingFace](https://huggingface.co) and [ElevenLabs](https://elevenlabs.io).
2. Create a `.env` file in the project root:

```env
HUGGINGFACE_API_KEY=your_huggingface_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## Installing ffmpeg and ffprobe

DJ Pyle relies on `pydub`, which requires `ffmpeg` and `ffprobe`.

### Windows:
- Download from [FFmpeg website](https://ffmpeg.org/download.html).
- Add the `bin` folder to your system's PATH.

### macOS (using Homebrew):
```bash
brew install ffmpeg
```

### Linux (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install ffmpeg
```

## Running the Application

Use the CLI to process your MP3 files:

```bash
python main.py /path/to/your/mp3/directory
```

## CLI Arguments

The DJ Pyle application supports the following command-line arguments:

### Required Argument:
- `directory` (str):  
  The path to the directory containing MP3 files. This argument is required to specify the location of the music files for processing.

### Optional Arguments:
- `--tgen`  
  Run only the **Text Generation** process. This option generates text based on the metadata of the MP3 files without generating the corresponding speech or merging the tracks.

- `--tts`  
  Run both **Text Generation** and **Text-to-Speech** processes. This option generates the descriptive text and converts it to speech, providing an audio intro to be merged with the MP3 files.

### Example Usage:
```bash
python main.py /path/to/mp3/directory
python main.py /path/to/mp3/directory --tgen
python main.py /path/to/mp3/directory --tts
```
---

## Future Enhancements  

- Add more CLI arguments for customization.  
- Improve pronunciation correction for artist and album names.  
- Support batch processing for multiple albums.
- Improve error handling.
- Album lookup using Musicbrainz when MP3s are not tagged. 

---

Enjoy seamless album playback with DJ Pyle! 🤘


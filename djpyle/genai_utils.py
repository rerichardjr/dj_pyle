"""Module for GenAI functions"""

import os
from dotenv import load_dotenv

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

from djpyle import utils
from djpyle.llm_config import LLM_PARAMS
from djpyle.tts_config import TTS_PARAMS

load_dotenv()

HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACEHUB_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

llm = HuggingFaceEndpoint(
    **LLM_PARAMS
)

tts = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

pronunciations = utils.load_pronunciations()


@utils.modify_output(utils.remove_emojis)
@utils.modify_output(utils.modify_pronunciations)
def generate_intro_text(genre:str, artist:str, album:str, year:str, llm_instance=llm):
    """Generate the DJ introduction text for use in a text-to-speech process."""

    prompt = PromptTemplate(
        input_variables=["genre", "artist", "album"],
        template=read_llm_prompt_file()
    )

    response = llm_instance.invoke(prompt.format(
        genre=genre,
        artist=artist,
        album=album,
        year=year
        )
    )

    return response


def generate_text_to_speech(text: str, mp3_file: str, client_instance=tts) -> str:
    """Converts text to audio."""

    voice_settings = VoiceSettings(**TTS_PARAMS['voice_settings'])

    print(f'Passing LLM output to Elevenlabs: {text}')

    response = client_instance.text_to_speech.convert(
        voice_id=TTS_PARAMS['voice_id'],
        optimize_streaming_latency=TTS_PARAMS['optimize_streaming_latency'],
        output_format=TTS_PARAMS['output_format'],
        text=text,
        model_id=TTS_PARAMS['model_id'],
        voice_settings=voice_settings,
    )

    with open(mp3_file, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {mp3_file}")

    return mp3_file


def read_llm_prompt_file() -> str:
    """Reads the text from the prompt file."""
    llm_prompt_file_path = os.path.join("extras", "dj_pyle.txt")
    with open(llm_prompt_file_path, "r", encoding="utf-8") as file:
        llm_prompt_file_text = file.read()
    return llm_prompt_file_text

''' Configuration parameters for text-to-speech in Eleven Labs '''

TTS_PARAMS = {
    "voice_id": "6xPz2opT0y5qtoRh1U1Y",
    #"voice_id": "nPczCjzI2devNBz1zQrb",
    "optimize_streaming_latency": "0",
    "output_format": "mp3_22050_32",
    "model_id": "eleven_turbo_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0.0,
        "use_speaker_boost": True,
    }
}

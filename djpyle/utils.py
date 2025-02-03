''' Utility functions '''

import os
import re
import json
import functools
from rapidfuzz import process

def remove_emojis(text):
    """Removed Emojis from LLM output if any exists."""
    emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def load_pronunciations(file_name="pronunciations.json"):
    """Load pronunciation fixes from the JSON file."""
    extras_folder_path = os.path.join(os.getcwd(), 'extras')
    file_path = os.path.join(extras_folder_path, file_name)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Pronunciations file not found at {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def fix_pronunciations(word, pronunciation_dict):
    """Replaces text in output using direct or fuzzy matching."""
    if word in pronunciation_dict:
        print(f'Found {word} and replacing with {pronunciation_dict[word]}.')
        return pronunciation_dict[word]

    # Fuzzy match: Find closest word in dictionary
    best_match, score, _ = process.extractOne(word, list(pronunciation_dict.keys()))
    if score >= 85:  # Using a threshold of 85%
        print(f'The best match for {word} is {best_match}.')
        return pronunciation_dict[best_match]  # Replace with correct word
    return word  # Keep original if no good match


def modify_pronunciations(text):
    """Modifies the LLM output."""
    pronunciations = load_pronunciations()  # Load the pronunciation dictionary
    words = text.split()  # Split the text into words

    #print(words)

    fixed_words = [fix_pronunciations(word, pronunciations) for word in words]  # Fix each word
    return " ".join(fixed_words)  # Join the fixed words into a sentence


def modify_output(decorator_func):
    """Generic decorator to modify the output of a function."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return decorator_func(result)
        return wrapper
    return decorator

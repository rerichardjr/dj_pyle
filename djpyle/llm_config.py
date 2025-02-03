''' Configuration parameters for LLM '''

LLM_PARAMS = {
    "repo_id": "mistralai/Mistral-7B-Instruct-v0.3",
    "task": "text-generation",
    "max_new_tokens": 100,
    "do_sample": False,
    "temperature": 1.2,
    "repetition_penalty": 1.3,
    "top_p": 0.9,
    "top_k": 50,
}
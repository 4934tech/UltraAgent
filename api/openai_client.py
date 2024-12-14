from openai import OpenAI

def create_openai_client(api_key):
    return OpenAI(api_key=api_key)

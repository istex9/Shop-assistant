import requests
from config import OLLAMA_API_URL, MODEL_NAME
import json

def get_llm_response(prompt, model=MODEL_NAME, temperature=0.0, max_tokens=500):
    """
    Lekéri az LLM válaszát a megadott prompt alapján.

    Args:
        prompt (str): Az LLM-nek küldendő prompt.
        model (str): Az Ollama által használt modell neve.
        temperature (float): A generálás hőmérséklete (0.0 - 1.0).
        max_tokens (int): A generált válasz maximális token száma.

    Returns:
        str: Az LLM válasza.
    """
    url = f"{OLLAMA_API_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, json=payload, stream=True)

    result = ''
    for line in response.iter_lines():
        if line:
            data = line.decode('utf-8')
            # JSON objektum feldolgozása
            try:
                json_data = json.loads(data)
                # A 'response' mező értékének hozzáadása
                result += json_data.get('response', '')
            except json.JSONDecodeError:
                # Ha a sor nem érvényes JSON, lépünk tovább
                continue
    return result.strip()

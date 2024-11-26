import re

from llm_interface import get_llm_response
from prompt_engineering import generate_prompt
from qa import get_relevant_documents


def handle_user_input(user_input):

    
    # Releváns dokumentumok lekérése
    docs = get_relevant_documents(user_input)
    context = "\n\n".join([doc.page_content for doc in docs])

    # Prompt generálása
    prompt = generate_prompt(user_input, context)

    # Válasz lekérése az LLM-től
    llm_response = get_llm_response(prompt)

    # Válasz utófeldolgozása

    # Ellenőrizzük, hogy a válasz megfelelő-e
    if not is_valid_response(llm_response):
        # Ha nem, kérjük az átfogalmazást
        return {
            "response": "Sajnálom, nem értem pontosan a kérdésedet. Kérlek, fogalmazd meg részletesebben, hogy jobban segíthessek!"
        }

    return {
        "response": llm_response
    }



def is_valid_response(response):
    # Definiáljuk, hogy mi számít érvényes válasznak
    # Például, ha a válasz nem üres és tartalmaz betűket
    return bool(response) and any(c.isalpha() for c in response)

# A33 - Chatbot fejlesztése LLM segítségével ügyféltámogatásra


Ez a projekt egy Flask alapú chatbot alkalmazás, amely integrálva van az Ollama-val, és böngészőn keresztül érhető el. A chatbot a Retrieval-Augmented Generation (RAG) technikát használja, amely lehetővé teszi, hogy a felhasználói kérdésekre releváns és pontos válaszokat adjon az előre indexelt dokumentumok alapján. A RAG megközelítés során a chatbot először releváns dokumentumokat keres a vállalati tudásbázisban, majd ezeket az információkat felhasználva generál választ a nyelvi modell (LLM) segítségével. Ez biztosítja, hogy a válaszok pontosak és a rendelkezésre álló dokumentumok tartalmára épüljenek.

## Előfeltételek

A projekt futtatásához szükséges:

- Telepített [Docker](https://www.docker.com/get-started) a rendszeren.

 **VAGY**
- Telepített [Ollama](https://ollama.com) a rendszeren.

## Build és Futatás

### Docker Image Buildelés

A Docker image buildeléshez használd a következő parancsot:

```bash
docker build -t chatbot-app .
```

### Docker Konténer Futtatása

Indítsd el a Docker konténert a következő parancsokkal:

```bash
docker run -p 5000:5000 -p 11434:11434 chatbot-app
```

### Az Alkalmazás Elérése

Nyisd meg a böngésződet, és navigálj a [http://localhost:5000/](http://localhost:5000/) címre a chatbot használatához.

## Projekt Fontosabb Fájlok Felépítése

- **`app.py`**: A fő Flask alkalmazás.
- **`handler.py`**: Kezeli a bemenetet.
- **`prompt_engineering.py`**: Promptokat készít a chatbot számára.
- **`llm_interface.py`**: Kommunikál az Ollama LLM-mel.
- **`index_documents.py`**: Dokumentumokat indexel a RAG (retrieval-augmented generation) működéséhez.
- **`config.py`**: Konfigurációs változókat tartalmaz.
- **`templates/`**: HTML sablonok a Flask alkalmazáshoz.
- **`static/`**: Statikus fájlok (CSS, JavaScript).
- **`requirements.txt`**: Python függőségek listája.
- **`Dockerfile`**: A Docker image felépítéséhez szükséges fájl.
- **`data/`**: Dokumentumokat tartalmazó mappa:
  - `contact_info.txt`
  - `faq_billing.txt`
  - `faq_general.txt`
  - `privacy_policy.txt`

### 1. `app.py`

**Funkció:**  
Ez a fő Flask alkalmazás, amely kezeli a webes interfészt és a bejövő kéréseket.

**Kulcsfontosságú Részek:**
- **Flask Beállítása:** Inicializálja a Flask alkalmazást és definiálja a route-okat.
- **Route-ok:**
  - `/`: Kezdeti oldal megjelenítése (`index.html`).
  - `/chat`: POST kérés fogadása a chatbot interakciókhoz.

### 2. `handler.py`

**Funkció:**  
Ez a fájl kezeli a felhasználói bemenetet, integrálja a dokumentumok lekérdezését és a válasz generálását a LLM (Ollama) segítségével.

**Kulcsfontosságú Függvények:**
- **`handle_user_input(user_input)`**  
  Kezeli a felhasználói üzenetet, lekéri a releváns dokumentumokat, generálja a promptot és megszerzi a válaszokat.
  
- **`is_valid_response(response)`**  
  Ellenőrzi, hogy a válasz érvényes-e és nem tartalmaz tiltott kifejezéseket.

### 3. `prompt_engineering.py`

**Funkció:**  
Ez a fájl felelős a promptok generálásáért, amelyeket a LLM-nek (Ollama) küldünk a válaszok előállításához.

**Kulcsfontosságú Függvény:**
- **`generate_prompt(user_input, context)`**  
  Létrehozza a promptot a felhasználói bemenet és a releváns dokumentumok alapján, beleértve a példákat a kívánt válaszformátumra.

### 4. `llm_interface.py`

**Funkció:**  
Ez a fájl kezeli az interfészt az LLM-hez (Ollama), és lekéri a válaszokat a generált promptok alapján.

**Kulcsfontosságú Függvény:**
- **`get_llm_response(prompt, model, temperature, max_tokens)`**  
  Küldi a promptot az LLM-nek és visszaadja a választ.

### 5. `config.py`

**Funkció:**  
Ez a fájl tartalmazza a projekt konfigurációs változóit, például az embedding modell nevét és egyéb beállításokat.

### 6. `index_documents.py`

**Funkció:**  
Felelős a dokumentumok betöltéséért és indexeléséért az `document_loader.py` segítségével. Ez a szkript biztosítja, hogy a dokumentumok előzetesen indexelve legyenek a RAG rendszer működéséhez.

## Függőségek

Minden Python függőség a `requirements.txt` fájlban található.

## Megjegyzések

- Győződj meg arról, hogy a `5000` és `11434` portok szabadok a rendszeren.
- Ha módosítani szeretnéd a portokat, frissítsd az `EXPOSE` direktívákat a Dockerfile-ban és a `-p` paramétereket a konténer futtatásakor.
- Az első inditásnál lassabb lehet mivel le kell tölteni-e a modell-t. Valamint az első kérdés szintén hosszabb ideig tart, mert be kell töltenie a modell-t.

## Docker Nélküli Futtatás

Ha nem szeretnél Docker-t használni, kövesd az alábbi lépéseket:

1. Telepítsd a függőségeket:
    ```bash
    pip install -r requirements.txt
    ```
2. Indexeld a dokumentumokat az `index_documents.py` segítségével:
    ```bash
    python index_documents.py
    ```
3. Töltsd le az Ollama-t, majd egy terminálban futtasd az alábbi parancsot az Ollama szerver elindításához:
    ```bash
    ollama pull llama3.1:8b
    ollama serve
    ```
4. Egy másik terminálban futtasd az `app.py`-t:
    ```bash
    python app.py
    ```
5. Nyisd meg a böngésződet, és navigálj a [http://localhost:5000/](http://localhost:5000/) címre a chatbot használatához.

## Teszt képek
 - A céges adatok 4 tipusba sorolhatóak, általában jól válaszól az asziszens, mindegyik kategoriában vagy azt mondja hogy nem tudja, kérdezd másképp.. Viszont ahogy a második képen is lehet látni néha hibázik, a nyugdijasoknak nincs kedvezmény.. A dokumentumok szerint, csak a diákoknak van.
 - Érdekesség, hogy elég nagy javulást lehet elérni ha a prompt_engineering-ben előre megadott krédés válasz példákat sorolunk fel, ugyanakkor a váratlan kérdésekre akkor nagyobb hibát szokott adni, ezért ki is vettem ezt a részt a megoldásomból.
 - Sokkal hatékonyabb volna ha az egész projekt angolul lenne, viszont kivánics voltam, hogy teljesít ha magyar.

### Tesztkép 1
![Tesztkép 1](teszt1.png)

### Tesztkép 2
![Tesztkép 2](teszt2.png)
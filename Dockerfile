FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -O https://ollama.ai/install.sh && \
    bash install.sh && \
    rm install.sh

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

EXPOSE 11434

RUN python index_documents.py

CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull llama3.1:8b && python app.py"]

from flask import Flask, request, jsonify, render_template
from handler import handle_user_input

app = Flask(__name__)

@app.route('/')
def index():
    """
    Kezeli a főoldal kérését, és rendereli az index.html fájlt.
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Kezeli a /chat végpontra érkező POST kéréseket, és visszaadja a chatbot válaszát.
    
    Returns:
        Response: A JSON válasz, amely tartalmazza az LLM válaszát.
    """
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Nincs megadva üzenet.'}), 400
    
    try:
        response = handle_user_input(user_input)
        return jsonify(response)
    except Exception as e:
        # Logolja a hibát (opcionális)
        app.logger.error(f"Hiba a kérés feldolgozása során: {e}")
        return jsonify({'error': 'Hiba történt a kérés feldolgozása során.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

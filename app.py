from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman
#from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Talisman for security headers
Talisman(
    app,
    content_security_policy={
        'default-src': "'self'",
        'script-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net'],
        'style-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net'],
        'img-src': ["'self'", 'data:'],
    },
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    session_cookie_http_only=True
)

# Store keys in memory (for demo purposes)
keys = {
    'public': None,
    'private': None
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    try:
        public_key, private_key = generate_keypair()
        keys['public'] = public_key
        keys['private'] = private_key
        return jsonify({
            'public_key': base64.b64encode(public_key).decode('utf-8'),
            'private_key': base64.b64encode(private_key).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        if not keys['public']:
            return jsonify({'error': 'Public key not generated'}), 400
        
        message = data['message'].encode('utf-8')
        ciphertext, shared_secret = encrypt(keys['public'], message)
        
        return jsonify({
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
            'shared_secret': base64.b64encode(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    try:
        data = request.get_json()
        if not data or 'ciphertext' not in data:
            return jsonify({'error': 'Ciphertext is required'}), 400
        
        if not keys['private']:
            return jsonify({'error': 'Private key not generated'}), 400
        
        ciphertext = base64.b64decode(data['ciphertext'])
        shared_secret = decrypt(keys['private'], ciphertext)
        
        return jsonify({
            'shared_secret': base64.b64encode(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 
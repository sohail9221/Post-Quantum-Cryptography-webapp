# Import necessary libraries
from flask import Flask, render_template, request, jsonify           # Flask components for web server, templates, API
from flask_talisman import Talisman                                  # Flask extension for setting security headers
# from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt  # Uncomment when using actual Kyber512 implementation
import base64                                                         # For encoding/decoding keys and messages
from dotenv import load_dotenv                                       # To load environment variables from a .env file

# Load environment variables from .env
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Configure Talisman for HTTP security headers
Talisman(
    app,
    content_security_policy={
        'default-src': "'self'",                                      # Restrict resources to same origin
        'script-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net'],  # Allow scripts from CDN and inline (limited)
        'style-src': ["'self'", "'unsafe-inline'", 'cdn.jsdelivr.net'],   # Allow styles from CDN and inline
        'img-src': ["'self'", 'data:'],                               # Allow inline images
    },
    force_https=True,                                                 # Enforce HTTPS
    strict_transport_security=True,                                   # Set HSTS header
    session_cookie_secure=True,                                       # Ensure cookies are sent over HTTPS only
    session_cookie_http_only=True                                     # Prevent JavaScript from accessing session cookies
)

# In-memory storage for keys (for demonstration only; not secure for production)
keys = {
    'public': None,
    'private': None
}

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')  # Renders the homepage

# Route for the demo page
@app.route('/demo')
def demo():
    return render_template('demo.html')  # Renders the cryptography demo interface

# API endpoint for generating key pairs
@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    try:
        public_key, private_key = generate_keypair()  # Generate post-quantum key pair
        keys['public'] = public_key                   # Store public key
        keys['private'] = private_key                 # Store private key

        # Return base64-encoded keys to the frontend
        return jsonify({
            'public_key': base64.b64encode(public_key).decode('utf-8'),
            'private_key': base64.b64encode(private_key).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500        # Handle errors gracefully

# API endpoint for encryption
@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    try:
        data = request.get_json()                     # Get JSON payload from request
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400

        if not keys['public']:
            return jsonify({'error': 'Public key not generated'}), 400

        message = data['message'].encode('utf-8')     # Convert message to bytes
        ciphertext, shared_secret = encrypt(keys['public'], message)  # Encrypt message

        # Return base64-encoded ciphertext and shared secret
        return jsonify({
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
            'shared_secret': base64.b64encode(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint for decryption
@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    try:
        data = request.get_json()
        if not data or 'ciphertext' not in data:
            return jsonify({'error': 'Ciphertext is required'}), 400

        if not keys['private']:
            return jsonify({'error': 'Private key not generated'}), 400

        ciphertext = base64.b64decode(data['ciphertext'])            # Decode base64-encoded ciphertext
        shared_secret = decrypt(keys['private'], ciphertext)         # Decrypt to get shared secret

        return jsonify({
            'shared_secret': base64.b64encode(shared_secret).decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app in debug mode (development only)
if __name__ == '__main__':
    app.run(debug=True)

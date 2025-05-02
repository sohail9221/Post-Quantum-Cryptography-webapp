# Post-Quantum Cryptography Web Application

A secure web application that demonstrates Post-Quantum Cryptography using the Kyber512 algorithm. The application provides a user-friendly interface for generating key pairs, encrypting messages, and decrypting ciphertext.

## Features

- Modern, responsive UI with smooth animations
- Secure key generation using Kyber512
- Message encryption and decryption
- Copy-to-clipboard functionality
- User-friendly error handling
- Secure HTTP headers and best practices

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Generate Keys**
   - Click the "Generate New Keys" button
   - The public and private keys will be displayed in their respective text areas

2. **Encrypt a Message**
   - Enter your message in the "Message to Encrypt" field
   - Click the "Encrypt Message" button
   - The encrypted message will appear in the "Encrypted Message" field

3. **Decrypt a Message**
   - Enter the encrypted message in the "Encrypted Message" field
   - Click the "Decrypt Message" button
   - The decrypted message will appear in the "Decrypted Message" field

## Security Features

- Flask-Talisman for secure HTTP headers
- Content Security Policy (CSP) implementation
- HTTPS enforcement
- Secure session cookie settings
- Input sanitization
- Error handling without exposing stack traces

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Custom styles and animations
│   └── js/
│       └── main.js    # Frontend JavaScript
├── templates/
│   └── index.html     # Main HTML template
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework
- Bootstrap for UI components
- pqcrypto for Post-Quantum Cryptography implementation 
document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const generateBtn = document.getElementById('generateBtn');
    const encryptBtn = document.getElementById('encryptBtn');
    const decryptBtn = document.getElementById('decryptBtn');
    const messageInput = document.getElementById('message');
    const publicKeyDisplay = document.getElementById('publicKey');
    const privateKeyDisplay = document.getElementById('privateKey');
    const ciphertextDisplay = document.getElementById('ciphertext');
    const sharedSecretDisplay = document.getElementById('sharedSecret');
    const resultDisplay = document.getElementById('result');
    const errorDisplay = document.getElementById('error');

    // Initialize error display
    function showError(message) {
        errorDisplay.textContent = message;
        errorDisplay.classList.remove('d-none');
    }

    function hideError() {
        errorDisplay.classList.add('d-none');
    }

    // Generate keys
    generateBtn.addEventListener('click', async function() {
        try {
            hideError();
            const response = await fetch('/generate_keys', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error('Failed to generate keys');
            }

            const data = await response.json();
            publicKeyDisplay.textContent = data.public_key;
            privateKeyDisplay.textContent = data.private_key;
            
            // Clear previous results
            ciphertextDisplay.textContent = 'Not encrypted yet';
            sharedSecretDisplay.textContent = 'Not generated yet';
            resultDisplay.textContent = 'Not decrypted yet';
        } catch (error) {
            showError(error.message);
        }
    });

    // Encrypt message
    encryptBtn.addEventListener('click', async function() {
        try {
            hideError();
            const message = messageInput.value.trim();
            if (!message) {
                throw new Error('Please enter a message to encrypt');
            }

            const response = await fetch('/encrypt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to encrypt message');
            }

            const data = await response.json();
            ciphertextDisplay.textContent = data.ciphertext;
            sharedSecretDisplay.textContent = data.shared_secret;
        } catch (error) {
            showError(error.message);
        }
    });

    // Decrypt message
    decryptBtn.addEventListener('click', async function() {
        try {
            hideError();
            const ciphertext = ciphertextDisplay.textContent;
            if (ciphertext === 'Not encrypted yet') {
                throw new Error('Please encrypt a message first');
            }

            const response = await fetch('/decrypt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ ciphertext })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to decrypt message');
            }

            const data = await response.json();
            resultDisplay.textContent = 'Decryption successful! Shared secret: ' + data.shared_secret;
        } catch (error) {
            showError(error.message);
        }
    });
}); 
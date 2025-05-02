# Post-Quantum Cryptography Web Application Report

## Group Members
- Muhammad Sohail
- Haseeb Ahmed
- Raja Obaid

## GitHub Repository
[Post-Quantum Cryptography Web Application](https://github.com/sohail9221/Post-Quantum-Cryptography-webapp.git)

## Introduction
This report documents the development and implementation of a web application that demonstrates Post-Quantum Cryptography (PQC) using the Kyber512 algorithm. The application provides a user-friendly interface for generating quantum-resistant key pairs, encrypting messages, and decrypting ciphertext.

## Application Screenshots

### Home Page
![Home Page](pqc_1.png)
*Figure 1: The home page provides an introduction to Post-Quantum Cryptography and an overview of the Kyber512 algorithm.*

### Demo Interface
![Demo Interface](pqc_2.png)
*Figure 2: The interactive demo interface showing the key generation, encryption, and decryption steps.*



## Post-Quantum Cryptography Algorithm: Kyber512

### Overview
Kyber512 is a lattice-based key encapsulation mechanism (KEM) that has been selected by NIST for standardization as part of their Post-Quantum Cryptography standardization process. It is designed to be resistant to attacks from both classical and quantum computers.

### Technical Specifications
- **Security Level**: 128-bit
- **Type**: Lattice-based cryptography
- **Base Problem**: Module Learning With Errors (Module-LWE)
- **Key Sizes**:
  - Public Key: 800 bytes
  - Private Key: 1,632 bytes
  - Ciphertext: 768 bytes
- **Shared Secret**: 32 bytes

### Security Features
1. **Quantum Resistance**: Based on mathematical problems that are believed to be hard for quantum computers to solve
2. **Compact Implementation**: Relatively small key and ciphertext sizes compared to other PQC algorithms
3. **Efficient Operations**: Fast key generation, encryption, and decryption processes
4. **Provable Security**: Security is based on the hardness of the Module-LWE problem

## Application Architecture

### Frontend Components
1. **Home Page**
   - Introduction to Post-Quantum Cryptography
   - Overview of the Kyber512 algorithm
   - Navigation to the demo interface

2. **Demo Interface**
   - Step-by-step cryptographic operations
   - Real-time key generation
   - Message encryption and decryption
   - Visual feedback and error handling

### Backend Implementation
1. **Flask Web Server**
   - RESTful API endpoints
   - Secure session management
   - Error handling and validation

2. **Cryptographic Operations**
   - Key pair generation
   - Message encryption
   - Ciphertext decryption
   - Shared secret derivation

## Working Explanation

### 1. Key Generation Process
1. User initiates key generation through the web interface
2. Backend generates a Kyber512 key pair:
   - Public key for encryption
   - Private key for decryption
3. Keys are encoded in Base64 for display and transmission
4. Keys are stored securely in memory for the session

### 2. Encryption Process
1. User enters a message to encrypt
2. System uses the generated public key to:
   - Create a shared secret
   - Encrypt the message into ciphertext
3. Both the ciphertext and shared secret are displayed to the user
4. The shared secret can be used for further secure communication

### 3. Decryption Process
1. User initiates decryption of the ciphertext
2. System uses the private key to:
   - Decrypt the ciphertext
   - Recover the shared secret
3. The decrypted result is displayed to the user
4. Verification of successful decryption is performed

## Security Considerations

### Implemented Security Measures
1. **Secure HTTP Headers**
   - Content Security Policy (CSP)
   - HTTP Strict Transport Security (HSTS)
   - X-Content-Type-Options
   - X-Frame-Options

2. **Session Security**
   - Secure session cookies
   - HTTP-only cookies
   - SameSite cookie attributes

3. **Input Validation**
   - Sanitization of user inputs
   - Error handling without exposing sensitive information
   - Rate limiting for API endpoints

### Best Practices
1. Keys are generated securely using the Kyber512 algorithm
2. All cryptographic operations are performed server-side
3. Sensitive data is never stored permanently
4. Error messages are user-friendly without exposing technical details

## Conclusion
The Post-Quantum Cryptography web application successfully demonstrates the implementation and use of the Kyber512 algorithm. It provides an accessible interface for users to understand and experiment with quantum-resistant cryptography, preparing for the future of secure communications in the quantum computing era.

## Future Enhancements
1. Support for additional PQC algorithms
2. Implementation of hybrid cryptography (combining classical and post-quantum algorithms)
3. Enhanced key management system
4. Additional security features and user authentication
5. Performance optimizations for large-scale deployment 
Ardian Web Security Lab

Local Web Authentication Security Lab built for hands-on cybersecurity learning and authorized security testing.

Overview

This project is a small web authentication laboratory built with Python and HTML.

The lab demonstrates how a login system processes credentials, stores password hashes with per-user salts, verifies authentication attempts, and can be tested in a controlled localhost environment.

Environment: Localhost ("127.0.0.1")

Architecture

HTML Login Form
       ↓
Python HTTP Server
       ↓
Authentication
       ↓
Salt + Password Hash
       ↓
users.json
       ↓
Authentication Verification
       ↓
Security Testing

Technologies

- Python
- HTML
- Linux / Termux
- JSON
- HTTP
- cURL
- Git / GitHub

Project Structure

web-security-lab/
├── index.html
├── server.py
├── create_user.py
├── users.json
└── README.md

«"users.json" is used only for the local lab and should not be uploaded to a public repository.»

Security Implementation

The lab implements:

- Username and password authentication
- Random per-user salt generation
- SHA-256 password hashing
- Password verification using the stored salt
- HTTP status codes for authentication results
- Local-only security testing

The authentication flow:

Password
   ↓
Random Salt
   ↓
SHA-256(Salt + Password)
   ↓
Password Hash
   ↓
Stored locally

Security Testing

The authentication endpoint was tested locally using cURL.

Valid credentials

POST /login
→ HTTP 200 OK
→ Login berhasil

Invalid credentials

POST /login
→ HTTP 401 Unauthorized
→ Login gagal

These tests were performed only against the authorized local laboratory environment.

Security Considerations

This project is intended for education and experimentation.

Plain SHA-256 is not recommended for production password storage because it is designed to be fast. A production authentication system should use a password-specific key derivation function such as:

- Argon2
- scrypt
- PBKDF2

A production system should also implement additional protections such as secure sessions, HTTPS, rate limiting, CSRF protection, secure cookies, and appropriate access controls.

Skills Demonstrated

- Basic web security concepts
- HTTP request/response analysis
- Authentication fundamentals
- Password hashing and salting
- Authentication verification
- Linux command-line usage
- Python scripting
- Local security testing
- Technical documentation
- Responsible and authorized security testing

Authorization

All security testing in this project is performed against a locally controlled environment.

No unauthorized access, credential theft, database extraction, or testing against third-party systems is part of this project.

Project Status

Completed — Initial Authentication Security Lab

Future improvements may include:

- Secure password hashing with Argon2
- Session-based authentication
- Login attempt rate limiting
- CSRF protection
- Security logging
- Input validation
- Automated security tests
- Basic vulnerability assessment report

Author

Muhammad Ardiansyah (Ardian)

Junior Cybersecurity / Web Security Enthusiast

Interested in web security, vulnerability assessment, security testing, Linux, and Python.

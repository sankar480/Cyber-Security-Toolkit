# Cyber-Security-Toolkit #
Welcome to the **Cyber Security Toolkit**, your all-in-one app designed to enhance digital security through powerful tools and user-friendly interfaces. Whether you're securing your personal data or analyzing potential threats, this toolkit has got you covered and it's free to use.

## 🎯 About This Project ##
The Cyber Security Toolkit integrates various essential tools like encryption, phishing link scanning, password generation, and file cryptography. Built with Streamlit, this app is simple to use and perfect for individuals and organizations aiming to safeguard their digital assets.

## 🚀 Features ##
* Temporary Email Generator: Quickly create disposable email addresses.

* Password Generator: Generate strong, customizable passwords.
* Phishing Link Scanner: Analyze URLs to detect potential phishing threats.
* File Cryptography: Encrypt and decrypt files with strong methods.
* PDF Decryptor: Attempt to unlock password-protected PDFs using a wordlist.
* Custom Cryptography Tool: Perform powerfull encryption and decryption.
* User-Friendly Interface: A sidebar-based navigation system for frendly-user access to all tools.

## Out Come of the Project ##

https://github.com/user-attachments/assets/895c1866-bc9d-4838-a6c5-1eff2c6d3793

## 🛠 How It Works ##
1. Navigation: Choose the tool you need from the sidebar menu.

2. Input Fields: Provide required data like text, files, or URLs.
3. Instant Results: Get results in real-time through an intuitive interface.
4. Export Options: Download encrypted/decrypted files, generated passwords, or other processed outputs.

## 📂 Code Highlights ##
**Main Components**
* **```easy.py:```** The primary program file managing app navigation and integration.

* **```crypto.py:```** Implements deterministic encryption and decryption for secure communication.
* **```file.py:```** Handles file encryption and decryption using the Fernet method.
* **```password.py:```** Generates secure passwords based on user preferences.
* **```link.py:```** Scans URLs to identify potential phishing risks.
* **```pdf.py:```** Attempts to decrypt PDF files using a wordlist.

### Why Streamlit? ###
**We chose Streamlit because:**
* It allows rapid development of interactive, web-based tools.

* It's lightweight and requires minimal setup for users.

## 🔧 Getting Started ##
1. Clone the repository:
```bash
git clone https://github.com/sankar480/Cyber-Security-Toolkit.git
cd Cyber-Security-Toolkit
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run easy.py
```
## File Structure ##
cyber-security-toolkit/

│

├── easy.py                 # Main program file for managing navigation and app logic

├── crypto.py               # Handles deterministic encryption and decryption

├── file.py                 # Provides file encryption and decryption using Fernet

├── password.py             # Generates customizable secure passwords

├── link.py                 # Scans URLs to detect phishing threats

├── pdf.py                  # Attempts to decrypt password-protected PDFs

├── Home.py                 # Home page layout and introduction

├── Email.py                # Temporary email generator

├── requirements.txt        # List of dependencies for the project

├── assets/                 # Directory for static assets

│   ├── style.css           # Custom styles for Streamlit

│   ├── images/             # Placeholder for images and logos

│   │   ├── logo.png        # Logo for the app

│   └── fonts/              # Placeholder for custom fonts

│       ├── Poppins-Bold.ttf

│       ├── Poppins-Medium.ttf

│

├── data/                   # Directory for sample or auxiliary files

│   ├── sample.pdf          # Example PDF file for testing

│   ├── wordlist.txt        # Wordlist file for PDF decryption

│

├── README.md               # Documentation for the project

└── .gitignore              # Specifies files and directories to ignore in version control


## 🛡 Security First ##
I take security seriously. Always handle sensitive data responsibly and ensure you use strong passwords for critical operations. This toolkit is meant to aid security practices and not as a substitute for comprehensive cybersecurity measures.

## 🤝 Contributing ##
I welcome contributions! If you have ideas to improve or expand the toolkit, feel free to fork the repository, make changes, and submit a pull request.

## 📬 Feedback ##
Have suggestions or encountered issues? Open an issue on GitHub or contact us via email.

# password_cracker
This is an educational cybersecurity project to understand how dictionary attacks work against cryptographic hashes.

## Features

- Supports algorithms: **MD5**, **SHA-1**, and **SHA-256**.
- **Interactive Mode**: If you run the script without arguments, it will guide you step-by-step.

## Installation

1. Clone this repository.
2. Ensure you have Python installed.

## Usage

1. **Hash**: Enter the hash you want to crack.
2. **Wordlist**: Write the path to your password file (e.g., `passwords.txt`).
3. **Algorithm**: Indicate the algorithm (e.g., `md5`, `sha1`, `sha256`).

```powershell
py cracker.py
```

### Command Line Mode
```powershell
py cracker.py <hash> <wordlist_path> <algorithm>
```

### Examples
- **MD5**: `py cracker.py 482c811da5d5b4bc6d497ffa98491e38 passwords.txt md5`
- **SHA-1**: `py cracker.py d033e22ae348aeb5660fc2140aec35850c4da997 passwords.txt sha1`
- **SHA-256**: `py cracker.py 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 passwords.txt sha256`

## Additional Tools & Tips

- **Hash Generator**: You can use the `encryptor.py` tool at [password_encryptor](https://github.com/Alvarezz11/password_encryptor) to generate hashes for the passwords you want to test.
- **Expand Wordlist**: You can edit the `passwords.txt` file to add more passwords and make your dictionary attack more effective.

## How the Code Works

1. **Library Imports**: Uses `hashlib` to generate hashes (MD5, SHA1, SHA256) and `os`/`sys` to handle files and arguments.
2. **Dictionary Reading**: Opens the text file line by line to avoid crashing RAM.
3. **Hashing Process**:
   - Takes each word from the file and removes whitespace (`.strip()`).
   - Converts the word to bytes (`.encode()`).
   - Generates the hash using the selected algorithm (`md5()`, `sha1()`, or `sha256()`).
4. **Comparison**: Compares the generated hash with the one provided by the user. If they match, the password has been found.
5. **Interactive Mode**: If no console arguments are passed, the script uses `input()` to ask for data in a user-friendly way.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Note: This project was created for educational purposes.*

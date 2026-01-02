import hashlib
import sys
import os

def crack_password(target_hash, wordlist_path, algorithm):
    """
    Attempts to crack a hash using a dictionary attack.
    """
    if not os.path.exists(wordlist_path):
        print(f"[!] Error: The file {wordlist_path} does not exist.")
        return None

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            print(f"[*] Starting dictionary attack with {algorithm}...")
            for line in file:
                word = line.strip()
                # Create the hash of the current word
                if algorithm == 'md5':
                    h = hashlib.md5(word.encode()).hexdigest()
                elif algorithm == 'sha1':
                    h = hashlib.sha1(word.encode()).hexdigest()
                elif algorithm == 'sha256':
                    h = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print(f"[!] Algorithm {algorithm} not supported.")
                    return None

                # Compare with the target hash
                if h == target_hash:
                    return word
    except Exception as e:
        print(f"[!] Error reading file: {e}")
    
    return None

def main():
    print("--- Educational Password Cracker ---")
    
    # If no arguments are passed, enter interactive mode
    if len(sys.argv) < 4:
        print("\n[!] Not enough arguments provided.")
        print("[*] Entering interactive mode...")
        
        target_hash = input("Enter the hash to crack: ").strip().lower()
        wordlist_path = input("Enter the wordlist path (e.g., passwords.txt): ").strip()
        algorithm = input("Enter the algorithm (md5, sha1, sha256): ").strip().lower()
    else:
        target_hash = sys.argv[1].lower()
        wordlist_path = sys.argv[2]
        algorithm = sys.argv[3].lower()

    # Help example if password is not found
    usage_help = (
        "\nUsage: py cracker.py <hash> <wordlist_path> <algorithm>\n"
        "Supported algorithms: md5, sha1, sha256\n"
        "\nExamples:\n"
        "  - MD5 (password123): 482c811da5d5b4bc6d497ffa98491e38\n"
        "  - SHA1 (admin):      d033e22ae348aeb5660fc2140aec35850c4da997\n"
        "  - SHA256 (admin):    8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    )

    result = crack_password(target_hash, wordlist_path, algorithm)

    if result:
        print(f"\n[+] Password found!: {result}")
    else:
        print("\n[-] Could not find the password in the provided list.")
        print(usage_help)

if __name__ == "__main__":
    main()

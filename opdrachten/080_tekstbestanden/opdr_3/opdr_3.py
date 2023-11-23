# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(tekst):
    encrypted_text = ""
    for char in tekst:
        if char.isalpha():  # Controleer of het karakter een letter is
            shift = 5
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = 5
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Vraag de gebruiker om tekst in te voeren
invoer_tekst = input("Geef de tekst die je wilt encrypten: ")

# Encrypteer de tekst
geencrypteerde_tekst = encrypt(invoer_tekst)
print(f"Geëncrypteerde tekst: {geencrypteerde_tekst}")

# Decrypteer de geëncrypteerde tekst
gedecrypteerde_tekst = decrypt(geencrypteerde_tekst)
print(f"Gedecrypteerde tekst: {gedecrypteerde_tekst}")



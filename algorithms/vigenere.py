# =====================================================
# CLEAN KEY
# =====================================================

def generate_key(text, key):

    key = key.upper()

    key_list = []

    j = 0

    for char in text:

        if char.isalpha():

            key_list.append(key[j % len(key)])

            j += 1

        else:

            key_list.append(char)

    return ''.join(key_list)

# =====================================================
# ENCRYPT
# =====================================================

def vigenere_encrypt(text, key):

    result = ""
    process = []

    generated_key = generate_key(text, key)

    for i in range(len(text)):

        char = text[i]
        key_char = generated_key[i]

        if char.isalpha():

            is_upper = char.isupper()

            p = ord(char.upper()) - 65
            k = ord(key_char.upper()) - 65

            c = (p + k) % 26

            encrypted = chr(c + 65)

            if not is_upper:
                encrypted = encrypted.lower()

            result += encrypted

            process.append(
                f"{char} ({p}) + {key_char} ({k}) mod 26 = {c} → {encrypted}"
            )

        else:

            result += char

            process.append(
                f"{char} → karakter khusus/spasi tidak berubah"
            )

    return result, process

# =====================================================
# DECRYPT
# =====================================================

def vigenere_decrypt(text, key):

    result = ""
    process = []

    generated_key = generate_key(text, key)

    for i in range(len(text)):

        char = text[i]
        key_char = generated_key[i]

        if char.isalpha():

            is_upper = char.isupper()

            c = ord(char.upper()) - 65
            k = ord(key_char.upper()) - 65

            p = (c - k) % 26

            decrypted = chr(p + 65)

            if not is_upper:
                decrypted = decrypted.lower()

            result += decrypted

            process.append(
                f"{char} ({c}) - {key_char} ({k}) mod 26 = {p} → {decrypted}"
            )

        else:

            result += char

            process.append(
                f"{char} → karakter khusus/spasi tidak berubah"
            )

    return result, process
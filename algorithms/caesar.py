import string

ALPHABET = string.ascii_uppercase

# =====================================================
# ENCRYPT
# =====================================================

def caesar_encrypt(text, key):

    result = ""
    process = []

    for char in text:

        if char.isalpha():

            is_upper = char.isupper()

            old_index = ord(char.upper()) - 65

            new_index = (old_index + key) % 26

            encrypted = chr(new_index + 65)

            if not is_upper:
                encrypted = encrypted.lower()

            result += encrypted

            process.append(
                f"{char} → ({old_index} + {key}) mod 26 = {new_index} → {encrypted}"
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

def caesar_decrypt(text, key):

    result = ""
    process = []

    for char in text:

        if char.isalpha():

            is_upper = char.isupper()

            old_index = ord(char.upper()) - 65

            new_index = (old_index - key) % 26

            decrypted = chr(new_index + 65)

            if not is_upper:
                decrypted = decrypted.lower()

            result += decrypted

            process.append(
                f"{char} → ({old_index} - {key}) mod 26 = {new_index} → {decrypted}"
            )

        else:

            result += char

            process.append(
                f"{char} → karakter khusus/spasi tidak berubah"
            )

    return result, process
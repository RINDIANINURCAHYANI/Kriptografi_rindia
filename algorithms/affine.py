# =====================================================
# GCD
# =====================================================

def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a

# =====================================================
# MOD INVERSE
# =====================================================

def mod_inverse(a, m):

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return None

# =====================================================
# ENCRYPT
# =====================================================

def affine_encrypt(text, a, b):

    process = []
    result = ""

    if gcd(a, 26) != 1:

        process.append(
            "Nilai 'a' harus relatif prima dengan 26!"
        )

        return "", process

    for char in text:

        if char.isalpha():

            is_upper = char.isupper()

            x = ord(char.upper()) - 65

            encrypted_num = (a * x + b) % 26

            encrypted = chr(encrypted_num + 65)

            if not is_upper:
                encrypted = encrypted.lower()

            result += encrypted

            process.append(
                f"E({x}) = ({a}×{x}+{b}) mod 26 = {encrypted_num} → {encrypted}"
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

def affine_decrypt(text, a, b):

    process = []
    result = ""

    inverse = mod_inverse(a, 26)

    if inverse is None:

        process.append(
            "Inverse modulo tidak ditemukan!"
        )

        return "", process

    for char in text:

        if char.isalpha():

            is_upper = char.isupper()

            y = ord(char.upper()) - 65

            decrypted_num = (inverse * (y - b)) % 26

            decrypted = chr(decrypted_num + 65)

            if not is_upper:
                decrypted = decrypted.lower()

            result += decrypted

            process.append(
                f"D({y}) = {inverse} × ({y}-{b}) mod 26 = {decrypted_num} → {decrypted}"
            )

        else:

            result += char

            process.append(
                f"{char} → karakter khusus/spasi tidak berubah"
            )

    return result, process
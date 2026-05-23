import numpy as np

# =====================================================
# TEXT TO NUMBER
# =====================================================

def text_to_numbers(text):

    numbers = []

    for char in text:

        if char.isalpha():

            numbers.append(ord(char.upper()) - 65)

    return numbers

# =====================================================
# NUMBER TO TEXT
# =====================================================

def numbers_to_text(numbers):

    text = ""

    for num in numbers:

        text += chr((num % 26) + 65)

    return text

# =====================================================
# ENCRYPT
# =====================================================

def hill_encrypt(text, matrix_input):

    process = []

    try:

        # =================================================
        # FIX UTAMA: matrix_input SUDAH LIST dari Flask
        # =================================================

        matrix_values = matrix_input  # 🔥 TIDAK PERLU SPLIT LAGI

        # 2x2 MATRIX
        if len(matrix_values) == 4:

            matrix = np.array(matrix_values).reshape(2, 2)
            size = 2

        # 3x3 MATRIX
        elif len(matrix_values) == 9:

            matrix = np.array(matrix_values).reshape(3, 3)
            size = 3

        else:

            process.append("Matrix harus 2x2 atau 3x3!")
            return "", process

        process.append(f"Matrix Key:\n{matrix}")

        # =================================================
        # TEXT PROCESSING
        # =================================================

        numbers = text_to_numbers(text)

        # padding (biar genap sesuai matrix)
        while len(numbers) % size != 0:
            numbers.append(23)

        result_numbers = []

        # =================================================
        # MATRIX MULTIPLICATION
        # =================================================

        for i in range(0, len(numbers), size):

            block = np.array(numbers[i:i+size])

            encrypted = np.dot(matrix, block) % 26

            process.append(
                f"{matrix} × {block} mod 26 = {encrypted}"
            )

            result_numbers.extend(encrypted)

        result = numbers_to_text(result_numbers)

        return result, process

    except Exception as e:

        process.append(f"Error: {str(e)}")

        return "", process
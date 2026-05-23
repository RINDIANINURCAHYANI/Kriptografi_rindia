import string

# =====================================================
# GENERATE MATRIX
# =====================================================

def generate_matrix(key):

    key = key.upper().replace("J", "I")

    used = []
    matrix = []

    for char in key:

        if char.isalpha() and char not in used:
            used.append(char)

    for char in string.ascii_uppercase:

        if char == "J":
            continue

        if char not in used:
            used.append(char)

    for i in range(0, 25, 5):

        matrix.append(
            used[i:i+5]
        )

    return matrix

# =====================================================
# FIND POSITION
# =====================================================

def find_position(matrix, char):

    for row in range(5):

        for col in range(5):

            if matrix[row][col] == char:
                return row, col

# =====================================================
# PREPARE TEXT
# =====================================================

def prepare_text(text):

    text = text.upper().replace("J", "I")

    cleaned = ""

    for char in text:

        if char.isalpha():
            cleaned += char

    pairs = []

    i = 0

    while i < len(cleaned):

        a = cleaned[i]

        if i + 1 < len(cleaned):
            b = cleaned[i + 1]
        else:
            b = "X"

        if a == b:

            pairs.append(a + "X")
            i += 1

        else:

            pairs.append(a + b)
            i += 2

    if len(pairs[-1]) == 1:
        pairs[-1] += "X"

    return pairs

# =====================================================
# ENCRYPT
# =====================================================

def playfair_encrypt(text, key):

    matrix = generate_matrix(key)

    pairs = prepare_text(text)

    process = []

    result = ""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # SAME ROW
        if row1 == row2:

            enc1 = matrix[row1][(col1 + 1) % 5]
            enc2 = matrix[row2][(col2 + 1) % 5]

            rule = "Same Row"

        # SAME COLUMN
        elif col1 == col2:

            enc1 = matrix[(row1 + 1) % 5][col1]
            enc2 = matrix[(row2 + 1) % 5][col2]

            rule = "Same Column"

        # RECTANGLE
        else:

            enc1 = matrix[row1][col2]
            enc2 = matrix[row2][col1]

            rule = "Rectangle Rule"

        encrypted_pair = enc1 + enc2

        result += encrypted_pair

        process.append(
            f"{pair} → {encrypted_pair} ({rule})"
        )

    return result, matrix, pairs, process
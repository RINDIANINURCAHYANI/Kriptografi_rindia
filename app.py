from flask import Flask, render_template, request, redirect, url_for, session

from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from algorithms.affine import affine_encrypt, affine_decrypt
from algorithms.hill import hill_encrypt
from algorithms.playfair import playfair_encrypt

app = Flask(__name__)
app.secret_key = "crypto_secret_key"

# =========================================
# HISTORY FUNCTIONS
# =========================================

def get_history():
    return session.get("history", [])

def add_history(algorithm, mode, input_text, result):
    history = session.get("history", [])

    history.append({
        "algorithm": algorithm,
        "mode": mode,
        "input": input_text,
        "result": result
    })

    session["history"] = history

# =========================================
# HOME
# =========================================

@app.route('/')
def index():

    return render_template(
        'index.html',
        history=session.get("history", [])
    )

# =========================================
# THEORY PAGE
# =========================================

@app.route('/theory')
def theory():

    return render_template(
        'theory.html',
        history=session.get("history", [])
    )
def index():
    return render_template('index.html', history=get_history())

# =========================================
# CLEAR HISTORY
# =========================================

@app.route('/clear_history')
def clear_history():
    session["history"] = []
    return redirect(request.referrer or url_for('index'))

# =========================================
# CAESAR
# =========================================

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():

    result = ""
    process = []

    if request.method == 'POST':

        text = request.form['text']
        key = int(request.form['key'])
        mode = request.form['mode']

        if mode == 'encrypt':
            result, process = caesar_encrypt(text, key)
        else:
            result, process = caesar_decrypt(text, key)

        add_history("Caesar Cipher", mode, text, result)

    return render_template(
        'caesar.html',
        result=result,
        process=process,
        history=get_history()
    )

# =========================================
# VIGENERE
# =========================================

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():

    result = ""
    process = []

    if request.method == 'POST':

        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']

        if mode == 'encrypt':
            result, process = vigenere_encrypt(text, key)
        else:
            result, process = vigenere_decrypt(text, key)

        add_history("Vigenere Cipher", mode, text, result)

    return render_template(
        'vigenere.html',
        result=result,
        process=process,
        history=get_history()
    )

# =========================================
# AFFINE
# =========================================

@app.route('/affine', methods=['GET', 'POST'])
def affine():

    result = ""
    process = []

    if request.method == 'POST':

        text = request.form['text']
        a = int(request.form['a'])
        b = int(request.form['b'])
        mode = request.form['mode']

        if mode == 'encrypt':
            result, process = affine_encrypt(text, a, b)
        else:
            result, process = affine_decrypt(text, a, b)

        add_history("Affine Cipher", mode, text, result)

    return render_template(
        'affine.html',
        result=result,
        process=process,
        history=get_history()
    )

# =========================================
# HILL
# =========================================


@app.route('/hill', methods=['GET', 'POST'])
def hill():

    result = ""
    process = []

    if request.method == 'POST':

        text = request.form['text']
        matrix_size = int(request.form['matrix_size'])

        matrix = []

        for i in range(matrix_size * matrix_size):

            value = request.form.get(f"m{i}", "0")

            if value == "":
                value = "0"

            matrix.append(int(value))

        result, process = hill_encrypt(text, matrix)

        add_history("Hill Cipher", "encrypt", text, result)

    return render_template(
        'hill.html',
        result=result,
        process=process,
        history=get_history()
    )
# =========================================
# PLAYFAIR
# =========================================

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():

    result = ""
    matrix = []
    pairs = []
    process = []

    if request.method == 'POST':

        text = request.form['text']
        key = request.form['key']

        result, matrix, pairs, process = playfair_encrypt(text, key)

        add_history("Playfair Cipher", "encrypt", text, result)

    return render_template(
        'playfair.html',
        result=result,
        matrix=matrix,
        pairs=pairs,
        process=process,
        history=get_history()
    )

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
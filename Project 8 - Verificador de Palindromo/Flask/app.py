from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(word):
    # fl (front letters) / bl (back letters)

    bl = len(word) - 1

    for fl in range(len(word)):
        if word[fl] == word[bl]:
            bl = bl - 1
            if fl == bl:
                break
        else:
            return False
    return True

@app.route('/', methods=["GET", "POST"])

def index():
    result = None
    word = ""
    
    if request.method == "POST":
        word = request.form.get('word', "").strip()

        if word:
            if word.lower() == "sair":
                result = "Programa encerrado."
            elif is_palindrome(word.lower()):
                result = f"'{word}' é um palíndromo."
            else:
                result = f"'{word}' não é um palíndromo."

    return render_template('index.html', result = result, word=word)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
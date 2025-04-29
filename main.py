from flask import Flask, request
import re
from itertools import combinations

app = Flask(__name__)

def is_addition_query(q):
    print(f"Checking if query is addition: {q}")
    return ' ' in q and re.search(r'\d', q) and not q.startswith('<') and not q.endswith('>')

def simple_addition(q):
    print(f"Performing simple addition on query: {q}")
    parts = re.split(r'[\+=\? ]+', q)
    try:
        numbers = [int(x) for x in parts if x]
        return str(sum(numbers))
    except ValueError:
        return "Error: Invalid numbers in query.", 400

def count_words_consonants_vowels(q):
    print(f"Counting words, consonants, and vowels in query: {q}")
    try:
        vowels = 'aeiouAEIOU'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        words = q.split()
        return f"{len(words)}-{sum(c in consonants for c in q)}-{sum(c in vowels for c in q)}"
    except ValueError:
        return "Error: Invalid input.", 400

def bonus_combinations(q):
    print(f"Processing combinations query: {q}")
    try:
        numbers = list(map(int, q[1:-1].strip().split()))
        sums = sorted(set(a + b for a, b in combinations(numbers, 2)))
        return ' '.join(map(str, sums[:5]))
    except Exception as e:
        return f"Error parsing bonus 1: {e}", 400

@app.route('/', methods=['GET'])
def query_actions():
    q = request.args.get('q', '')
    print(f"Received query: {q}")

    special_cases = {
        'PING': "PONG",
        'What is your name?': "Ignacio Rojas",
        'What is your quest?': "coding",
        'Source code for this exercise?': "https://github.com/naxoxhide/vacasa-coding-exercise"
    }

    if q in special_cases:
        return special_cases[q], 200
    elif is_addition_query(q):
        return simple_addition(q)
    elif q.startswith('<') and q.endswith('>'):
        return bonus_combinations(q)
    elif any(c.isalpha() for c in q):
        if re.fullmatch(r'[A-Za-z ]+', q):
            return count_words_consonants_vowels(q)
    else:
        return "The query could not be interpreted.", 400

if __name__ == '__main__':
    app.run(port=3000,threaded=True)
from random import choice
secret_word = None
def generate_word():
    vocabulary = dict()

    with open('words.txt', 'r', encoding='utf-8') as file:
        for i in range(100):
            text = file.readline().split('-')
            if len(text[0]) <= 12:
                vocabulary[text[0].strip().upper()] = text[1].strip()
        secret_word = (choice(list(vocabulary.keys())))
    clue = vocabulary[secret_word]
    word = ['_' for i in range(len(secret_word))]

    return clue, word, secret_word


if __name__ == "__main__":
    print(generate_word())
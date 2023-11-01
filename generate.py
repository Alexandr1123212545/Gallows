from random import choice

secret_word = None

def generate_word():
    """
    generate secret word from words_uk.txt

    secret_word = random words
    vocabulary - key: secret word, value: clue from secret word
    number_words - words_uk.txt stores 25 pairs
    word - sheet consistig of underscores. number underscors == len(secret_word)
    clue - hint for the player
    """
    vocabulary = dict()
    number_words = 25

    with open('words_uk.txt', 'r', encoding='utf-8') as file:
        for i in range(number_words):
            text = file.readline().strip().split(' - ')
            vocabulary[text[0].upper()] = text[1]
        secret_word = (choice(list(vocabulary.keys())))
    clue = vocabulary[secret_word]
    word = ['_' for i in range(len(secret_word))]

    return clue, word, secret_word


if __name__ == "__main__":
    print(*generate_word(), sep='\n')


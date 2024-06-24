import csv
import random

from numpy.core.defchararray import lower


def play_game(word_list: list):
    tip = []

    index = random.randint(1, len(word_list))

    chosen_word = word_list[index - 1]

    for i in range(0, len(chosen_word)):
        tip.append("_")

    guess_number = 5


    guess_input = set()
    guess_incorrect = set()

    winner = False
    while guess_number > 0:
        guess = input("Escolha uma letra: ")
        guess_input.add(guess)

        if guess in chosen_word:
            print(f"letra: {guess} correto !")
            print(f"Tip: {' '.join(get_tip(guess, chosen_word, tip))}")
        else:
            if guess in guess_incorrect:
                print(f"Você já tentou a letra {guess}, tente outra letra !")
            else:
                guess_incorrect.add(guess)
                guess_number = guess_number - 1
                print(f"Letra: {guess} INCORRETA ! Você tem mais {guess_number} tentativas.")
                print(f"Tip: {' '.join(tip)}")

        if not "_" in tip:
            winner = True
            break

    if not winner:
        print(f"Você perdeu ... A palavra era {''.join(chosen_word)}")
    else:
        print(f"Parabéns, você acertou ! A palavra é {''.join(tip) }")


def get_tip(input_letter: str, word: str, tip: str) -> list:
    for i in range(0, len(word)):
        if input_letter == word[i]:
            tip[i] = input_letter
    return tip

def get_pokemon_list() -> list:
    pokemon_list = []
    reader = csv.DictReader(open('pokemon.csv'))
    dictobj = list(reader)
    for item in dictobj:
        pokemon_list.append(item['Name'].lower())

    return pokemon_list

def clean_composed_names(pokemon_list: list) -> list:
    for item in pokemon_list:
        if " " in item:
            pokemon_list.remove(item)

    return pokemon_list

if __name__ == '__main__':
    size = int(input("Quantos pokemons você quer considerar no jogo ?"))
    pokemon_list = clean_composed_names(get_pokemon_list())
    word_list = clean_composed_names(pokemon_list)[0:size]
    play_game(word_list)

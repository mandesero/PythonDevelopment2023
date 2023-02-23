import argparse
import urllib
from random import randint
from cowsay import cowsay, list_cows


def bullscows(guess: str, secret: str) -> (int, int):
    return sum(i == k for i, k in zip(guess, secret)), len(
        set(guess).intersection(secret)
    )


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    count = 0
    format_string = "Быки: {}, Коровы: {}"
    prompt = "Введите слово: "
    secret = words[randint(0, len(words) - 1)]
    while True:
        count += 1
        user_word = ask(prompt)
        inform(format_string, *bullscows(user_word, secret))
        if user_word == secret:
            return count


def ask(prompt: str, valid: list[str] = None) -> str:
    prompt = cowsay(prompt, cow=list_cows()[randint(0, len(list_cows()))])
    print(prompt)
    if valid:
        while buff := input():
            if buff in valid:
                return buff
            print("Not valid word, try again.")
    return input()


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay(
        format_string.format(bulls, cows),
        cow=list_cows()[randint(0, len(list_cows()))]
    ))


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary")
    parser.add_argument("length", type=int, default=5)
    return parser


def main():
    args = parser().parse_args()
    url, length = args.dictionary, args.length
    try:
        urllib.request.urlretrieve(url, "dictionary")
    except:
        pass

    with open("dictionary", "r") as file:
        words = [word.strip() for word in file if len(word.strip()) == length]

    print(gameplay(ask, inform, words))


if __name__ == "__main__":
    main()

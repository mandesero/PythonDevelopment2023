import argparse
import urllib
from random import randint


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

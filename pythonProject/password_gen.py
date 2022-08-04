from random import *
from string import *


def create_chars():
    chars = []
    print("Приветствую! Я - генератор надежных паролей.")
    n = int(input("Какое количество паролей будем генерировать?\n")).strip()
    while n < 1:
        n = int(input("Давай попробуем еще разочек :)\nКакое количество паролей будем генерировать?\n")).strip()
    lengh = int(input("Отлично! Пароль считается надёжным, если он состоит не менее чем из 8 символов. Какую длину будем использовать?\n")).strip()
    while lengh < 8:
        lengh = int(input("Давай попробуем еще разочек :)\nДлина пароля должна быть не менее 8 символов\n")).strip()
    if input_parametr('цифры'):
        chars.extend(digits)
    if input_parametr('прописные буквы'):
        chars.extend(ascii_uppercase)
    if input_parametr('строчные буквы'):
        chars.extend(ascii_lowercase)
    if input_parametr('символы'):
        chars.extend(punctuation)
    if not input_parametr('неоднозначные символы il1Io0O|'):
        for c in chars:
            if c in 'il1Io0O|':
                chars.remove(c)
    return n, lengh, chars


def input_parametr(s):
    text = input(f"Будем ли включать в пароль {s}? Если да, введи 'да', в противном случае 'нет'\n").strip()
    while text.lower() != 'да' and text.lower() != 'нет':
        text = input("Ошибка ввода: введите 'да' или 'нет'\n").strip()
    if text.lower() == 'да':
        flag = True
    else:
        flag = False
    return flag


def generate_password(length, chars):
    password = sample(chars, length)
    return ''.join(password)


def main():
    n, length, chars = create_chars()
    passwords = [generate_password(length, chars) for _ in range(n)]
    print(*passwords, sep='\n')


if __name__ == "__main__":
    main()

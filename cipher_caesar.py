def cipher_word(text, n):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    new_str = []
    for c in text:
        if c in lower_eng_alphabet:
            new_str.append(temp(lower_eng_alphabet, c, n))
        elif c in upper_eng_alphabet:
            new_str.append(temp(upper_eng_alphabet, c, n))
        elif c in lower_rus_alphabet:
            new_str.append(temp(lower_rus_alphabet, c, n))
        elif c in upper_rus_alphabet:
            new_str.append(temp(upper_rus_alphabet, c, n))
        else:
            new_str.append(c)
    return ''.join(new_str)


def cipher(text):
    result = []
    for elem in text:
        n = get_word_len(elem)
        result.append(cipher_word(elem, n))
    return result


def temp(string, c, n):
    length = len(string)
    new_num = get_num(string.index(c), n, length)
    return string[new_num]


def get_num(c, n, length):
    num = c + n
    if num > 25:
        num -= 26
    return num


def get_word_len(text):
    length = 0
    all_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    for c in text:
        if c in all_chars:
            length += 1
    return length


def main():
    text = input().strip().split()
    print(' '.join(cipher(text)))


if __name__ == "__main__":
    main()

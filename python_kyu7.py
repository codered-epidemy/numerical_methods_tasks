import math


def to_weird_case(words):
    weird_case = []
    weird_res = ''
    splitted_words = words.split()
    for splitted_word in splitted_words:
        for letter in splitted_word:
            if splitted_word.index(letter) % 2 == 0:
                letter.upper()
                weird_res += letter
            else:
                letter.lower()
                weird_res += letter
        weird_case.append(weird_res)
    res = ''
    for word in weird_case:
        res += word + ' '
    return res.strip()


def main():
    res = to_weird_case('This')
    print(res)


if __name__ == '__main__':
    main()

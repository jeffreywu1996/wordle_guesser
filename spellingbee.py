import sys
import re
from english_words import english_words_lower_alpha_set


def convert_to_regex(word):
    return word.replace('_', '[a-z]')


def get_words_with(words_set, word):
    words = set()
    regex_str = convert_to_regex(word)
    for w in words_set:
        if re.search(regex_str, w):
            words.add(w)
    return words


def filter_exclude(words_set: set, exclude: str):
    s = set()
    for w in words_set:
        if all([ch not in w for ch in exclude]):
            s.add(w)
    return s


def filter_include(words_set: set, include: str, must_have: str):
    s = set()
    ws2 = set()
    for w in words_set:
        if any([ch not in include for ch in w]):
            continue
        ws2.add(w)

    for w in ws2:
        if must_have in w and any([ch in w for ch in include]):
            s.add(w)
    return s


def main():
    include = sys.argv[1]
    must_have = sys.argv[2]

    print(f"Guess word is: {include}")

    # words_set = set(english_words_lower_alpha_set)
    words_set = set(filter(lambda x:len(x) >= 4, english_words_lower_alpha_set))
    # words_set = set(filter(lambda x:len(x) >= 4, english_words_lower_alpha_set))

    if include:
        words_set = filter_include(words_set, include, must_have)

    # guesses = get_words_with(words_set, word)
    guesses = words_set
    print(f'Possible guesses: {len(guesses)} results')
    print(guesses)

    print('Pretty print')
    for g in guesses:
        print(g)


if __name__ == "__main__":
    main()

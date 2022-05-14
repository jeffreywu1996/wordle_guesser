import argparse
import re

from english_words import english_words_lower_alpha_set


def convert_to_regex(word: str) -> str:
    return word.replace('_', '[a-z]')


def get_words_with(words_set: set, word: str) -> set:
    words = set()
    regex_str = convert_to_regex(word)
    for w in words_set:
        if re.search(regex_str, w):
            words.add(w)
    return words


def filter_exclude(words_set: set, exclude: str) -> set:
    s = set()
    for w in words_set:
        if all([ch not in w for ch in exclude]):
            s.add(w)
    return s


def filter_include(words_set: set, include: str) -> set:
    s = set()
    for w in words_set:
        if all([ch in w for ch in include]):
            s.add(w)
    return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="Guessed word with correct position, use _ for unknown. Ex: __ple if ple is in correct position")
    parser.add_argument("-i", "--include",
            help="characters that must be included in word. Can be in any order/repeated. Ex: abc")
    parser.add_argument("-e", "--exclude",
            help="characters that must be excluded in word. Can be in any order/repeated. Ex: aie")
    args = parser.parse_args()

    word = args.word
    if len(word) != 5:
        print('ERROR: Word can only be length of 5')
        exit(-1)

    print(f"Guess word is: {word}")

    words_set = set(filter(lambda x:len(x) == 5, english_words_lower_alpha_set))

    if args.exclude:
        words_set = filter_exclude(words_set, args.exclude)

    if args.include:
        words_set = filter_include(words_set, args.include)

    guesses = get_words_with(words_set, word)
    print(f'Possible guesses: {len(guesses)} results')
    print(guesses)


if __name__ == "__main__":
    main()

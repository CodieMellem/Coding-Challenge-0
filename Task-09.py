
def print_vowels(random_word):
    all_vowels = "Vowels: "
    random_word = random_word.lower()
    for vowel in 'aeiou':
        if vowel in random_word:
            all_vowels +=  vowel + ' '

    print(all_vowels)


print_vowels("hElleO")
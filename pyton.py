#!/usr/bin/env python
# coding: utf-8

from random import choice

TURKISH_VOWELS = "aeıioöuüAEIİOÖUÜ"
HAIKU_SYLLABLES = [5, 7, 5]

def count_syllables(word):
    """Counts vowels in a word using TURKISH_VOWELS."""
    count = 0
    for char in word:
        if char in TURKISH_VOWELS:
            count += 1
    return count

# Define raw_words list including original and new words
raw_words = [
    # Original words from word_options
    "Büyüleyici", "Muhteşem", "Renkli", "Keyifli", "Hassas",
    "vizyonlar", "mesafe", "vicdan", "süreç", "kaos",
    "batıl", "zıt", "zarif", "davetkar", "çelişkili", "ezici",
    "doğru", "karanlık", "soğuk", "sıcak", "harika",
    "manzara","mevsim", "renkler","ışıklar","İlkbahar","Kış","Yaz","Sonbahar",
    "inkar edilemez", "güzel", "yeri doldurulamaz", "inanılmaz", "geri alınamaz",
    "ilham", "hayal gücü", "bilgelik", "düşünceler",
    # New words
    "kar", "kiraz", "yaprak", "güneş", "sessiz", "nehir", "yıldız", "eski",
    "yeni", "küçük", "büyük", "ve", "bir", "gölge", "rüya",
    # Adding a few more for variety
    "umut", "sevgi", "ay", "gece", "sabah", "dağ", "deniz"
]

# Create MASTER_WORD_LIST using a list comprehension
MASTER_WORD_LIST = [{'text': word, 'syllables': count_syllables(word)} for word in raw_words]

def choose_word(word_list, max_syllables):
    """Chooses a word from word_list with syllable count <= max_syllables."""
    eligible_words = [word for word in word_list if word['syllables'] <= max_syllables]
    if not eligible_words:
        return None
    return choice(eligible_words)

def generate_haiku_line(available_words_pool, target_syllables):
    """Generates a line of a Haiku with a target syllable count."""
    line_words = []
    current_syllables = 0

    # First word
    first_word_obj = choose_word(available_words_pool, target_syllables)
    if first_word_obj:
        line_words.append(first_word_obj['text'])
        current_syllables += first_word_obj['syllables']

        # Second word (optional)
        remaining_syllables = target_syllables - current_syllables
        if remaining_syllables > 0:
            second_word_obj = choose_word(available_words_pool, remaining_syllables)
            if second_word_obj:
                line_words.append(second_word_obj['text'])
                current_syllables += second_word_obj['syllables']

    return line_words, current_syllables

def generate_haiku():
    """Generates and prints a Haiku using MASTER_WORD_LIST."""
    # MASTER_WORD_LIST is now used directly
    all_word_choices = MASTER_WORD_LIST

    print(("-" * 30) + "\nHaiku Oluşturucu\n" + ("-" * 30))

    for i in range(3):
        target_syllables = HAIKU_SYLLABLES[i]
        line_words, total_syllables = generate_haiku_line(all_word_choices, target_syllables)
        print("{} ({} syllables)".format(" ".join(line_words), total_syllables))

if __name__ == "__main__":
    generate_haiku()

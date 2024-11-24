# example_usage.py
from text_analyzer import count_characters, count_spaces, count_uppercase, count_lowercase, count_punctuation, character_frequency, word_frequency,count_words, count_sentences, average_word_length, average_sentence_length, count_unique_words, unique_word_percentage, most_common_words,most_common_characters, generate_report

text = "Hello, World!"
print("Characters:", count_characters(text))
print("Spaces:", count_spaces(text))
print("Uppercase letters:", count_uppercase(text))
print("Lowercase letters:", count_lowercase(text))
print("Punctuation marks:", count_punctuation(text))
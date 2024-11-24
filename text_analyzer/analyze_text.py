import string

def count_characters(text):
    """Повертає загальну кількість символів у тексті."""
    return len(text)

def count_spaces(text):
    """Повертає кількість пробілів у тексті."""
    return text.count(' ')

def count_uppercase(text):
    """Повертає кількість великих літер у тексті."""
    return sum(1 for char in text if char.isupper())

def count_lowercase(text):
    """Повертає кількість малих літер у тексті."""
    return sum(1 for char in text if char.islower())

def count_punctuation(text):
    """Повертає кількість розділових знаків у тексті."""
    return sum(1 for char in text if char in string.punctuation)

def character_frequency(text):
    """Повертає словник із частотою кожного символу в тексті."""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def word_frequency(text):
    """Повертає словник із частотою кожного слова в тексті."""
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def count_words(text):
    """Повертає кількість слів у тексті."""
    return len(text.split())

def count_sentences(text):
    """Повертає кількість речень у тексті."""
    import re
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def average_word_length(text):
    """Повертає середню довжину слів у тексті."""
    words = text.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def average_sentence_length(text):
    """Повертає середню довжину речень у тексті."""
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0

def count_unique_words(text):
    """Повертає кількість унікальних слів у тексті."""
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def unique_word_percentage(text):
    """Повертає відсоток унікальних слів від загальної кількості слів."""
    words = text.split()
    unique_words = set(words)
    return len(unique_words) / len(words) * 100 if words else 0

def most_common_words(text, n=5):
    """Повертає список з `n` найчастіших слів у тексті."""
    frequency = word_frequency(text)
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:n]

def most_common_characters(text, n=5):
    """Повертає список з `n` найчастіших символів у тексті."""
    frequency = character_frequency(text)
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:n]

def generate_report(text):
    """Повертає звіт з основними метриками тексту."""
    report = {
        "Загальна кількість символів": count_characters(text),
        "Кількість пробілів": count_spaces(text),
        "Кількість великих літер": count_uppercase(text),
        "Кількість малих літер": count_lowercase(text),
        "Кількість розділових знаків": count_punctuation(text),
        "Кількість слів": count_words(text),
        "Кількість речень": count_sentences(text),
        "Середня довжина слова": average_word_length(text),
        "Середня довжина речення": average_sentence_length(text),
        "Кількість унікальних слів": count_unique_words(text),
        "Відсоток унікальних слів": unique_word_percentage(text),
        "Найчастіші слова": most_common_words(text),
        "Найчастіші символи": most_common_characters(text),
    }
    return report

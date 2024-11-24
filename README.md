# TextAnalyzer

**Author:** Denis,Markian
**Subject:** Data Science Tool  
**Description:** TextAnalyzer is a Python library for analyzing text structure. It helps analyze style and structure, making it useful for educational and professional needs.

## Features
- Count total characters, spaces, uppercase/lowercase letters, and punctuation marks.
- Analyze text structure and generate reports.

## Installation
```bash
pip install textanalyzer
```

## Usage
```python
from text_analyzer import count_characters, count_spaces, count_uppercase, count_lowercase, count_punctuation, character_frequency, word_frequency,count_words, count_sentences, average_word_length, average_sentence_length, count_unique_words, unique_word_percentage, most_common_words,most_common_characters, generate_report

text = "Hello, World!"
analysis = count_characters(text)
print(analysis)
```

## Project Structure
```
TextAnalyzer/
    LICENSE
    README.md
    setup.py
    pyproject.toml
    text_analyzer/
        __init__.py
        core.py
    tests/
        test_core.py
    example_usage.ipynb
```

## License
This project is licensed under the MIT License.

import re
from typing import Generator, List

# Base class for text preprocessing
class TextCleaner:
    def __init__(self, text: str):
        self.text = text

    def clean_text(self) -> str:
        text = self.text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
        text = re.sub(r"[^a-z\s]", "", text)  # remove punctuation/numbers
        text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
        return text

# Subclass that adds tokenization
class Tokenizer(TextCleaner):
    def __init__(self, text: str):
        super().__init__(text)

    def get_tokens(self) -> List[str]:
        cleaned = self.clean_text()
        return cleaned.split()

    # Generator that yields tokens one by one
    def token_generator(self) -> Generator[str, None, None]:
        for token in self.get_tokens():
            yield token

# Example usage
sample = "Mental health matters! Visit https://support.org for help."
processor = Tokenizer(sample)

# See cleaned tokens
processor.get_tokens()

# Use the generator
[token for token in processor.token_generator()]

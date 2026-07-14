from pathlib import Path

def load_skills(file_path: Path) -> set[str]:
    """Loads skills from a text file."""

    with open(file_path, "r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}
    
def generate_ngrams(tokens: list[str], n: int) -> set[str]:
    """Generates n-grams from a list of tokens."""
    return {f"{' '.join(tokens[i:i+n])}" for i in range(len(tokens) - n + 1)}


def extract_skills(text:str,skill_set:set[str])->set[str]:
    """
    Extracts skills from the preprocessed text based on a predefined skill set.

    Args:
        text (str): The input text from which to extract skills.
        skill_set (set[str]): A set of predefined skills to look for in the text.

    Returns:
        set[str]: A set of skills found in the text.
    """

    # Tokenize the processed text
    tokens = text.split()

    # Generate unigrams, bigrams, and trigrams
    unigrams = set(tokens)
    bigrams = generate_ngrams(tokens, 2)
    trigrams = generate_ngrams(tokens, 3)

    # Combine all phrases
    all_phrases = unigrams | bigrams | trigrams

    # Extract skills by checking if each phrase is in the skill set
    extracted_skills = {phrase for phrase in all_phrases if phrase in skill_set}


    return extracted_skills

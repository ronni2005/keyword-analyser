from pathlib import Path

def load_skills(file_path: Path) -> set[str]:
    """Loads skills from a text file."""

    with open(file_path, "r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}
    
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

    # Extract skills by checking if each token is in the skill set
    extracted_skills = {token for token in tokens if token in skill_set}

    return extracted_skills

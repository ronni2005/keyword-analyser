from pathlib import Path
from src.similarity import calculate_similarity
from src.preprocess import preprocess_text

def read_file(file_path:Path)->str:
    """Reads the content of a file and returns it as a string."""

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def interpret_score(score:float)->str:
    #->str represents return type of function
    """gives human readable interpretation"""
    if score>=0.70:
        return "best match"
    elif score>=0.50:
        return "good match"
    elif score>=0.30:
        return "poor match"
    return "very poor match"

def main():
    data_path=Path("data")
    resume_path=data_path/"resume.txt"
    jd_path=data_path/"job_description.txt"
    resume_text = preprocess_text(read_file(resume_path))
    jd_text = preprocess_text(read_file(jd_path))

    similarity = calculate_similarity(resume_text, jd_text)

    print(f"Resume match score: {similarity*100:.2f}%")
    print(f"Interpretation: {interpret_score(similarity)}")




if __name__=="__main__":
    main()
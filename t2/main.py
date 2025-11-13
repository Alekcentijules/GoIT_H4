"""Module for reading information about cats from a file."""

from pathlib import Path

def get_cats_info(path):
    """
    Reads a file with information about cats and returns a list of dictionaries.

    Args:
        path (str): Path to the file (format: id,name,age).

    Returns:
        List[Dict[str, str]]: List of dictionaries with keys 'id', 'name', 'age'.
                              Empty list if the file is not found.

    Examples:
        >>> get_cats_info("data/cats.txt")
        [{'id': '60b90c1c...', 'name': 'Tayson', 'age': '3'}, ...]
    """
    cats = []
    try:
        file_path = Path(path)
        if not file_path.exists():
            return []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 2)
                if len(parts) == 3:
                    id, name, age = parts
                    cats.append({"id": id, "name": name, "age": age})
        return cats
    
    except (FileNotFoundError, PermissionError):
         return []

cats_file = input("Enter a path to cats file: ")
cats_info = get_cats_info(cats_file) 

print(cats_info)
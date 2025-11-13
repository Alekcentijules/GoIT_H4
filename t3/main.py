"""Module for recursive output of directory structure with colors."""

import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def show_directory(path, indent=0):
    """
    Recursively outputs the directory structure with color formatting.

    Args:
        path (str): Path to the directory.
        indent (int): Indentation for nested levels (default is 0).

    Returns:
        None

    Raises:
        Outputs error messages (access, not a directory, etc.).
    """
    try:
        directory = Path(path).resolve()

        if not directory.exists():
            print(f"{Fore.RED} Error: Path {directory} does not exist!")
            return
        if not directory.is_dir():
            print(f"{Fore.RED} Error: {directory} is not a directory!")
            return
        
        indent_str = " " * indent
        for item in directory.iterdir():
            if item.is_dir():
                print(f"{indent_str}{Fore.BLUE} folder {item.name}")
                show_directory(item, indent + 1)
            else:
                print(f"{indent_str}{Fore.GREEN} file {item.name}")
        
    except PermissionError:
        print(f"{Fore.RED} Error: not access to {path}")
    except Exception as err:
        print(f"{Fore.RED} Unknown error: {str(err)}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Error: Specify the path to the directory!")
        print(f"For example: python {sys.argv[0]} picture")
        sys.exit(1)

    path = sys.argv[1]
    print(f"{Fore.CYAN}Directory structure: {path}")
    show_directory(path)

if __name__ == "__main__":
    main()
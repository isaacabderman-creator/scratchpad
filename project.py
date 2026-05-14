from pathlib import Path
from modules.interface import console, list_dir_content, show_file_content

MAIN_DIR: Path = Path("./college")


def main() -> None:
    console.print(show_file_content(MAIN_DIR, "example.md"))
    console.print(list_dir_content(MAIN_DIR))


if __name__ == "__main__":
    main()

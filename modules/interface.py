from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from os import listdir

console: Console = Console()


def show_file_content(DIR: Path, file_name: str) -> Panel:
    path: Path = DIR / file_name
    with path.open() as file:
        try:
            text: str = file.read()
            content: Panel = Panel(Markdown(text))
            return content

        except FileNotFoundError:
            return Panel("[red]File not found[/red]")


def list_dir_content(DIR: Path) -> str:
    content: list = listdir(DIR)
    return "\n".join(content)

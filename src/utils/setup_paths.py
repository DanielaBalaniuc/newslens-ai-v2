from pathlib import Path
import sys


def setup_project_path():
    """
    Add the project root to sys.path so notebooks can import from src.
    """
    project_root = Path.cwd().parent

    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    return project_root
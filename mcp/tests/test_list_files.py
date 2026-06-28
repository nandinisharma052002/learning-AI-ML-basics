import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.file_tools import list_files

# for workspace directory
print(list_files())

# for subdirectory inside workspace dir
print(list_files("notes"))
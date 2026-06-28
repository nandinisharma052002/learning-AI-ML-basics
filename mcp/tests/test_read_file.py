import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.file_tools import read_file

print(read_file("sample.txt"))

print(read_file("missing.txt"))

print(read_file("."))\

# for files outside the mcp folder
print(read_file("../README.md"))

# using pytest

def test_read_existing_file():
    result = read_file("sample.txt")
    assert  result["success"] is True
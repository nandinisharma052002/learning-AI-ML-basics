import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.file_tools import read_file,write_file

# result = write_file(
#     "notes/test.txt",
#     "Hello from MCP"
# )

# print(result)

# print("="*10)

# print(write_file(
#     "../hack.txt",
#     "BAD"
# ))


# roundtrip testing
result = write_file("roundtrip2.txt","This is roundtrip testing")

print(result)

print(read_file("roundtrip2.txt"))
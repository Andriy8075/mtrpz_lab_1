import sys
from interactive import interactive
from noninteractive import noninteractive as with_file

if len(sys.argv) == 2:
    file_path = sys.argv[1]
    with_file(file_path)
else:
    interactive()
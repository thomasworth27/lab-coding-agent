'''
This program prints stdin to the screen.
'''
import sys

def cat(file_obj, out):
    while True:
        chunk = file_obj.read1(CHUNK_SIZE)
        if not chunk:
            break
        out.write(chunk)

if __name__ == "__main__":
    out = sys.stdout.buffer

    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f, out)
    else:
        cat(sys.stdin.buffer, out)

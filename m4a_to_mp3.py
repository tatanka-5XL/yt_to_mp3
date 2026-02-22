import sys
import subprocess
from pathlib import Path

inp = Path(sys.argv[1])
out = inp.with_suffix(".mp3")

subprocess.run([
    "ffmpeg", "-i", str(inp),
    "-vn",
    "-codec:a", "libmp3lame",
    "-q:a", "2",
    str(out)
])

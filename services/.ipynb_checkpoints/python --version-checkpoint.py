import sys
import subprocess


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
print(f"Python {sys.version.split()[0]}")

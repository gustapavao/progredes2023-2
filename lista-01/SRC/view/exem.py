import os
from pathlib import Path

a = os.path.dirname(__file__)
a = a.replace("SRC/view", "arquivos_base")
print(a)
from pathlib import Path

path = Path("alice.txt")
nl = "agregando una línea"

path.write_text(nl, encoding="utf-8")
print(path.read_text(encoding="utf-8"))

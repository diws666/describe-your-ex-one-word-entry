import os

# Verified count: 11 characters (uninstalled)
WORD = "uninstalled"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
if output_dir:
    output_path = os.path.join(output_dir, "entry.txt")
else:
    output_path = "/output/entry.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(WORD)

print(len(WORD))

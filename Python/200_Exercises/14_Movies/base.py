from collections import defaultdict

script = """
COOPER: We're not meant to save the world. We're meant to leave it.

BRAND: We've got to find a way home.

TARS: Everybody good? Plenty of slaves for my robot colony?
"""

line_blocks = script.strip().split("\\n\\n")
character_dialogue = defaultdict(list)

for block in line_blocks:
    if ": " in block:
        name, text = block.split(": ", 1)
        character_dialogue[name.strip()].append(text.strip())

print("Cooper's dialogue:", character_dialogue["COOPER"])
print("TARS's dialogue:", character_dialogue["TARS"])
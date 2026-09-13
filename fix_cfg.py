import pathlib, shutil

base = "G:/Projects/1projects/rayquiro-docs"

# Restore working old-style config
new = pathlib.Path(base + "/src/content.config.ts")
if new.exists():
    new.unlink()
    print("Removed src/content.config.ts")

old = pathlib.Path(base + "/src/content/config.ts")
old.write_text(
    "import { defineCollection } from 'astro:content';\n"
    "import { docsSchema } from '@astrojs/starlight/schema';\n"
    "\n"
    "export const collections = {\n"
    "  docs: defineCollection({ type: 'content', schema: docsSchema() }),\n"
    "};\n",
    encoding="utf-8"
)
print("Wrote src/content/config.ts (type:content)")

# Check logo files
import os
assets = base + "/src/assets"
for f in os.listdir(assets):
    print("asset:", f)

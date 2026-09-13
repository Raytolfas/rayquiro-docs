import pathlib

cfg = pathlib.Path("G:/Projects/1projects/rayquiro-docs/astro.config.mjs")
cfg.write_text("""// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "RayQuiro",
      description: "Official documentation for the RayQuiro programming language",
      social: [
        { icon: "github", label: "GitHub", href: "https://github.com/raytolfas/rayquiro" },
      ],
      sidebar: [
        { label: "Getting Started", autogenerate: { directory: "getting-started" } },
        { label: "Language", autogenerate: { directory: "language" } },
        { label: "Built-in Modules", autogenerate: { directory: "built-ins" } },
        { label: "Package Manager", autogenerate: { directory: "package-manager" } },
        { label: "CLI", autogenerate: { directory: "cli" } },
        { label: "Guides", autogenerate: { directory: "guides" } },
      ],
      customCss: ["./src/styles/custom.css"],
    }),
  ],
});
""", encoding="utf-8")
print("astro.config.mjs updated (autogenerate)")

cc = pathlib.Path("G:/Projects/1projects/rayquiro-docs/src/content.config.ts")
cc.write_text(
    "import { defineCollection } from \\"astro:content\\";\n"
    "import { docsLoader } from \\"@astrojs/starlight/loaders\\";\n"
    "import { docsSchema } from \\"@astrojs/starlight/schema\\";\n"
    "\n"
    "export const collections = {\n"
    "  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),\n"
    "};\n",
    encoding="utf-8"
)
print("content.config.ts ok")


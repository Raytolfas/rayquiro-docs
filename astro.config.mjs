// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "RayQuiro",
      description: "RayQuiro programming language official documentation",
      logo: { src: "./src/assets/logo.png", replacesTitle: false },
      favicon: "/favicon.ico",
      social: [
        { icon: "github", label: "GitHub", href: "https://github.com/raytolfas/rayquiro" },
      ],
      sidebar: [
        { label: "Getting Started", autogenerate: { directory: "getting-started" } },
        { label: "Language",        autogenerate: { directory: "language" } },
        { label: "Built-ins",       autogenerate: { directory: "built-ins" } },
        { label: "Modules",         autogenerate: { directory: "modules" } },
        { label: "Packages",        autogenerate: { directory: "packages" } },
        { label: "CLI",             autogenerate: { directory: "cli" } },
        { label: "Guides",          autogenerate: { directory: "guides" } },
      ],
      customCss: ["./src/styles/custom.css"],
    }),
  ],
});

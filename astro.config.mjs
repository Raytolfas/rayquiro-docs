import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import starlightVersions from "starlight-versions";

export default defineConfig({
  integrations: [
    starlight({
      plugins: [
        starlightVersions({
          versions: [
            { slug: "0.2.1", label: "v0.2.1" },
          ],
        }),
      ],
      title: "RayQuiro",
      description: "RayQuiro programming language official documentation",
      logo: { src: "./src/assets/logo.png", replacesTitle: false },
      favicon: "/favicon.ico",
      defaultLocale: "root",
      locales: {
        root: {
          label: "English",
          lang: "en",
        },
        ru: {
          label: "Русский",
          lang: "ru",
        },
      },
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
        { label: "Core API",        autogenerate: { directory: "core-api" } },
        { label: "Guides",          autogenerate: { directory: "guides" } },
      ],
      customCss: ["./src/styles/custom.css"],
    }),
  ],
});

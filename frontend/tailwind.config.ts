import type { Config } from "tailwindcss";

const config: Config = {
    content: [
        "./app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                void: "#030014",
                neon: {
                    purple: "#A855F7",
                    blue: "#3B82F6",
                    pink: "#EC4899",
                }
            },
            backgroundImage: {
                'grid-pattern': "linear-gradient(to right, #ffffff05 1px, transparent 1px), linear-gradient(to bottom, #ffffff05 1px, transparent 1px)",
            }
        },
    },
    plugins: [],
};
export default config;

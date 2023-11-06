import { defineConfig, UserConfig } from 'vite'
import svgLoader from 'vite-svg-loader'
import glsl from "vite-plugin-glsl";

export default defineConfig({
  slidev: {
    vue: {
      template: {
        compilerOptions: {
          // treat all components starting with `my-lit` as custom elements
          isCustomElement: tag => tag.startsWith('shader-doodle'),
        },
      },
    },
  },
  plugins: [
    
    svgLoader(),
    glsl(),
    
  ],
} as UserConfig)
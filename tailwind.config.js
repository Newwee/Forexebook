export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#060911',
          900: '#0b0f19',
          850: '#0f172a',
          800: '#141e33',
          750: '#1a2744',
          700: '#203055',
          600: '#2d4373',
        },
        emerald: {
          450: '#10b981',
          550: '#059669',
          glow: 'rgba(16, 185, 129, 0.15)'
        }
      },
      fontFamily: {
        sans: ['Inter', 'Sarabun', 'system-ui', 'sans-serif'],
      },
      screens: {
        'xs': '420px',
        'ipad': '820px',
        'ipad-pro': '1024px',
        'tablet-landscape': '1180px',
      }
    },
  },
  plugins: [],
}

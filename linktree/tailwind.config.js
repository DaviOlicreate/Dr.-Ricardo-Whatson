/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        brand: {
          dark: '#0a0d0b',
          darker: '#050706',
          light: '#F8F9FA',
          gold: '#bda662',
          goldHover: '#a38d4f',
          wpp: '#25D366'
        }
      },
      fontFamily: {
        heading: ['Fraunces', 'serif'],
        body: ['Inter', 'sans-serif'],
      }
    }
  },
  plugins: [],
}

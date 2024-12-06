/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx}"],
  theme: {
    screens: {
      'small': {'max': '339px'},
      'mobile': {'min': '340px', 'max': '767px'},
      'tablet': {'min': '768px', 'max': '1023px'},
      'laptop': {'min': '1024px', 'max': '1279px'},
      'desktop': {'min': '1280px', 'max': '1535px'},
      'monitor': {'min': '1536px'},
    },
    extend: {},
  },
  plugins: [],
}
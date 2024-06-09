/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/**/*.js',
  ],
  theme: {
    extend: {},
  },
  corePlugins: {
    preflight: false,
  },
  plugins: [],
}


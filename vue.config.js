const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? '/storymous-migration/dist' : '/dist',
  outputDir: 'dist',
})

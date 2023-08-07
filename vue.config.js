const { defineConfig } = require('@vue/cli-service');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = defineConfig({
  publicPath: "/",
  outputDir: 'dist',
  configureWebpack: {
    plugins: [
      // Copy CNAME file to the build output directory
      new CopyPlugin({
        patterns: [
          {
            from: 'CNAME',
            to: '.',
            toType: 'dir'
          }
        ]
      })
    ]
  }
});

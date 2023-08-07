const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  publicPath: "/",
  outputDir: 'dist',
  chainWebpack: config => {
    config.plugin('copy').tap(([options]) => {
      options.push({
        from: 'CNAME',
        to: config.output.get('path'),
        toType: 'dir'
      });
      return [options];
    });
  }
})

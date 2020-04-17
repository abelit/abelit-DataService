process.env.VUE_APP_VERSION = require('./package.json').version

module.exports = {
  // config
  outputDir: 'dist',
  assetsDir: 'static', // For simple configuration of static files in Flask (the "static_folder='client/dist/static'" part in app.py)
  indexPath: 'ptraffic_index.html',
  devServer: {
    proxy: 'http://localhost:5000', // So that the client dev server can access your Flask routes
    // host: 'localhost',
    // port: 8080,

    // auto open browser
    open: true
  }
};
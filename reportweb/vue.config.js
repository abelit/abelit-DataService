process.env.VUE_APP_VERSION = require("./package.json").version;

module.exports = {
  // config
  outputDir: 'dist',
  assetsDir: "static", // For simple configuration of static files in Flask (the "static_folder='client/dist/static'" part in app.py)
  indexPath: 'report_index.html',
  devServer: {
    proxy: "http://58.42.231.98:5060", // So that the client dev server can access your Flask routes
    // host: 'localhost',
    // port: 8080,

    // auto open browser
    open: true
  }
};

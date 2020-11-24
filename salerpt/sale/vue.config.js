module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://58.42.231.98:5060',
          ws: true,
          changeOrigin: true
        },
        // '/foo': {
        //   target: '<other_url>'
        // }
      }
    }
  }
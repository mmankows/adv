const webpack = require('webpack');

module.exports = {
  devServer: {
    proxy: {
      "/": {
        target: "http://adv:8000",
      },
    },
  },
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
          'process.env.BACKEND_URL': JSON.stringify(process.env.BACKEND_URL),
      }),
    ]
  },
}


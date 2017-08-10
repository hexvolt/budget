const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const config = {
  context: __dirname,

  entry: './src/js/index', // entry point of app

  output: {
      path: path.resolve('./bundles/'),
      filename: "bundle.js"
  },

  module: {
    loaders: [
      // transform JSX into JS:
      {
        test: /\.jsx?$/,          // Match both .js and .jsx files
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          presets: ['react', 'es2015']
        }
      }
    ]
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],

  // where and which files look for
  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['*', '.js', '.jsx']
  }
};

module.exports = config;

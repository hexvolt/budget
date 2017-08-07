const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const config = {
  context: __dirname,

  entry: './src/js/index.js', // entry point of app

  output: {
      path: path.resolve('./bundles/'),
      filename: "[name]-[hash].js"
  },

  module: {
    loaders: [
      // transform JSX into JS:
      { test: /\.jsx?$/, exclude: /node_modules/, use: 'babel-loader'}
    ]
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],

  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['*', '.js', '.jsx']
  }
};

module.exports = config;

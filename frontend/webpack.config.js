const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const config = {
  context: __dirname,

  entry: './src', // entry point of app

  output: {
      path: path.resolve('./bundles/'),
      filename: "bundle.js"
  },

  module: {
    rules: [
      {
        test: /\.jsx?$/,          // Match both .js and .jsx files
        exclude: /node_modules/,
        use: [{
            loader: 'babel-loader',
            options: { presets: ['react', 'es2015'] }
        }],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
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

const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

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
        test: /\.less$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: "css-loader!less-loader",
        }),
      },
    ]
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin("styles.css"),
  ],

  // where and which files look for
  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['*', '.js', '.jsx']
  }
};

module.exports = config;

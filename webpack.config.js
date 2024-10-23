const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const WriteFilePlugin = require('write-file-webpack-plugin')

module.exports = {
    entry: './static/js/index.js',
    output: {
        path: path.resolve(__dirname, './static/assets'),
        filename: 'bundle.js',
        publicPath: '/static/assets/'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '../assets/styles.css',
        }),
        new WriteFilePlugin(),
    ],
    devServer: {
        static: {
            directory: path.join(__dirname, './static'),
        },
        compress: true,
        port: 9000,
        hot: false,
        devMiddleware: {
            writeToDisk: true,
        }
    },
};
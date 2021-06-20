module.exports = {
    env: {
        node: true,
        commonjs: true,
        es2021: true,
        jest: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended',
        'plugin:@typescript-eslint/recommended-requiring-type-checking',
        'airbnb-typescript/base',
        'plugin:prettier/recommended',
    ],
    parserOptions: {
        ecmaVersion: 12,
        sourceType: 'module',
        tsconfigRootDir: __dirname,
        project: './tsconfig.json',
    },
    parser: '@typescript-eslint/parser',
    plugins: ['@typescript-eslint'],
    rules: {
        camelcase: [
            2,
            {
                properties: 'always',
            },
        ],
        'max-len': [
            2,
            {
                code: 80,
            },
        ],
        'no-param-reassign': [2, { props: false }],
        'no-underscore-dangle': 'off',
        'max-classes-per-file': ['error', 2],
    },
};

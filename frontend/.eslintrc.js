module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/typescript/recommended",
    "@vue/prettier",
    "@vue/prettier/@typescript-eslint",
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "prettier/prettier": ["warn", {
      "tabWidth": 2,
      "useTabs": false,
      "semi": true,
      "trailingComma": "all",
      "singleQuote": false
    }, {
      "usePrettierrc": true
    }],
    "@typescript-eslint/no-empty-function": ["warn", {
      "allow": ["protected-constructors", "private-constructors"]
    }]
  },
};

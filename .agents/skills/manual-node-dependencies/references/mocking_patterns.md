# Dependency Mocking Patterns

When manually managing dependencies, you can often skip installing large or complex libraries if you only need a small subset of their functionality, or if the main package only uses them for optional features.

## 1. Empty Function Mock
Useful for utility libraries that are called but their return value is ignored or fits a simple pattern.

```javascript
// node_modules/some-lib/index.js
module.exports = function() {
    return {};
};
```

## 2. image-size Mock
If `pptxgenjs` or similar libraries require `image-size` but you aren't adding images to your slides, you can mock the dimension check.

```javascript
// node_modules/image-size/index.js
module.exports = function(path) {
    return { width: 100, height: 100, type: 'png' };
};
```

## 3. Logger Mock
For libraries that depend on a specific logging framework.

```javascript
// node_modules/winston/index.js
module.exports = {
    createLogger: () => ({
        info: console.log,
        error: console.error,
        warn: console.warn
    }),
    format: { combine: () => {}, timestamp: () => {}, json: () => {} },
    transports: { Console: class {} }
};
```

## 4. fs/path Polyfills
If a library written for the browser tries to access Node built-ins (unlikely in CJS, but possible in poorly bundled code), you can provide them:

```javascript
global.fs = require('fs');
global.path = require('path');
```

---
name: manual-node-dependencies
description: Fetch and manage Node.js dependencies manually from UNPKG when npm or cmd is restricted. Use when 'npm install' fails, Node modules are missing, or environment policies prevent standard package management.
---

# Manual Node Dependency Manager

This skill provides a workflow for manually installing Node.js packages by fetching them from UNPKG and organizing them into a `node_modules` structure that Node.js can recognize via `require()`.

## When to Use

1.  **Environment Restrictions**: `npm install` fails due to PowerShell ExecutionPolicy, missing `cmd.exe`, or firewall rules.
2.  **Broken Node Installation**: `npm` is missing or corrupted but `node.exe` is functional.
3.  **Ad-hoc Dependencies**: You need a specific library for a single script without modifying a global `package.json`.

## Core Workflow

### 1. Identify the Package and Entry Point
Identify the package name and version on [unpkg.com](https://unpkg.com). 
- Check the package's `package.json` on UNPKG (e.g., `https://unpkg.com/package@version/package.json`) to find the `main` or `exports.require` path.
- Standard paths are usually `dist/index.cjs` or `dist/package.bundle.js`.

### 2. Fetch the Package
Use the provided script to download the package into a local `node_modules` folder.

```powershell
& "path/to/skill/scripts/fetch_from_unpkg.ps1" -Package "pptxgenjs" -Type "cjs"
```

### 3. Handle Missing Peer Dependencies
Node.js will throw `MODULE_NOT_FOUND` if a package requires other libraries (like `jszip` or `image-size`).
- Fetch these dependencies manually into their own `node_modules` subfolders.
- If a package expects a global variable (e.g., `JSZip`), define it in your script before requiring the main package:
  ```javascript
  global.JSZip = require("jszip");
  const pptxgen = require("pptxgenjs");
  ```

### 4. Mocking Dependencies
If a dependency is large or hard to fetch but its functionality isn't needed for your specific task (e.g., `image-size` when not using images), you can mock it:

```powershell
New-Item -ItemType Directory -Path "node_modules/mock-pkg"
Set-Content -Path "node_modules/mock-pkg/index.js" -Value "module.exports = function() { return {}; };"
```

## Bundled Resources

- **scripts/fetch_from_unpkg.ps1**: Automates downloading and folder structure creation.
- **references/mocking_patterns.md**: Examples of common dependency mocks.

## Common Pitfalls

- **Bundle Issues**: Bundled versions (`.bundle.js`) often include dependencies but may export them in ways that confuse Node.js (e.g., returning JSZip instead of the main library). Prefer `cjs` versions.
- **Pathing**: Ensure you run your main script from the directory containing `node_modules`.

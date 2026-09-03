# 第 2 章：建立練習專案

```bash
mkdir opencode-lab && cd opencode-lab
git init
mkdir src tests
printf '# OpenCode Lab\n' > README.md
git add . && git commit -m 'Create practice project'
opencode run "說明這個練習專案，不要修改檔案"
```

請先確認 `git status`，並在乾淨專案中測試代理。

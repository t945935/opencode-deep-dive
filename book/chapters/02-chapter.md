<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 2 章　安裝、啟動與基本操作

安裝方式隨平台改變，先依官方安裝頁完成安裝，接著確認：

```bash
opencode --version
opencode --help
opencode providers
opencode models
```

在專案根目錄啟動 `opencode` 可進入互動式介面；`opencode run "任務"` 適合腳本或一次性任務。首次操作請選擇安全的小目標，例如「列出測試指令並解釋，不要執行」。確認模型、認證與工作目錄正確後，再允許讀檔、執行測試或修改檔案。

建立 `.gitignore`、乾淨的 Git 狀態與可執行測試，是使用代理前最有效的保護。代理不應取代版本控制；每次可接受的修改都應保留為可審查的 diff。

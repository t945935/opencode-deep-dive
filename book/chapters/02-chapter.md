<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 2 章　安裝、啟動與基本操作

## 本章目標

本章建立一個可重現、可還原的 OpenCode 工作環境，並完成第一次唯讀任務。所有後續實作都應從這種安全基線開始。

## 2.1 安裝前檢查

先確認作業系統、終端機、Git 與 Node.js（若目前版本的安裝方式需要）符合官方文件。OpenCode 的 CLI 會持續更新，因此不要只複製網路文章中的安裝指令；先查看官方安裝頁，再以版本指令確認結果：

```bash
opencode --version
opencode --help
```

在 Windows WSL2 中，請注意目前工作目錄與檔案權限；需要 GUI 時另行確認 WSLg 或使用 Windows 端介面。無論平台為何，都應在專案根目錄啟動，避免代理誤讀相鄰專案。

## 2.2 建立安全的練習專案

```bash
mkdir opencode-lab && cd opencode-lab
git init
printf '# OpenCode Lab\n' > README.md
mkdir src tests
printf 'def add(a, b):\n    return a + b\n' > src/math.py
git add . && git commit -m 'Create practice project'
```

真實專案則應先確認 `git status`，並把未提交的個人修改保存好。代理產生的差異必須可透過 Git 審查或還原。

## 2.3 互動與一次性執行

在專案根目錄執行 `opencode` 可啟動互動式介面；`opencode run "任務"` 適合腳本、教學與可重現的單次工作。第一次請使用唯讀任務：

```bash
opencode run "找出 add 函式，說明它目前缺少哪些測試；不要修改檔案"
```

接著自行檢查回應是否引用真實檔案，而不是只接受流暢文字。當任務需要修改時，先要求代理提出計畫，再逐項批准。

## 2.4 啟動失敗的排查順序

遇到錯誤時依序檢查：命令是否在 `PATH`、版本是否符合、目前目錄是否正確、Provider 是否已登入、模型是否可用、設定檔是否有語法錯誤。用 `opencode debug --help` 查看當前版本支援的除錯功能；不要直接刪除 Session 或設定檔來「碰運氣」修復。

## 章末練習

- 建立一個乾淨練習專案並提交初始版本。
- 執行一次唯讀探索，再執行一次只修改測試的任務。
- 用 `git diff` 比較代理操作前後的變更。

## 小結

可靠的代理工作始於正確的工作目錄、乾淨的版本控制與小型可驗證任務。安裝只完成一半；真正的基線是能重現、能審查、能還原。

<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 2 章　安裝、啟動與基本操作

## 本章目標

本章建立可重現、可還原的工作環境，完成第一次唯讀任務，並學會以版本、工作目錄、認證與設定檔的順序排查啟動問題。

## 2.1 安裝前檢查

OpenCode 的安裝方式依作業系統與版本而異，應先參考官方安裝頁，再驗證：

```bash
opencode --version
opencode --help
```

Windows WSL2 使用者還要確認目前是在 WSL 或 Windows 端、檔案是否位於預期的掛載路徑，以及是否需要 WSLg 顯示 GUI。不要把 Linux 家目錄、Windows 掛載目錄與專案路徑混為一談。

## 2.2 建立練習專案

```bash
mkdir opencode-lab && cd opencode-lab
git init
mkdir src tests
printf '# OpenCode Lab\n' > README.md
printf 'def add(a, b):\n    return a + b\n' > src/math.py
git add . && git commit -m 'Create practice project'
```

正式專案開始前，先執行 `git status --short`，把未提交的個人修改保存好。代理的每次修改都應能由 Git 審查或還原。

## 2.3 互動與一次性任務

在專案根目錄執行 `opencode` 可進入互動介面；`opencode run "任務"` 適合腳本與教學。第一次只做唯讀探索：

```bash
opencode run "找出 add 函式，提出三個測試案例；不要修改檔案"
```

之後自行檢查檔案、測試目錄與代理引用的路徑。只有在目標清楚且變更可還原時，才批准寫檔或執行測試。

## 2.4 啟動排查流程

遇到問題時依序檢查：

1. `command -v opencode` 是否找到正確執行檔。
2. `opencode --version` 是否符合書中技術基線。
3. `pwd` 是否為專案根目錄。
4. Provider 是否完成登入，模型是否在 `opencode models` 清單。
5. `opencode.json`／`.jsonc` 是否為合法 JSONC。
6. 是否有命令列或環境變數覆寫設定。

使用 `opencode debug --help` 查詢該版本支援的診斷功能。不要一遇到設定錯誤就刪除 Session；先保存錯誤訊息與目前檔案，才能重現問題。

## 2.5 安全基線

練習專案不放 API Key、客戶資料或生產憑證。為寫入任務建立 Git 分支，先讓代理列出預計修改檔案，再用 `git diff` 檢查。測試失敗時保留輸出，不要讓代理自行刪除測試來取得綠燈。

## 本章實作

進入 `examples/02-practice-project/`，建立練習專案並完成一次唯讀探索。把命令、版本與預期結果記入 README，讓另一位讀者能在相同目錄重做。

## 章末練習

- 在乾淨專案完成一次唯讀任務與一次測試任務。
- 故意從子目錄啟動，觀察設定與規則是否改變。
- 以 `git diff --check` 找出格式問題，並記錄修復方式。

## 小結

可重現的工作目錄、乾淨的 Git 狀態與小型任務，是使用代理的安全基線。安裝完成後，還要驗證版本、Provider、模型與設定是否真的生效。

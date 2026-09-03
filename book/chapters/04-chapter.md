<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 4 章　設定檔放哪裡

## 本章目標

本章解決初學者最常遇到的問題：設定檔究竟放在哪裡、哪一份會生效、LLM 選擇寫在哪裡，以及如何在不洩漏憑證的情況下共享專案設定。

## 4.1 先確認版本與工作目錄

設定鍵與搜尋規則可能隨 OpenCode 版本改變，因此不要直接套用未標示版本的網路文章。先執行：

```bash
pwd
opencode --version
opencode --help
```

工作目錄應是專案根目錄，也就是包含 `.git` 的目錄，而不是 `src/`、`dist/` 或暫存目錄。代理若在錯誤目錄啟動，可能讀不到 `AGENTS.md`，也可能把另一個專案當成目前工作範圍。

## 4.2 全域設定放哪裡

個人偏好通常放在使用者設定目錄。Linux 常見位置是：

```text
~/.config/opencode/opencode.json
~/.config/opencode/opencode.jsonc
```

Windows 與 macOS 的實際路徑可能不同，請以當前版本官方文件為準。全域設定適合放個人常用模型、顯示偏好或本機工具選項；不適合放團隊規則與秘密。

檢查檔案是否存在：

```bash
ls -la ~/.config/opencode/
```

## 4.3 專案設定放哪裡

可共享的設定放在：

```text
<專案根目錄>/opencode.json
<專案根目錄>/opencode.jsonc
```

例如：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "provider/model-name"
}
```

`provider/model-name` 是佔位值，必須替換成 `opencode models` 顯示且帳號可用的模型 ID。專案設定應只包含團隊可以共享的內容，不應包含 API Key、個人絕對路徑或客戶資料。

## 4.4 `AGENTS.md` 與 `.opencode/`

`AGENTS.md` 適合描述人類可讀的工作規則：測試命令、格式化工具、目錄責任、不可修改的檔案與完成定義。它不是權限邊界，因此不能取代工具層的批准與限制。

自訂 Agent、Command、Skill 與 Plugin 的目錄與檔名會依 OpenCode 版本及功能而異；使用前先查官方文件。把這類資源放在專案內的好處是可版本控制，但必須審查其 Prompt 與權限。

## 4.5 設定優先順序的排查方法

不同來源同時設定同一個欄位時，先不要猜哪份檔案優先。建立最小測試專案，只保留一個設定來源，記錄結果，再逐一加入全域設定、專案設定、命令列選項與環境變數。每次只改一項，才能知道真正的覆寫來源。

當模型不是預期選擇時，依序檢查：啟動目錄、專案設定、全域設定、`-m/--model` 命令列選項、Provider 認證與模型 ID。把版本、命令與結果寫入問題報告，比截取一段模糊錯誤更有用。

## 4.6 安全設定檢查

提交前執行：

```bash
git diff --check
git status --short
git grep -n -i -E 'api[_-]?key|token|secret|password' -- ':!*.lock' || true
```

最後一個命令只能做初步搜尋，不能取代秘密掃描工具。若 API Key 曾經提交，刪除檔案並不足夠，還必須撤銷並重新產生憑證。

## 本章實作

進入 `examples/04-config/`，複製範例設定到一個測試專案，加入 `AGENTS.md`，再以唯讀任務確認代理能看見規則。不要在正式專案第一次測試新的 Provider 或 Plugin。

## 章末練習

1. 分別建立全域與專案設定，記錄哪一個模型實際生效。
2. 寫一份 `AGENTS.md`，列出測試命令與禁止修改的路徑。
3. 故意輸入不存在的模型 ID，記錄錯誤並說明如何恢復。

## 小結

全域設定服務個人偏好，專案根目錄設定服務團隊共識，`AGENTS.md` 描述工作規則。設定問題應以最小實驗排查，憑證則永遠與可共享設定分離。

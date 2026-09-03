<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 4 章　設定檔放哪裡

## 本章目標

本章建立可追蹤的設定層次，說明全域設定、專案設定、`AGENTS.md` 與 `.opencode/` 的責任，並避免把機密資料提交到儲存庫。

## 4.1 先查版本，再查文件

設定鍵與搜尋順序可能隨 OpenCode 版本改變。本書範例以目前驗證版本為基線，但實作前仍應執行：

```bash
opencode --version
opencode --help
```

設定檔的 JSON Schema 可協助編輯器提示欄位與型別。不要因網路文章使用另一個版本，就假設所有欄位都仍可用。

## 4.2 全域與專案位置

個人預設通常放在使用者設定目錄，例如 Linux 的 `~/.config/opencode/opencode.json` 或 `.jsonc`；專案共用設定放在目前專案根目錄的 `opencode.json` 或 `opencode.jsonc`。專案根目錄是包含 `.git` 的目錄，而不是 `src/`、`dist/` 或任意目前子目錄。

`AGENTS.md` 用於人類可讀的規則：測試命令、格式化要求、不可觸碰的路徑與完成定義。`opencode.json` 則較適合機器可讀的模型、Provider 或功能設定。自訂 Agent、Command、Skill 與 Plugin 的具體目錄，務必依當前官方文件確認。

## 4.3 最小設定

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "provider/model-name"
}
```

`provider/model-name` 只是佔位值；使用 `opencode models` 查詢帳號實際可用的 ID。API Key 不應放進 JSON；把憑證管理與專案設定分開，才能安全提交設定檔。

## 4.4 設定衝突的排查

當實際模型或行為與預期不同，記錄：啟動所在目錄、使用的設定檔、命令列參數、環境變數與版本。一次只改一項，重新執行一個短任務，再比較結果。這種實驗式排查比同時修改多個檔案可靠。

## 章末練習

建立一份不含秘密的專案設定，加入 `AGENTS.md` 指定測試命令，並寫一個任務要求代理先讀規則再回答。將設定檔加入 Git，確認 `git diff` 沒有出現 Token。

## 小結

全域設定服務個人偏好，專案根目錄設定服務團隊共識，`AGENTS.md` 描述工作規則。清楚的放置位置與優先順序，是可重現代理行為的前提。

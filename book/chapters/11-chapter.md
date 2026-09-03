<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 11 章　MCP 外部工具整合

MCP（Model Context Protocol）讓 OpenCode 以標準協定連接外部工具與資料來源，例如 GitHub、文件搜尋、資料庫或內部服務。它適合把能力留在獨立服務，而非把供應商 SDK 寫入每個 Agent。

導入 MCP 前要檢查：伺服器來源、授權範圍、可讀寫資源、網路邊界、日誌是否含敏感資料，以及失敗時的行為。先以唯讀、單一服務與測試帳號開始。MCP 是能力介面，不會自動讓工具安全；權限與使用者確認仍不可省略。

# 第四部　Extension-First 設計

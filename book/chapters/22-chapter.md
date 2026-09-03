<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 22 章　OpenCode 的設計哲學

精簡核心的價值在於可替換：模型會改變、UI 會改變、工具與工作流程也會改變，但 Session、訊息、權限與事件邊界可以保持可理解。Extension-first 並非追求無限功能，而是讓每個能力有清楚的責任、依賴與失敗模式。

成功的代理系統不是讓模型獲得最多權限，而是讓人員能理解、檢查、停止、恢復與替換它。當模型能力持續進步，這些工程邊界會比任何單一模型名稱更持久。

# 附錄 A　常用指令速查

```bash
opencode --help
opencode providers
opencode models
opencode run "說明此專案的測試方式"
opencode --continue
opencode --session <session-id> --fork
opencode stats
opencode export <session-id>
opencode import <file>
opencode mcp --help
opencode agent --help
opencode debug --help
```

# 附錄 B　提交前檢查表

- [ ] 不含 API Key、Token、客戶資料或機密日誌。
- [ ] 已閱讀代理的 Git diff。
- [ ] 已執行相關測試，並記錄結果。
- [ ] 自訂 Tool 具備最小權限與錯誤處理。
- [ ] MCP 的來源、授權範圍與資料流已審查。
- [ ] 設定、模型 ID 與 OpenCode 版本已記錄。
- [ ] 讀者資源已更新：<https://github.com/t945935/opencode-deep-dive>。

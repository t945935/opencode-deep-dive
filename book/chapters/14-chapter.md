<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 14 章　實用擴充模式

常見擴充模式包括：自訂 Command 封裝固定工作、專用 Agent 設定角色與權限、Provider Adapter 接入內部模型閘道、事件 Hook 加入審計，以及 MCP Server 連接業務服務。先從一個痛點開始，例如「每次 PR 都要手動整理測試結果」，再決定它應是 Prompt、Skill、Tool、Plugin 還是 MCP。

選錯抽象層會增加維護成本。只改提示文字時不要寫 Plugin；需要受控副作用時不要只寫 Prompt；要與多種客戶端共用時，MCP 或 SDK 往往比 UI 專屬功能更合適。

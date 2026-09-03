<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 5 章　LLM Provider 與模型選擇

OpenCode 不是模型供應商。Provider 是提供模型與帳務的服務，模型 ID 則識別特定可用模型。先以 `opencode providers` 完成登入或憑證設定，再用 `opencode models [provider]` 查詢當前可用模型。模型可透過 `-m provider/model` 在單次啟動時覆寫，也可在設定檔指定預設值。

初學者只需選一個主力模型。一般程式開發可優先挑選能力平衡的 Claude Sonnet、OpenAI GPT 或 Gemini Pro 系列中，帳號可用且預算可接受者；不要把書中的示例 ID 當成永久名稱。選擇時看四件事：程式與工具使用品質、回應速度、長上下文成本、原始碼是否可傳送至該 Provider。

第二個模型的最佳用途是備援或審查，而不是隨機切換。可用較低成本模型處理摘要與小型整理，把跨模組重構、疑難除錯交給主力模型。Provider 暫時失敗時，保留 Session、記錄已執行工具與測試結果，再有意識地切換備援模型。

範例設定位於 [`resources/opencode.example.jsonc`](resources/opencode.example.jsonc)。其中的 `provider/model-name` 必須改為你的帳號實際可用 ID；API Key 不可放入此檔。

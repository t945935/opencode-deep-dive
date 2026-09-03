<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 5 章　LLM Provider 與模型選擇

## 本章目標

本章說明 Provider、Model 與 API 憑證的關係，提供初學者一至三個選擇，並建立可切換、可控成本且不洩漏機密的模型策略。

## 5.1 Provider 與 Model

Provider 是提供模型與帳務的服務；Model 是該服務中的具體版本。OpenCode 將兩者以 `provider/model` 形式識別。先用 `opencode providers` 管理登入或憑證，再用 `opencode models [provider]` 查詢目前帳號可用的模型。不要把書中的模型 ID 視為永久不變的名稱。

## 5.2 初學者三種選擇

- **Claude Sonnet 系列**：適合一般程式開發、重構、除錯與工具協作，作為單一主力模型通常容易開始。
- **OpenAI GPT 系列**：適合多用途開發、文件與既有服務整合；先選帳號實際可用的穩定版本。
- **Gemini Pro 系列**：適合長文件或大型程式庫探索；仍應以實際工具呼叫品質與費用測試為準。

初學者應先選一個主力模型，不要同時研究十個 Provider。第二個模型可用於備援或審查；低成本模型則適合摘要、格式整理與簡單文件工作。模型選擇必須同時考慮品質、速度、上下文成本與原始碼傳輸政策。

## 5.3 設定與單次切換

專案設定可使用：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "provider/model-name"
}
```

當次任務可用 CLI 覆寫：

```bash
opencode run -m provider/model-name "只分析測試失敗原因，不要修改檔案"
```

請將實際模型 ID 替換為 `opencode models` 顯示的值。模型選擇範例位於 [`examples/05-model-selection/`](../../examples/05-model-selection/)。

## 5.4 憑證與安全

API Key 不可寫進 `opencode.json`、Skill、Prompt 或 Git。使用 OpenCode 支援的 Provider 登入流程、環境變數或作業系統憑證管理。若專案含客戶程式碼，先確認公司的資料政策與 Provider 的保留政策；必要時採本機模型或遮蔽敏感資料。

## 5.5 Fallback 與評估

Provider 暫時失效時，先保留 Session 與已完成的測試結果，再切換備援模型。切換後不可假設輸出等價，重要修改仍須重新執行測試。可建立十個代表性任務，記錄成功率、耗時、Token、費用、工具錯誤與人工修正量，以資料而不是印象選模型。

## 章末練習

1. 用 `opencode models` 找出帳號可用模型，挑一個主力與一個備援。
2. 建立不含憑證的 `opencode.jsonc`，執行一次唯讀任務。
3. 比較兩個模型完成相同測試修正任務的時間、diff 大小與測試結果。

## 小結

模型是可替換的服務元件。初學者從一個穩定主力開始，以專案設定記錄策略，以 CLI 在單次任務切換，並用測試與成本資料驗證選擇。

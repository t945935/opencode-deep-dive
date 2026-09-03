<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 17 章　JSONL RPC

## 本章目標

本章以 JSON Lines 建立跨程序 Agent Client，處理請求、回覆、事件串流、逾時、取消與重連。

## 17.1 每行一個訊息

JSONL 的優點是簡單、可串流、容易由不同語言讀寫。Client 以 request ID 對應回覆；事件可以在回覆前後抵達，因此不能假設「一個請求只產生一行輸出」。每行都要驗證 JSON 結構，不能把未解析的文字直接當成命令執行。

## 17.2 可靠性

為請求設定逾時與取消訊號，區分網路失敗、Provider 錯誤、工具拒絕與輸入驗證錯誤。重連後不要盲目重送具有副作用的請求；若必須重試，使用冪等鍵或先查詢上一個 request ID 的狀態。

## 17.3 安全邊界

RPC Server 不應暴露本機任意路徑或無限制 Shell。每個連線要完成身分驗證、租戶隔離與權限判斷；錯誤回覆不應包含環境變數、完整 Prompt 或內部堆疊。

## 練習與小結

寫一個 Client 狀態機，涵蓋 Connected、Waiting、Streaming、Cancelled、Failed 與 Reconnecting，並為每種狀態設計可安全重試的規則。

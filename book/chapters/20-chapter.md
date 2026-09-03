<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 20 章　OpenCode 與主流工具比較

## 本章目標

本章不追逐短期模型排行榜，而從工作流、控制力、整合與治理需求選擇工具。

## 20.1 選擇面向

比較終端機或 IDE、Provider 彈性、Session 恢復、Tool／Skill／MCP 擴充、SDK／RPC、權限模型、隱私、成本與學習曲線。版本更新後應重新確認功能，不把本章視為永久規格表。

## 20.2 適用情境

OpenCode 適合偏好終端機、需要多 Provider、希望自訂工具與 MCP，或要把代理嵌入應用程式的人。Claude Code 與 Aider 也適合終端機工作流；Cursor、Windsurf 等 IDE 工具適合需要編輯器整合、補全與視覺操作的人；GitHub Copilot 適合深度使用 GitHub 生態的團隊。

## 20.3 不適用情境

若需求只有 IDE 補全，建立完整 Extension-first 平台可能過度複雜；若團隊沒有能力維護權限、Provider 與擴充版本，單純的託管工具可能更合適。工具不會消除人工審查、測試與資料治理的責任。

## 練習與小結

以你的團隊需求評分三個工具：工作流、整合、隱私、成本與維護。說明每個分數的證據，而不是只引用品牌印象。

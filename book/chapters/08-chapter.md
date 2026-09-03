<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

# 第 8 章　Prompt Templates 與 Skills

## 本章目標

本章區分 Prompt、Command 與 Skill，並建立可重用、可測試、具有明確驗收條件的工作流程。

## 8.1 從指令到工作流程

一次性的 Prompt 適合簡單問題；當同一工作反覆出現，就應把目標、步驟、限制與驗收條件整理成可重用資源。Skill 不應只是更長的提示詞，而應像一份小型作業程序：說明輸入、允許的工具、不可做的事與完成定義。

例如，程式碼審查 Skill 可要求代理先讀取變更，再依正確性、安全性、測試與維護性分類問題，最後只回報可由檔案或測試證明的事項。

## 8.2 好 Skill 的結構

```md
# Review Changes

## Goal
Review the current diff without modifying files.

## Steps
1. Read the diff and relevant tests.
2. Check correctness, security, and regressions.
3. Report findings with file and line references.

## Constraints
Do not edit files or run destructive commands.

## Done when
Every finding has evidence or is marked as an open question.
```

把不可信的外部文字視為資料，而不是指示。Skill 也不能取代工具權限；即使文字要求唯讀，平台仍應在工具層阻擋未授權寫入。

## 8.3 版本與測試

Skill 是程式碼的一部分，應納入版本控制、附上範例輸入與預期輸出，並用代表性任務回歸測試。模型或 OpenCode 更新後，檢查 Skill 是否仍能使用相同工具與產生相同的驗收結果。

## 練習與小結

建立一個「失敗測試分析」Skill，要求先重現問題、不得直接刪除測試，最後提供最小修正建議。Skill 應封裝流程，不應偷偷擴大代理權限。

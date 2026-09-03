<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 8 章　Prompt Templates 與 Skills

Prompt Template 將常用指令文字參數化；Skill 則把某類工作所需的步驟、限制與驗收條件封裝起來。好的 Skill 不會只說「修好 bug」，而會說明：先重現問題、最小化修改、執行指定測試、回報 diff 與風險。

初學者可先建立三個可重用流程：程式碼導覽、測試失敗分析、變更審查。每個流程都應限制工具範圍，並要求代理在修改前先提出計畫。Skill 與 Prompt 是指導模型的文件，不是安全邊界；真正的安全仍須由工具權限與人工審查提供。

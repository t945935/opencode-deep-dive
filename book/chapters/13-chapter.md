<!-- 正式稿章節；範例與勘誤見 https://github.com/t945935/opencode-deep-dive -->

## 第 13 章　Extension 架構

Extension-first 的意思不是「所有功能都做成外掛」，而是核心只保留穩定協調能力，領域功能透過明確 API 加入。這降低核心耦合，也讓團隊能替換 Provider、UI 或工具實作。

好的 Extension 有小而穩定的介面、清楚的設定、可測試的副作用與明確版本相容範圍。它不應依賴未公開的內部狀態。升級 OpenCode 前，先在測試專案驗證關鍵 Extension，並鎖定或記錄已驗證版本。

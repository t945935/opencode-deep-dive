# OpenCode 深入解析：讀者服務資料

本儲存庫是《OpenCode 深入解析：代理迴圈、工作階段、工具與擴充優先架構》的讀者資源。

- [書稿](BOOK.md)
- [第 5 章：模型選擇範例](examples/05-model-selection/)
- [最小設定檔範例](resources/opencode.example.jsonc)

## 使用方式

```bash
git clone https://github.com/t945935/opencode-deep-dive.git
cd opencode-deep-dive
opencode --version
opencode providers
opencode models
```

請依你的 OpenCode 版本與 Provider 帳號調整範例。模型 ID、設定欄位與可用功能會更新；以 [OpenCode 官方文件](https://opencode.ai/docs) 為準。

## 安全性

不要提交 `.env`、API Key、Token、私有程式碼、客戶資料或含機密的 Agent 日誌。範例中的 `provider/model-name` 是佔位值，並非可直接使用的模型 ID。

## 版本基線

本版書稿以 OpenCode `1.18.25` 為檢查基線。

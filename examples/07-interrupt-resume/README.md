# 第 7 章：中斷與恢復

1. 讓代理先提出修改計畫，不立即批准寫檔。
2. 中斷後檢查：

```bash
git status --short
git diff --stat
git diff
```

3. 目標不變時使用 `opencode --continue`；要試另一方案時使用指定 Session 加 `--fork`；需求改變時建立新 Session。

重試前先確認沒有部分寫入、背景程序或外部服務副作用。

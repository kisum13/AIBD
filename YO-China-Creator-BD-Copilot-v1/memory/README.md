# Memory 回复记忆库

这个目录用于沉淀真实达人问答，让 Codex 后续不仅能读“知识”，还能学习你的 BD 回复风格和决策方式。

## 文件说明

- `reply_memory.jsonl`：核心语料库，每一行是一条真实或标准化问答。
- `memory_schema.json`：语料字段说明。
- `memory_rules.md`：如何新增、清洗、维护语料。
- `weekly_update_template.md`：每周更新模板。

## 使用原则

每次你和达人沟通后，把有代表性的消息沉淀成：

```json
{
  "id": "pricing_hybrid_en_001",
  "language": "English",
  "intent": "hybrid_model",
  "stage": "pricing_discussion",
  "creator_message": "...",
  "best_reply": "...",
  "why_this_reply": "...",
  "next_step": "..."
}
```

以后 Codex 收到类似问题，就能优先检索这里的真实案例。

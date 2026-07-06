# Memory Usage Prompt for Codex

当你处理达人消息时，必须优先参考：

1. `memory/reply_memory.jsonl`
2. `knowledge/`
3. `agents/`
4. `templates/`

## 检索顺序

1. 先从 `memory/reply_memory.jsonl` 找相似案例。
2. 如果找到相似案例，模仿其回复结构和口吻。
3. 再用 `knowledge/` 校验项目事实和合同口径。
4. 如果没有相似案例，再走 `workflows/intent_router.md`。
5. 生成回复后，建议是否把本次对话新增到 memory。

## 输出格式

- 目标语言回复
- 中文翻译
- 匹配到的 memory id
- 建议新增/更新的知识库位置

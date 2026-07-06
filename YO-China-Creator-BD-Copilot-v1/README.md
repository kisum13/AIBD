# YO China Creator BD Copilot

面向 YourChannel / YO China 海外达人 AI 短剧项目的 Creator BD 智能体知识库。

目标：让 Codex / Custom GPT / 其他 Agent 能根据达人邮件或 WhatsApp 消息，自动判断语言、意图、合作阶段、风险点，并生成符合业务口径和 BD 风格的回复草稿。

## 核心链路

达人消息 → 识别语言/意图/阶段/情绪/风险 → 调用 agents/ → 读取 knowledge/ → 匹配 templates/ → 生成回复草稿 → 人工确认 → 通过聚星网站 skill/邮件/WhatsApp 发送

## 目录结构

- `CODEX.md`：给 Codex 的核心工作说明
- `agents/`：不同场景的智能体规则
- `knowledge/`：项目事实、合同口径、报价、分成、推广、内容流程
- `workflows/`：意图路由和回复决策流程
- `templates/`：多语言标准回复模板
- `prompts/`：Custom GPT / Codex 可用 Prompt
- `training_data/`：历史问答语料和数据结构
- `cases/`：平台案例和可对外提及案例
- `docs/`：上传、维护、Codex 连接说明
- `tools/`：后续脚本
- `config/`：可调参数

## 使用原则

1. 先生成草稿，不要自动发送，除非用户明确要求。
2. 不编造合同条款。
3. 收益只做潜力估算，不保证结果。
4. 固定费低时，避免伤害达人感受。
5. 高意向达人少推销，多推进。
6. 默认输出目标语言 + 中文翻译。

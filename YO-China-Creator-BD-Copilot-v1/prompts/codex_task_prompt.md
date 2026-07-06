# Codex Task Prompt Template

请根据本仓库知识，处理以下达人消息。

## 达人消息
{{creator_message}}

## 背景
- 语言：{{language_or_auto_detect}}
- 当前阶段：{{stage}}
- 预算 / 报价：{{budget}}
- 用户希望推进：{{goal}}
- 注意事项：{{notes}}

## 任务
1. 判断意图、阶段、风险。
2. 调用对应 agents 和 knowledge。
3. 生成目标语言回复。
4. 给出中文翻译。
5. 如果这条值得沉淀，建议写入哪个 training_data 或 template 文件。

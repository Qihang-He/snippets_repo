# Contributing（如何与 agent/仓库协作）

1. 报告问题或请求新模板
- 使用 Issue 或直接在对话中向 agent 提交任务，遵循 `AGENT_USAGE.md` 中的任务模板。

2. 提交变更
- agent 的变更应包含清晰的 commit message，并在 PR 描述中列出 acceptance 条件。

3. 审计与安全
- 对 third-party skills 需要 `security-review: true` 标注；agent 会先归档再执行审计。

4. 运行示例
- 请使用 `snippets/examples/requirements.txt` 创建虚拟环境并运行脚本。

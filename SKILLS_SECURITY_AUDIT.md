# Skills 初步安全审计（自动生成）

审计时间: 2026-08-28

已安装技能（来自 `INSTALLED_SKILLS.md` 与 `.agents/skills/` 目录）:

- `research-assistant-templates` — 本地模板（未发现远程来源）
- `python-performance-optimization` — 性能分析
- `python-testing-patterns` — 测试模式
- `python-design-patterns` — 设计模式
- `python-mcp-server-generator` — MCP 服务生成器
- `python-appservice-deploy` — 部署到 Azure App Service
- `dataverse-python-production-code` — Dataverse 相关
- `data-analysis-jupyter` — Jupyter 辅助（目录存在： `data-analysis-jupyter/`）
- `jupyter-notebook-writing` — 标注为 High Risk（目录存在： `jupyter-notebook-writing/`）
- `marimo-notebook` — 标注为 Medium Risk（目录存在： `marimo-notebook/`）

初步风险与建议:

- `jupyter-notebook-writing` (High Risk): 建议手动检查该 skill 的 `SKILL.md`、入口脚本与任何网络/远程执行逻辑。若包含自动安装、外部脚本下载或 socket/SSH 操作，应立即移除或隔离运行环境。操作建议：
  1) 在本地打开 `.agents/skills/jupyter-notebook-writing/`，检查 README 与主脚本。  
  2) 若存在不透明权限请求或执行远端代码，使用 git 删除该目录并更新 `INSTALLED_SKILLS.md`。

- `marimo-notebook` (Medium Risk): 建议审查权限要求与依赖安装脚本，确认不会在未经授权时修改系统或联网下载。若只提供本地 notebook helpers，风险较低。

- 其他 Python 生态技能（performance/testing/design 等）通常为文档/辅助代码，风险较低，但仍建议审阅 `SKILL.md` 以确认行为限定为“建议/生成代码”而非“执行/安装”。

下一步建议（我可以代为执行）:

1) 自动打开并汇总每个高/中风险 skill 的 `SKILL.md`（我可以生成摘要）。
2) 对 `jupyter-notebook-writing` 进行逐文件检查并列出潜在危险行（下载、执行命令、网络调用）。
3) 如需移除，删除 `.agents/skills/<skill>` 并更新 `INSTALLED_SKILLS.md`（我可代为执行并提交）。

注：此为初步自动化审计，最终决定请基于人工代码审查。若你授权，我将继续深入审查 `jupyter-notebook-writing`。

Actions taken (2026-08-28):

- 已将 `jupyter-notebook-writing` 从 `.agents/skills/` 移动并归档到 `.agents/skills_archives/jupyter-notebook-writing_20260828_223527`，以隔离该 skill 并保留其源文件供后续人工审查。
- 已更新 `INSTALLED_SKILLS.md`，将该 skill 标记为已归档并记录归档路径。

Actions taken (2026-08-28 → 2026-08-29):

- 已永久从仓库中删除 `.agents/skills_archives/jupyter-notebook-writing_20260828_223527`，变更已提交并推送。
- 已更新 `INSTALLED_SKILLS.md` 以反映删除状态。



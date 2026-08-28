# Agent 使用指南（快速指派模板）

目的：提高向 agent 布置任务的效率与一致性，减少来回确认。

1) 任务模板（必填字段）
- 标题（title）: 一行概述任务。
- 优先级（priority）: P0/高 / P1/中 / P2/低。
- 输出物（deliverable）: 明确可交付文件或操作（例如：新增文件路径、生成报告、提交 PR）。
- 接受标准（acceptance）：列出 2-4 条可验证准则。
- 约束（constraints）: 环境、依赖、不可做的事（如不联网、不要改主分支）。
- 资源（resources）: 相关文件路径或链接。

示例任务（创建数据分析示例的 PR）
```
title: 创建：数据分析示例与 README
priority: P1
deliverable:
  - snippets/examples/data_analysis_example.py
  - snippets/examples/README.md
acceptance:
  - 脚本可在干净 venv 中用 requirements.txt 安装后运行（smoke run）。
  - 输出包含 group_summary.csv 和 boxplot.png。
constraints:
  - 不修改主分支 README 除非 PR 描述中说明。
resources:
  - snippets/examples/
```

2) 指令风格建议
- 使用简洁动词开头（创建/更新/移除/审计）。
- 提供最小示例输入或数据路径。
- 明确是否需要自动提交与推送。

3) 快速验收命令（本地）
```powershell
python snippets/examples/data_analysis_example.py
python snippets/examples/figure_example.py
python snippets/examples/latex_table_example.py
```

4) 当 agent 执行变更时要点
- agent 应更新 `TODO`（`manage_todo_list`）以记录进度。
- 所有修改应有 commit 消息并 push。若修改影响 skills，应在 `INSTALLED_SKILLS.md` 记录。

5) 常见任务标签（可用于快速筛选）
- docs / chore / feat / fix / audit / example / ci

6) 若需人工审计（安全）
- 标注 `security-review: true` 并指定 `skills` 或路径，agent 应先归档（archive）再提交审计报告。

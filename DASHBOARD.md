# Repository Dashboard — snippets_repo

**最近本地测试**: 3 passed, 0 failed (运行命令: `python -m pytest -q`).

**关键 CI 工作流**:
- `Examples Smoke Tests` (.github/workflows/examples-smoke.yml): 在对 `snippets/examples/` 的变更时触发。
- `Examples Smoke Tests (Scheduled)` (.github/workflows/examples-cron.yml): 每日定时运行示例脚本。
- `Bandit Security Scan` (.github/workflows/bandit-scan.yml): 对 `.agents/skills/` 运行静态安全检查并上传 JSON 报告。

**最近变更摘要**:
- 新增：`tests/test_examples_smoke.py`（pytest smoke tests）。
- 新增：`.github/workflows/bandit-scan.yml`（Bandit 扫描）。
- 新增：`.github/workflows/examples-cron.yml`（定时 CI）。

**建议的下一步**:
- 将 Bandit 的 JSON 报告汇总到 `SKILLS_SECURITY_AUDIT.md`（自动化归档发现）。
- 将 `snippets/examples/requirements.txt` 中的 dev 依赖提取到根级 `requirements-dev.txt`（更清晰的依赖分层）。

**维护提示**:
- 当新增 third-party skills 时，请先在本地运行 `bandit -r .agents/skills -f json -o bandit-report.json` 并审阅报告。

生成时间: 2026-08-29

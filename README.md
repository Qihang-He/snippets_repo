# snippets_repo 备份仓库

该仓库包含你为科研工作构建的 prompts、snippets 与 skills 的本地备份副本。

主要内容：
- `prompts/` — VS Code 用户 prompts 模板
- `snippets/` — 完整/精简/微型 snippets
- `skills/` — 本地 user-level skill 草案与 eval scaffold

推送到远端（示例）：

1. 在 PowerShell 中设置远端并推送：

```powershell
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

2. 使用随仓库提供的脚本（Windows PowerShell）：

```powershell
.\push_to_remote.ps1 -RemoteUrl 'https://github.com/yourname/snippets_repo.git' -Branch 'main'
```

注意：如果远端已存在 `origin`，请先手动移除或使用脚本的 `-Force` 选项。

如果你愿意，我可以在你提供远端 URL 和授权后为你执行推送操作。
This repo stores VS Code prompts and snippets for quick reuse.

Included:
- prompts/README.md (user templates)
- snippets/research_templates.code-snippets
- snippets/research_short.code-snippets
- snippets/research_micro.code-snippets

Location: c:\Users\hqh\AppData\Roaming\Code\User

Note: This is a user-level repo for easy backup and sync.
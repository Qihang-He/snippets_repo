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

 
 Note: This is a user-level repo for easy backup and sync.

同步说明（将 prompts 同步到 VS Code 用户目录）:

1. 在本仓库根目录运行同步脚本（Windows PowerShell）：

```powershell
.\sync_prompts.ps1
```

2. 脚本会在 `%%APPDATA%%\Code\User\prompts` 下创建一个时间戳备份（如 `prompts_backup_YYYYMMDD_HHMMSS`），然后复制 `prompts/` 下的文件到用户 prompts 目录。请在运行前确保 VS Code 未锁定目标文件。

3. 若想恢复备份，请手动将对应备份目录的文件复制回 `%%APPDATA%%\Code\User\prompts`。

安全提示：在运行第三方 skills 或未审查的脚本前，请先查看 `SKILLS_SECURITY_AUDIT.md` 中的审计建议。

Included:
- prompts/README.md (user templates)
- snippets/research_templates.code-snippets
- snippets/research_short.code-snippets
- snippets/research_micro.code-snippets

Location: c:\Users\hqh\AppData\Roaming\Code\User

Note: This is a user-level repo for easy backup and sync.
#!/usr/bin/env pwsh
<#
Sync prompts/ from this repository to the VS Code user prompts directory.
Creates a timestamped backup of the existing prompts directory before copying.

Usage: Run from repository root or double-click in Explorer (PowerShell).
#>

$source = Join-Path $PSScriptRoot 'prompts'
$dest = Join-Path $env:APPDATA 'Code\User\prompts'

if (-not (Test-Path $source)) {
    Write-Error "Source prompts directory not found: $source"
    exit 1
}

if (Test-Path $dest) {
    $ts = (Get-Date).ToString('yyyyMMdd_HHmmss')
    $backup = Join-Path (Split-Path $dest -Parent) "prompts_backup_$ts"
    Write-Output "Backing up existing prompts from $dest to $backup"
    Copy-Item -Path $dest -Destination $backup -Recurse -Force
}

Write-Output "Copying prompts from $source to $dest"
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path (Join-Path $source '*') -Destination $dest -Recurse -Force

Write-Output "Sync complete. Files copied:"
Get-ChildItem -Path $dest -Recurse | ForEach-Object { Write-Output " - $($_.FullName)" }

exit 0

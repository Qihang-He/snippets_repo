param(
    [Parameter(Mandatory=$true)][string]$RemoteUrl,
    [string]$Branch = 'main',
    [switch]$Force
)

function Exec([string]$cmd) {
    Write-Host "> $cmd"
    & cmd /c $cmd
    if ($LASTEXITCODE -ne 0) { throw "Command failed: $cmd" }
}

# Ensure git is available
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git not found in PATH. Install git and retry."
    exit 2
}

Push-Location -LiteralPath (Split-Path -Parent $MyInvocation.MyCommand.Path)
try {
    if ($Force -and (git remote get-url origin 2>$null)) {
        Exec "git remote remove origin"
    }

    if (-not (git rev-parse --is-inside-work-tree 2>$null)) {
        Write-Host "Initializing git repository..."
        Exec "git init"
    }

    if (-not (git remote get-url origin 2>$null)) {
        Exec "git remote add origin $RemoteUrl"
    } else {
        Exec "git remote set-url origin $RemoteUrl"
    }

    Exec "git add -A"
    Exec 'git commit -m "chore: backup prompts/snippets/skills"'
    Exec "git branch -M $Branch"
    Exec "git push -u origin $Branch"

    Write-Host "Push complete."
} finally {
    Pop-Location
}

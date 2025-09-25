# Alexander's Notebook 管理脚本
param(
    [string]$Command = "serve",
    [string]$Message = ""
)

$ErrorActionPreference = "Stop"

Write-Host "📝 Alexander's Notebook 管理工具" -ForegroundColor Cyan
Write-Host "=" * 40 -ForegroundColor Gray

try {
    switch ($Command.ToLower()) {
        "install" {
            Write-Host "📦 安装依赖..." -ForegroundColor Yellow
            pip install -r requirements.txt
        }
        "scan" {
            Write-Host "🔍 扫描文件并更新导航..." -ForegroundColor Yellow
            python manage.py scan
        }
        "clean" {
            Write-Host "🧹 清理构建文件..." -ForegroundColor Yellow
            python manage.py clean
        }
        "serve" {
            Write-Host "🚀 启动开发服务器..." -ForegroundColor Yellow
            if (-not (Get-Command mkdocs -ErrorAction SilentlyContinue)) {
                Write-Host "📦 检测到 MkDocs 未安装，正在安装..." -ForegroundColor Yellow
                pip install -r requirements.txt
            }
            python manage.py scan
            mkdocs serve
        }
        "build" {
            Write-Host "🏗️ 构建网站..." -ForegroundColor Yellow
            python manage.py all
        }
        "commit" {
            Write-Host "💾 提交更改..." -ForegroundColor Yellow
            if ($Message) {
                python manage.py commit $Message
            } else {
                python manage.py commit
            }
        }
        "push" {
            Write-Host "🚀 提交并推送..." -ForegroundColor Yellow
            if ($Message) {
                python manage.py push $Message
            } else {
                python manage.py push
            }
        }
        "deploy" {
            Write-Host "🌐 部署到 GitHub Pages..." -ForegroundColor Yellow
            python manage.py deploy
        }
        "all" {
            Write-Host "🔄 执行完整流程..." -ForegroundColor Yellow
            python manage.py scan
            python manage.py clean
            mkdocs build
            Write-Host "✅ 完整流程执行完成" -ForegroundColor Green
        }
        default {
            Write-Host @"
用法: .\start.ps1 [命令] [消息]

命令:
  install   安装依赖
  scan      扫描文件并更新导航
  clean     清理构建文件
  serve     启动开发服务器 (默认)
  build     构建网站
  commit    提交更改
  push      提交并推送更改
  deploy    部署到 GitHub Pages
  all       执行完整流程

示例:
  .\start.ps1
  .\start.ps1 push "添加新的笔记"
  .\start.ps1 build
"@ -ForegroundColor White
        }
    }
}
catch {
    Write-Host "❌ 执行失败: $_" -ForegroundColor Red
    exit 1
}

Write-Host "`n🎉 操作完成!" -ForegroundColor Green
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MkDocs 项目管理脚本
支持一键清理、更新导航、提交推送等操作
"""

import os
import sys
import yaml
import subprocess
from pathlib import Path
from datetime import datetime

class NotebookManager:
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.docs_dir = self.root_dir / "docs"
        self.config_file = self.root_dir / "mkdocs.yml"
    
    def scan_markdown_files(self):
        """扫描所有 Markdown 文件并生成导航结构"""
        nav_structure = []
        
        # 首页
        nav_structure.append({"首页": "index.md"})
        
        # 扫描主要分类
        categories = {
            "mathematics": "数学",
            "physics": "物理", 
            "programming": "编程",
            "tools": "工具"
        }
        
        for category_dir, category_name in categories.items():
            category_path = self.docs_dir / category_dir
            if category_path.exists():
                category_nav = self._build_category_nav(category_path, category_dir)
                if category_nav:
                    nav_structure.append({category_name: category_nav})
        
        # 关于页面
        if (self.docs_dir / "about.md").exists():
            nav_structure.append({"关于": "about.md"})
        
        return nav_structure
    
    def _build_category_nav(self, category_path, category_prefix):
        """构建分类导航"""
        nav_items = []
        
        # 添加分类概述页面
        index_file = category_path / "index.md"
        if index_file.exists():
            nav_items.append({"概述": f"{category_prefix}/index.md"})
        
        # 扫描子目录
        for subdir in sorted(category_path.iterdir()):
            if subdir.is_dir():
                subdir_nav = self._build_subdir_nav(subdir, f"{category_prefix}/{subdir.name}")
                if subdir_nav:
                    nav_items.append({subdir.name.replace('-', ' ').title(): subdir_nav})
        
        # 扫描当前目录的其他 md 文件
        for md_file in sorted(category_path.glob("*.md")):
            if md_file.name != "index.md":
                title = md_file.stem.replace('-', ' ').title()
                nav_items.append({title: f"{category_prefix}/{md_file.name}"})
        
        return nav_items
    
    def _build_subdir_nav(self, subdir_path, prefix):
        """构建子目录导航"""
        nav_items = []
        
        for md_file in sorted(subdir_path.glob("*.md")):
            title = md_file.stem.replace('-', ' ').title()
            nav_items.append({title: f"{prefix}/{md_file.name}"})
        
        return nav_items
    
    def update_navigation(self):
        """更新 mkdocs.yml 中的导航配置"""
        print("🔍 扫描 Markdown 文件...")
        new_nav = self.scan_markdown_files()
        
        print("📝 更新导航配置...")
        with open(self.config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        config['nav'] = new_nav
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True, indent=2)
        
        print("✅ 导航配置已更新")
    
    def clean_build(self):
        """清理构建文件"""
        print("🧹 清理构建文件...")
        build_dirs = ['site', '.cache']
        
        for build_dir in build_dirs:
            build_path = self.root_dir / build_dir
            if build_path.exists():
                import shutil
                shutil.rmtree(build_path)
                print(f"   删除: {build_dir}")
        
        print("✅ 构建文件已清理")
    
    def git_operations(self, message=None):
        """执行 Git 操作"""
        if not (self.root_dir / ".git").exists():
            print("🔧 初始化 Git 仓库...")
            subprocess.run(["git", "init"], cwd=self.root_dir)
            subprocess.run(["git", "branch", "-M", "main"], cwd=self.root_dir)
        
        print("📦 添加文件到 Git...")
        subprocess.run(["git", "add", "."], cwd=self.root_dir)
        
        if not message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"更新笔记内容 - {timestamp}"
        
        print(f"💾 提交更改: {message}")
        result = subprocess.run(["git", "commit", "-m", message], cwd=self.root_dir, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 更改已提交")
            
            # 检查是否有远程仓库
            result = subprocess.run(["git", "remote"], cwd=self.root_dir, capture_output=True, text=True)
            if result.stdout.strip():
                print("🚀 推送到远程仓库...")
                push_result = subprocess.run(["git", "push"], cwd=self.root_dir, capture_output=True, text=True)
                if push_result.returncode == 0:
                    print("✅ 推送成功")
                else:
                    print(f"❌ 推送失败: {push_result.stderr}")
            else:
                print("⚠️  未配置远程仓库，跳过推送")
        else:
            print(f"⚠️  无新更改需要提交")
    
    def serve(self):
        """启动开发服务器"""
        print("🚀 启动开发服务器...")
        subprocess.run(["mkdocs", "serve"], cwd=self.root_dir)
    
    def build(self):
        """构建静态网站"""
        print("🏗️  构建静态网站...")
        subprocess.run(["mkdocs", "build"], cwd=self.root_dir)
        print("✅ 构建完成")
    
    def deploy(self):
        """部署到 GitHub Pages"""
        print("🚀 部署到 GitHub Pages...")
        subprocess.run(["mkdocs", "gh-deploy", "--force"], cwd=self.root_dir)
        print("✅ 部署完成")

def main():
    manager = NotebookManager()
    
    if len(sys.argv) < 2:
        print("""
📝 Alexander's Notebook 管理工具

用法:
  python manage.py <命令> [选项]

命令:
  scan        扫描文件并更新导航
  clean       清理构建文件
  commit      提交更改 [消息]
  push        提交并推送更改 [消息]
  serve       启动开发服务器
  build       构建静态网站
  deploy      部署到 GitHub Pages
  all         执行完整流程 (scan + clean + build)

示例:
  python manage.py scan
  python manage.py push "添加新的数学笔记"
  python manage.py all
        """)
        return
    
    command = sys.argv[1]
    
    try:
        if command == "scan":
            manager.update_navigation()
        elif command == "clean":
            manager.clean_build()
        elif command == "commit":
            message = sys.argv[2] if len(sys.argv) > 2 else None
            manager.git_operations(message)
        elif command == "push":
            message = sys.argv[2] if len(sys.argv) > 2 else None
            manager.git_operations(message)
        elif command == "serve":
            manager.serve()
        elif command == "build":
            manager.build()
        elif command == "deploy":
            manager.deploy()
        elif command == "all":
            manager.update_navigation()
            manager.clean_build() 
            manager.build()
        else:
            print(f"❌ 未知命令: {command}")
            
    except KeyboardInterrupt:
        print("\n👋 操作已取消")
    except Exception as e:
        print(f"❌ 执行出错: {e}")

if __name__ == "__main__":
    main()
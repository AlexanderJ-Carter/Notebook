#!/bin/bash

# 安装 MkDocs 和依赖
pip install mkdocs-material pymdownx-extensions mkdocs-git-revision-date-localized-plugin

# 启动开发服务器
mkdocs serve
# Alexander's Notebook

[![Deploy Status](https://github.com/alexander-xin/notebook/workflows/Deploy%20MkDocs%20to%20Pages/badge.svg)](https://github.com/alexander-xin/notebook/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

基于 MkDocs Material 构建的个人学习笔记网站，记录数学、物理、编程等学科的学习心得。

🌐 **在线访问**: [notebook.alexander.xin](https://notebook.alexander.xin)

## 🌟 特性

- **📝 Markdown 支持**: 原生 Markdown 语法
- **🧮 数学公式**: MathJax 渲染 LaTeX 公式  
- **💻 代码高亮**: 多语言语法高亮
- **🌓 主题切换**: 浅色/暗色模式
- **🔍 全文搜索**: 快速内容检索
- **📱 响应式**: 完美移动端体验

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip

### 本地运行

1. 克隆项目
```bash
git clone https://github.com/alexander-xin/notebook.git
cd notebook
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动开发服务器
```bash
mkdocs serve
```

4. 访问 http://localhost:8000

### 构建静态文件

```bash
mkdocs build
```

## 📁 项目结构

```
notebook/
├── docs/                   # 文档源文件
│   ├── index.md           # 首页
│   ├── mathematics/       # 数学笔记
│   ├── physics/           # 物理笔记  
│   ├── programming/       # 编程笔记
│   ├── tools/             # 工具使用
│   ├── about.md           # 关于页面
│   └── javascripts/       # 自定义 JS
├── mkdocs.yml             # MkDocs 配置
├── requirements.txt       # Python 依赖
└── README.md             # 项目说明
```

## 🚀 部署

### GitHub Pages

1. 推送代码到 GitHub
2. 运行部署命令：
```bash
mkdocs gh-deploy
```

### Cloudflare Pages

1. 连接 GitHub 仓库
2. 构建命令：`mkdocs build`
3. 输出目录：`site`

## 📝 内容分组

### 📊 数学
- 高等数学：极限、导数、积分
- 线性代数：向量、矩阵、特征值
- 概率论：概率分布、随机变量

### 🔬 物理
- 经典力学：牛顿定律、能量动量
- 电磁学：电场磁场、电磁感应
- 量子力学：基本原理、薛定谔方程

### 💻 编程  
- Python：基础语法、数据结构、科学计算
- 算法：排序、图算法
- 机器学习：监督学习、深度学习

### 🛠️ 工具
- LaTeX：数学公式排版
- Git：版本控制
- VS Code：代码编辑器

## 🎨 自定义

### 修改主题色彩
编辑 `mkdocs.yml` 中的 `palette` 配置：

```yaml
theme:
  palette:
    primary: blue  # 主色调
    accent: blue   # 强调色
```

### 添加新页面
1. 在 `docs/` 目录创建 Markdown 文件
2. 在 `mkdocs.yml` 的 `nav` 部分添加导航

### 数学公式
使用 LaTeX 语法：
- 行内公式：`$E = mc^2$`  
- 块级公式：`$$\int_0^\infty e^{-x} dx = 1$$`

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可

MIT License

## 📬 联系

- GitHub: [@alexander-xin](https://github.com/alexander-xin)
- Email: alexander@example.com
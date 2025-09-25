# 📖 内容创作指南

## 🎯 文件组织结构

### 📁 目录结构
```
docs/
├── index.md                    # 首页
├── mathematics/               # 数学分组
│   ├── index.md              # 数学概述
│   ├── calculus/             # 微积分
│   ├── linear-algebra/       # 线性代数
│   └── probability/          # 概率论
├── physics/                  # 物理分组  
│   ├── index.md              # 物理概述
│   ├── mechanics/            # 力学
│   ├── electromagnetism/     # 电磁学
│   └── quantum/              # 量子力学
├── programming/              # 编程分组
│   ├── index.md              # 编程概述
│   ├── python/               # Python
│   ├── algorithms/           # 算法
│   └── machine-learning/     # 机器学习
└── tools/                    # 工具分组
    ├── index.md              # 工具概述
    └── [工具名].md           # 具体工具
```

## 📝 文件命名规范

### ✅ 正确命名
- `linear-algebra.md` - 使用小写字母和连字符
- `python-basics.md` - 清晰描述内容
- `quantum-mechanics.md` - 完整的英文单词

### ❌ 错误命名
- `Linear_Algebra.md` - 避免大写和下划线
- `py.md` - 名称过于简略
- `数学.md` - 避免使用中文文件名

## 📋 Markdown 格式规范

### 🔤 标题结构
```markdown
# 页面标题 (H1 - 每页只有一个)

## 主要章节 (H2)

### 子章节 (H3)

#### 小节 (H4)
```

### 🧮 数学公式
```markdown
<!-- 行内公式 -->
函数的导数定义为 $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$

<!-- 块级公式 -->
$$
\int_a^b f(x) dx = F(b) - F(a)
$$

<!-- 编号公式 -->
$$
E = mc^2 \tag{1}
$$
```

### 💻 代码规范
````markdown
```python
# Python 代码示例
def fibonacci(n):
    """计算斐波那契数列的第 n 项"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 使用示例
result = fibonacci(10)
print(f"第10项: {result}")
```
````

### 📊 表格格式
```markdown
| 物理常数 | 符号 | 数值 | 单位 |
|---------|------|------|------|
| 光速 | $c$ | $2.998 \times 10^8$ | m/s |
| 普朗克常数 | $h$ | $6.626 \times 10^{-34}$ | J⋅s |
```

### 💡 提示框
```markdown
!!! note "注意"
    这是一个注意事项

!!! tip "提示" 
    这是一个有用的提示

!!! warning "警告"
    这是一个警告信息

!!! example "示例"
    这是一个示例说明

!!! theorem "定理"
    这是数学定理的表述
```

## 🎨 内容写作建议

### 📖 结构化写作
1. **学习目标** - 明确本节要达成的目标
2. **基础概念** - 定义和基本原理
3. **详细内容** - 深入讲解和推导
4. **实例应用** - 具体例子和代码演示
5. **练习题目** - 巩固理解的习题
6. **总结要点** - 重点内容回顾

### 🔗 链接规范
```markdown
<!-- 内部链接 -->
参见 [线性代数基础](../linear-algebra/basics.md)

<!-- 外部链接 -->
更多信息请访问 [官方文档](https://example.com)

<!-- 图片引用 -->
![算法流程图](../images/algorithm-flowchart.png)
```

## 🛠️ 便捷操作指南

### 🚀 快速开始
```bash
# 1. 启动开发服务器
.\start.ps1 serve

# 2. 添加新内容后更新导航
.\start.ps1 scan

# 3. 提交并推送更改
.\start.ps1 push "添加新的学习笔记"
```

### 📝 添加新笔记流程

1. **创建文件**
   ```bash
   # 在对应分组目录下创建 .md 文件
   # 例如：docs/mathematics/topology/basic-concepts.md
   ```

2. **编写内容**
   - 按照上述格式规范编写
   - 使用合适的标题层级
   - 添加数学公式和代码示例

3. **更新导航**
   ```bash
   .\start.ps1 scan
   ```

4. **预览效果**
   ```bash
   .\start.ps1 serve
   # 访问 http://localhost:8000
   ```

5. **提交推送**
   ```bash
   .\start.ps1 push "描述你的更改"
   ```

### 🎯 批量操作
```bash
# 完整流程：扫描 + 清理 + 构建
.\start.ps1 all

# 部署到 GitHub Pages
.\start.ps1 deploy
```

## 📏 质量检查

### ✅ 发布前检查清单
- [ ] 文件命名符合规范
- [ ] 标题层级结构合理
- [ ] 数学公式显示正确
- [ ] 代码块有语言标识
- [ ] 链接可以正常访问
- [ ] 图片路径正确
- [ ] 内容逻辑清晰
- [ ] 无语法错误

### 🔍 常见问题
1. **公式不显示** - 检查 LaTeX 语法是否正确
2. **链接失效** - 确认文件路径和文件名
3. **导航未更新** - 运行 `.\start.ps1 scan` 
4. **样式异常** - 检查 Markdown 语法格式

---

💡 **提示**: 使用管理脚本可以大大简化日常操作，专注于内容创作即可！
# 编程

## 💻 概述

编程是实现想法的工具，是连接理论与实践的桥梁。在这个分组中，我记录了从基础语法到高级应用的编程知识。

## 🚀 学习模块

### 🐍 Python
Python 是一门简洁而强大的编程语言，广泛应用于科学计算、数据分析、人工智能等领域。

- [基础语法](python/basics.md) - Python 语言基础
- [数据结构](python/data-structures.md) - 列表、字典、集合等
- [科学计算](python/scientific-computing.md) - NumPy、Pandas、Matplotlib

### 🧠 算法
算法是解决问题的方法和步骤，是程序设计的核心。

- [排序算法](algorithms/sorting.md) - 各种排序方法的实现
- [图算法](algorithms/graph.md) - 图的遍历与最短路径

### 🤖 机器学习
机器学习是人工智能的重要分支，让计算机能够从数据中学习。

- [监督学习](machine-learning/supervised.md) - 分类与回归问题
- [深度学习](machine-learning/deep-learning.md) - 神经网络与深度模型

## 🛠️ 开发环境

### 推荐工具

- **编辑器**: VS Code, PyCharm
- **版本控制**: Git
- **包管理**: pip, conda
- **虚拟环境**: venv, conda

### 代码规范

```python
# Python 代码规范示例
def calculate_fibonacci(n: int) -> int:
    """
    计算斐波那契数列的第 n 项
    
    Args:
        n: 正整数，表示数列的项数
        
    Returns:
        第 n 项斐波那契数
        
    Raises:
        ValueError: 当 n 不是正整数时
    """
    if n <= 0:
        raise ValueError("n 必须是正整数")
    
    if n <= 2:
        return 1
    
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    
    return b
```

## 📈 学习路径

!!! tip "编程学习建议"
    1. **基础扎实**: 先掌握一门语言的基本语法
    2. **多练习**: 通过大量编程练习提高技能
    3. **读源码**: 阅读优秀项目的源代码
    4. **做项目**: 通过实际项目巩固知识
    5. **持续学习**: 关注新技术和最佳实践

## 🎯 项目实践

### 初级项目
- 计算器程序
- 文件管理工具
- 简单游戏（贪吃蛇、2048）

### 中级项目
- 网络爬虫
- 数据可视化应用
- Web 应用开发

### 高级项目
- 机器学习模型
- 分布式系统
- 开源贡献

---

!!! quote "编程智慧"
    > "程序是写给人读的，只是偶尔让计算机执行一下。" —— Donald Knuth
    
    > "过早的优化是万恶之源。" —— Donald Knuth
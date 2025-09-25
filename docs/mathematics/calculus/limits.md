# 极限与连续

## 🎯 学习目标

- 理解极限的定义和性质
- 掌握极限的计算方法
- 理解函数连续性的概念

## 📖 基本定义

### 函数极限

设函数 $f(x)$ 在点 $x_0$ 的某个去心邻域内有定义。如果存在常数 $A$，对于任意给定的正数 $\varepsilon$，都存在正数 $\delta$，使得当 $0 < |x - x_0| < \delta$ 时，有：

$$|f(x) - A| < \varepsilon$$

则称常数 $A$ 为函数 $f(x)$ 当 $x$ 趋向于 $x_0$ 时的极限，记作：

$$\lim_{x \to x_0} f(x) = A$$

### 数列极限

设 $\{a_n\}$ 为一数列，如果存在常数 $a$，对于任意给定的正数 $\varepsilon$，都存在正整数 $N$，使得当 $n > N$ 时，有：

$$|a_n - a| < \varepsilon$$

则称常数 $a$ 为数列 $\{a_n\}$ 的极限，记作：

$$\lim_{n \to \infty} a_n = a$$

## 🧮 极限性质

!!! theorem "极限的四则运算"
    设 $\lim_{x \to x_0} f(x) = A$，$\lim_{x \to x_0} g(x) = B$，则：
    
    1. $\lim_{x \to x_0} [f(x) + g(x)] = A + B$
    2. $\lim_{x \to x_0} [f(x) - g(x)] = A - B$
    3. $\lim_{x \to x_0} [f(x) \cdot g(x)] = A \cdot B$
    4. $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{A}{B}$ （当 $B \neq 0$ 时）

## 📐 重要极限

### 第一个重要极限

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

### 第二个重要极限

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$$

或者等价形式：

$$\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e$$

## 💻 Python 演示

```python
import numpy as np
import matplotlib.pyplot as plt

# 演示 sin(x)/x 的极限
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
x = x[x != 0]  # 去除 x=0 的点
y = np.sin(x) / x

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = \frac{\sin x}{x}$')
plt.axhline(y=1, color='r', linestyle='--', alpha=0.7, label='y = 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'函数 $f(x) = \frac{\sin x}{x}$ 的图像')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim([-0.5, 1.5])
plt.show()
```

## 🔍 连续性

### 定义

函数 $f(x)$ 在点 $x_0$ 处连续，当且仅当：

$$\lim_{x \to x_0} f(x) = f(x_0)$$

### 连续的条件

函数在一点连续需要满足三个条件：

1. $f(x_0)$ 有定义
2. $\lim_{x \to x_0} f(x)$ 存在
3. $\lim_{x \to x_0} f(x) = f(x_0)$

## 📝 练习题

!!! example "例题 1"
    计算 $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$
    
    **解答**：
    利用等价无穷小 $1 - \cos x \sim \frac{x^2}{2}$ （当 $x \to 0$ 时）
    
    $$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \lim_{x \to 0} \frac{\frac{x^2}{2}}{x^2} = \frac{1}{2}$$

!!! example "例题 2"
    判断函数 $f(x) = \begin{cases} x^2, & x \leq 1 \\ 2x-1, & x > 1 \end{cases}$ 在 $x = 1$ 处的连续性
    
    **解答**：
    - $f(1) = 1^2 = 1$
    - $\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} x^2 = 1$
    - $\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (2x-1) = 1$
    
    因为 $\lim_{x \to 1} f(x) = f(1) = 1$，所以函数在 $x = 1$ 处连续。

---

!!! tip "学习建议"
    - 多练习 $\varepsilon - \delta$ 语言的应用
    - 熟记常用的等价无穷小
    - 理解连续性与极限的关系
    - 通过图像理解极限的几何意义
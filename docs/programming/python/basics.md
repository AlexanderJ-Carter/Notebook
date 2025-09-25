# Python 基础语法

## 🎯 学习目标

- 掌握 Python 基本语法
- 理解 Python 数据类型
- 学会使用控制结构
- 掌握函数定义和使用

## 🔤 变量与数据类型

### 基本数据类型

```python
# 整数
age = 25
print(type(age))  # <class 'int'>

# 浮点数
pi = 3.14159
print(type(pi))   # <class 'float'>

# 字符串
name = "Alexander"
message = '欢迎学习 Python'
print(type(name)) # <class 'str'>

# 布尔值
is_student = True
is_working = False
print(type(is_student))  # <class 'bool'>
```

### 变量命名规则

!!! tip "命名约定"
    - 使用小写字母和下划线：`user_name`, `total_score`
    - 常量使用大写：`PI = 3.14159`, `MAX_SIZE = 100`
    - 类名使用驼峰命名：`StudentInfo`, `DataProcessor`

## 📊 数据结构

### 列表 (List)

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "hello", 3.14, True]

# 访问元素
print(fruits[0])    # 苹果
print(fruits[-1])   # 橙子

# 修改元素
fruits[1] = "葡萄"
print(fruits)       # ['苹果', '葡萄', '橙子']

# 添加元素
fruits.append("芒果")
fruits.insert(1, "草莓")

# 删除元素
fruits.remove("苹果")
deleted = fruits.pop()  # 删除并返回最后一个元素
```

### 字典 (Dictionary)

```python
# 创建字典
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grades": [85, 92, 78]
}

# 访问值
print(student["name"])          # 张三
print(student.get("age", 0))    # 20

# 修改和添加
student["age"] = 21
student["email"] = "zhangsan@example.com"

# 遍历字典
for key, value in student.items():
    print(f"{key}: {value}")
```

## 🔄 控制结构

### 条件语句

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"得分 {score}，等级 {grade}")
```

### 循环语句

```python
# for 循环
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢{fruit}")

# 使用 range
for i in range(1, 6):  # 1 到 5
    print(f"第 {i} 次循环")

# while 循环
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

# 列表推导式
squares = [x**2 for x in range(1, 11)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
```

## 🔧 函数

### 函数定义

```python
def greet(name, greeting="你好"):
    """
    问候函数
    
    Args:
        name (str): 姓名
        greeting (str): 问候语，默认为"你好"
    
    Returns:
        str: 问候消息
    """
    return f"{greeting}, {name}!"

# 使用函数
message1 = greet("Alice")
message2 = greet("Bob", "欢迎")
print(message1)  # 你好, Alice!
print(message2)  # 欢迎, Bob!
```

### 高阶函数

```python
# 函数作为参数
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
cubed = apply_operation(numbers, cube)

print(f"平方: {squared}")  # [1, 4, 9, 16, 25]
print(f"立方: {cubed}")    # [1, 8, 27, 64, 125]

# Lambda 函数
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"翻倍: {doubled}")  # [2, 4, 6, 8, 10]
```

## 📦 模块和包

```python
# 导入整个模块
import math
print(math.pi)      # 3.141592653589793
print(math.sqrt(16))  # 4.0

# 导入特定函数
from math import sin, cos, pi
print(sin(pi/2))    # 1.0

# 给模块起别名
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# 导入自定义模块
# from my_utils import helper_function
```

## 🔍 异常处理

```python
def safe_divide(a, b):
    """
    安全除法，处理除零异常
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误: 不能除以零")
        return None
    except TypeError:
        print("错误: 输入必须是数字")
        return None
    finally:
        print("除法操作完成")

# 测试
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 错误信息
print(safe_divide(10, "a")) # 错误信息
```

## 💻 实践练习

!!! example "练习 1: 计算器"
    编写一个简单的计算器程序：
    
    ```python
    def calculator():
        while True:
            print("\n简单计算器")
            print("1. 加法")
            print("2. 减法") 
            print("3. 乘法")
            print("4. 除法")
            print("5. 退出")
            
            choice = input("请选择操作 (1-5): ")
            
            if choice == '5':
                break
            
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("输入第一个数字: "))
                num2 = float(input("输入第二个数字: "))
                
                if choice == '1':
                    print(f"结果: {num1 + num2}")
                elif choice == '2':
                    print(f"结果: {num1 - num2}")
                elif choice == '3':
                    print(f"结果: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"结果: {num1 / num2}")
                    else:
                        print("错误: 不能除以零")
    
    # calculator()  # 取消注释运行
    ```

!!! example "练习 2: 学生成绩管理"
    创建一个学生成绩管理系统：
    
    ```python
    class Student:
        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
            self.grades = {}
        
        def add_grade(self, subject, score):
            self.grades[subject] = score
        
        def get_average(self):
            if not self.grades:
                return 0
            return sum(self.grades.values()) / len(self.grades)
        
        def __str__(self):
            avg = self.get_average()
            return f"学生: {self.name}, 学号: {self.student_id}, 平均分: {avg:.2f}"
    
    # 使用示例
    student = Student("张三", "2021001")
    student.add_grade("数学", 95)
    student.add_grade("物理", 88)
    student.add_grade("化学", 92)
    print(student)
    ```

---

!!! tip "学习建议"
    - 多动手练习，编写实际的程序
    - 阅读官方文档和优秀的开源代码
    - 使用 IDE 的调试功能理解程序执行过程
    - 参与编程社区，与他人交流学习心得
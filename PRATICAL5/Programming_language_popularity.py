import matplotlib.pyplot as plt

# 1. 创建字典存储编程语言及其使用比例
language_usage = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}

# 2. 绘制柱状图
plt.figure(figsize=(8, 5))  # 设置图表大小
plt.bar(language_usage.keys(), language_usage.values(), color=['blue', 'red', 'green', 'purple', 'orange'])

# 设置图表标题和标签
plt.xlabel("Programming Languages")
plt.ylabel("Percentage of Developers (%)")
plt.title("Popularity of Programming Languages (Feb 2024)")

# 显示具体数值
for i, v in enumerate(language_usage.values()):
    plt.text(i, v + 1, f"{v}%", ha='center', fontsize=10)

plt.ylim(0, 70)  # 设置 y 轴范围
plt.grid(axis='y', linestyle='--', alpha=0.6)  # 添加网格线
plt.show()  # 显示图表

# 3. 查询某种语言的使用率
query_language = "Python"  # <- 修改此变量以查询其他语言
if query_language in language_usage:
    print(f"The percentage of developers who use {query_language} is {language_usage[query_language]}%.")
else:
    print("Language not found in the dataset.")
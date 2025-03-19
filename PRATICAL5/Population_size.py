import matplotlib.pyplot as plt

# 1. 存储数据
uk_countries = {
    "England": 57.11,
    "Wales": 3.13,
    "Northern Ireland": 1.91,
    "Scotland": 5.45
}

china_provinces = {
    "Zhejiang": 65.77,
    "Fujian": 41.88,
    "Jiangxi": 45.28,
    "Anhui": 61.27,
    "Jiangsu": 85.15
}

# 2. 生成排序列表
sorted_uk = sorted(uk_countries.values())
sorted_china = sorted(china_provinces.values())

print("Sorted UK populations:", sorted_uk)
print("Sorted China populations:", sorted_china)

# 3. 绘制 UK 饼图
plt.figure(figsize=(12, 6))  # 设置画布大小
plt.subplot(1, 2, 1)  # 创建子图 (1行2列，第1个)
plt.pie(uk_countries.values(), labels=uk_countries.keys(), autopct='%1.1f%%',
        colors=["blue", "red", "green", "purple"], startangle=140, pctdistance=0.85)
plt.title("Population Distribution in UK Countries")
plt.gca().set_aspect("equal")  # 保持饼图圆形

# 4. 绘制浙江邻近省份的饼图
plt.subplot(1, 2, 2)  # 第2个子图
plt.pie(china_provinces.values(), labels=china_provinces.keys(), autopct='%1.1f%%',
        colors=["gold", "cyan", "magenta", "orange", "pink"], startangle=140, pctdistance=0.85)
plt.title("Population Distribution in Zhejiang-Neighbouring Provinces")
plt.gca().set_aspect("equal")  

# 5. 显示图表
plt.tight_layout()  # 自动调整子图布局
plt.show()

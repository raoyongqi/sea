import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 Excel 文件
file_path = 'path/to/your/excel_file.xlsx'  # 替换为您的文件路径
sheet_name = 'Sheet1'  # 替换为您要读取的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 假设您的数据在列 'AMT' 和 'AP' 中
x = df['AMT']  # 替换为您的 X 轴数据列名
y = df['AP']    # 替换为您的 Y 轴数据列名

# 创建绘图窗口，包含两个子图
fig = plt.figure(figsize=(6, 6))

# 定义绘图区域
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)

# 散点图
main_ax = fig.add_subplot(grid[1:4, 0:3])
main_ax.scatter(x, y, color='steelblue', alpha=0.6)
main_ax.set_xlabel('AMT (°C)')
main_ax.set_ylabel('AP (mm)')

# 顶部直方图
top_hist = fig.add_subplot(grid[0, 0:3], sharex=main_ax)
top_hist.hist(x, bins=15, color='steelblue', edgecolor='black')
top_hist.axis('off')  # 隐藏轴

# 右侧直方图
right_hist = fig.add_subplot(grid[1:4, 3], sharey=main_ax)
right_hist.hist(y, bins=15, orientation='horizontal', color='steelblue', edgecolor='black')
right_hist.axis('off')  # 隐藏轴

# 显示图形
plt.show()


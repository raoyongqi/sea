import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 Excel 文件
file_path = 'data/1_Alldata.xlsx'  # 替换为您的文件路径
sheet2_name = 'Plotdata'  # 第二个工作表名称
sheet1_name = 'Lacation'  # 第一个工作表名称

# 读取两个工作表LON


df1 = pd.read_excel(file_path, sheet_name=sheet1_name)  # 第一个工作表
df2 = pd.read_excel(file_path, sheet_name=sheet2_name)  # 第二个工作表

# 假设第一个工作表中有 'Site' 列，第二个工作表中有 'Site'、'MAT' 和 'MAP' 列
# 使用 merge() 函数根据 'Site' 列合并两个 DataFrame
df2 = df2[['Site', 'MAT', 'MAP']].drop_duplicates()
merged_df = pd.merge(df1, df2, left_on='Site', right_on='Site', how='left')

# 提取需要绘制的数据
x = merged_df['MAT']  # 替换为您的 X 轴数据列名
y = merged_df['MAP']  # 替换为您的 Y 轴数据列名

# 创建绘图窗口，包含两个子图
fig = plt.figure(figsize=(6, 6))

# 定义绘图区域
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)

# 散点图
main_ax = fig.add_subplot(grid[1:4, 0:3])
main_ax.scatter(x, y, color='steelblue', alpha=0.6)
main_ax.set_xlabel('MAT (°C)')
main_ax.set_ylabel('MAP (mm)')

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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 设置字体
plt.rcParams['font.family'] = 'Noto Sans CJK'

# 读取 Excel 文件
file_path = 'data/output_data.xlsx'  # 替换为你的文件路径
data = pd.read_excel(file_path)

# 将列名转换为小写
data.columns = data.columns.str.lower()

# 提取变量，使用小写列名
mat = data['mat']  # 使用小写
map = data['map']  # 使用小写
pl = data['pl']    # 使用小写

# 创建宽高比为 3:2 的图形
plt.figure(figsize=(15, 10))  # 15:10 = 3:2

# 绘制 MAT 对 PL 的多项式回归
plt.subplot(1, 2, 1)  # 一行两列的第一个子图
# 使用二次多项式拟合
coeffs_mat = np.polyfit(mat, pl, 2)  # 使用二次多项式
poly_eq_mat = np.poly1d(coeffs_mat)

# 绘制散点图
plt.scatter(mat, pl, color='blue', label='Data Points', alpha=0.5)

# 绘制拟合曲线
plt.plot(mat, poly_eq_mat(mat), color='red', label='Fitted Polynomial Line')

# 获取并绘制置信区间（此处为简单估计，实际应用中可能需要更复杂的计算）
plt.fill_between(mat, poly_eq_mat(mat) - 1, poly_eq_mat(mat) + 1, color='red', alpha=0.3, label='Approximate Confidence Interval')

plt.xlabel('MAT (Mean Annual Temperature)')
plt.ylabel('PL (Plant Disease Severity)')
plt.title('Polynomial Regression of MAT vs PL')
plt.legend()

# 绘制 MAP 对 PL 的多项式回归
plt.subplot(1, 2, 2)  # 一行两列的第二个子图
# 使用二次多项式拟合
coeffs_map = np.polyfit(map, pl, 2)  # 使用二次多项式
poly_eq_map = np.poly1d(coeffs_map)

# 绘制散点图
plt.scatter(map, pl, color='blue', label='Data Points', alpha=0.5)

# 绘制拟合曲线
plt.plot(map, poly_eq_map(map), color='red', label='Fitted Polynomial Line')

# 获取并绘制置信区间（此处为简单估计，实际应用中可能需要更复杂的计算）
plt.fill_between(map, poly_eq_map(map) - 1, poly_eq_map(map) + 1, color='red', alpha=0.3, label='Approximate Confidence Interval')

plt.xlabel('MAP (Mean Annual Precipitation)')
plt.ylabel('PL (Plant Disease Severity)')
plt.title('Polynomial Regression of MAP vs PL')
plt.legend()

# 调整子图之间的间距
plt.subplots_adjust(wspace=0.3)  # 增加水平间距

plt.tight_layout()
title ='Polynomial Regression of MAP vs PL'
# 设置标题
output_file_path = f'data/{title}.png'
plt.savefig(output_file_path, dpi=300, bbox_inches='tight')
plt.show()

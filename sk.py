import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# 示例数据（真实值和预测值）
true_k = np.random.uniform(0, 6, 300)  # 真实值
pred_k = true_k + np.random.normal(0, 0.5, 300)  # 模拟预测值带有误差

# 创建绘图区域
plt.figure(figsize=(6, 6))

# 绘制散点图和密度图
sns.kdeplot(x=true_k, y=pred_k, fill=True, cmap="coolwarm", thresh=0.05)
plt.scatter(true_k, pred_k, alpha=0.5, color="purple")

# 拟合曲线
model = LinearRegression()
model.fit(true_k.reshape(-1, 1), pred_k)
pred_line = model.predict(true_k.reshape(-1, 1))
plt.plot(true_k, pred_line, color='red', label="Fitted Line")

# 理想的 y=x 参考线
plt.plot([0, 6], [0, 6], 'k--', label="Ideal Line")

# 设置标签和标题
plt.xlabel('True_k')
plt.ylabel('Predict_k')
plt.title('LightGBM')

plt.xlim(0, 6)
plt.ylim(0, 6)

# 显示图例
plt.legend()

# 显示图像
plt.show()

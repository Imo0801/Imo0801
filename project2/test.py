import numpy as np

# サンプルデータの作成
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 行列の転置
transposed_data = np.transpose(data)
print("Transposed Data:\n", transposed_data)

# 行列の和
sum_data = np.sum(data)
print("Sum of all elements:", sum_data)

# 行列の平均
mean_data = np.mean(data)
print("Mean of all elements:", mean_data)

# 行列の標準偏差
std_dev_data = np.std(data)
print("Standard Deviation of all elements:", std_dev_data)
import numpy as np

# 计算布尔矩阵乘法
def multiply(a, b):
    # 确保矩阵维度匹配
    if a.shape[1] != b.shape[0]:
        raise ValueError("矩阵维度不匹配，无法相乘")
    
    # 布尔矩阵乘法：使用 AND 操作代替乘法，OR 操作代替加法
    rows_a, cols_a = a.shape
    cols_b = b.shape[1]
    
    # 初始化结果矩阵
    result = np.zeros((rows_a, cols_b), dtype=bool)
    
    # 执行布尔矩阵乘法
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                # 使用 OR 来累积 AND 的结果
                result[i][j] = result[i][j] or (a[i][k] and b[k][j])
    
    return result

if __name__ == '__main__':
    a = np.array([[True, False], [True, True]])
    b = np.array([[False, True], [False, False]])
    print(multiply(a, b))
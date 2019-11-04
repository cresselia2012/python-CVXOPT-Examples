from cvxopt import matrix, solvers

# min f(x) = 1/2 x^T Q x + p^T x

# 行列 Q とベクトル p を生成
Q = 2 * matrix( [ [2, 0.5], [0.5, 1] ] )
p = matrix( [1.0, 1.0] )

# 最適化スタート
sol = solvers.qp( Q, p )

# 結果を出力
print('ステータス = {}'.format(sol['status']))
print('最適値 = {}'.format(sol['primal objective']))
print('最適解:')
print(sol['x'])

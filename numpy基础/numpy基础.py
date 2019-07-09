import numpy as np
print(np.empty([2,2], dtype=int))

#创建与X一样的数组
X = np.array([[1,2,3], [4,5,6]], np.int32)
Y=np.empty_like(X)
print(Y)
#创建对角矩阵
print(np.eye(3))
print(np.identity(3))
#创建3*2的全为1的矩阵
print(np.ones([3,2],float))
#创建3*2的全为0的矩阵
print(np.zeros([3,2],float))
#创建与X shape一样的全为1的矩阵
x=np.arange(4,dtype=np.int64)
print(x)
print(np.ones_like(x))
#创建2*5的矩阵 填充6
print(np.full([2,5],6,dtype=np.uint))
print(np.ones([2,5],dtype=np.uint)*6)
#创建与x相同shape，填充6的数组
x=np.arange(4,dtype=np.int64)
print(x)
print(np.full_like(x,6))
print(np.ones_like(x)*6)

#创建【1,2,3】
print(np.array([1,2,3]))
#将列表转换为数组
x=[1,2]
print(x)
print(np.asarray(x))
#将数组转换为matrix
x=np.array([[1,2],[3,4]])
print(x)
print(np.asmatrix(x))
#转换数组类型为float
x=[1,2]
print(x)
print(np.asfarray(x))
print(np.asarray(x,float))
#将数组转为单个元素
x=np.array([30])
print(x)
print(np.asscalar(x))
#拷贝数组x，id不一样
x=np.array([1,2,3])
y=np.copy(x)
print(id(x),x)
print(id(y),y)
#创建数组of 2,4,6。。。100
print(np.arange(2,101,2))
#在3.和10.之间创建包含50个等距元素的一维数组
print(np.linspace(3.,10.,50))
#对数等距的50个一维数组
print(np.logspace(3.,10.,50))
#获取矩阵的对角元素,对角元素组成一维矩阵
x=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(x,np.diag(x))
#创建对角元素为1,2,3,4其余为0的矩阵
print(np.diagflat([1,2,3,4]))
#创建下三角矩阵
print(np.tri(3,4,-1))
#获取矩阵的上三角形
print(np.tril(np.arange(1,13).reshape(4,3),0))
#获取矩阵的上三角形
print(np.triu(np.arange(1,13).reshape(4,3),0))

#查看numpy版本
print(np.__version__)

x=np.ones([10,10,3])
out=np.reshape(x,[-1,150])
print(x)
print(out)
assert np.allclose(out,np.ones([10,10,3]).reshape([-1,150]))
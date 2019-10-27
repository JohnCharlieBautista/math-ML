
__author__ = 'Charlie Bautista'
x = [[4,3,2],
	[7,7,6],
	[7,8,9]]
y = [[5,4,2],
	[6,6,6],
	[7,8,9]]
res = [[0,0,0],
	   [0,0,0],
	   [0,0,0]]


for i in range(len(x)):
	
	for a in range(len(y)):

		for b in range(len(y)):
			res[i][b] += x[i][a] * y[a][b]
			
for result in res:
	print(result)


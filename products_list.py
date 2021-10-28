products = [] # 建立购物清单

while True:
	name = input("请输入商品名称： ")
	if name == 'q': # 如果使用者输入 q ，程序终止
		break
	price = input("请输入商品价格： ")
	products.append([name, price]) # 购物清单添加 [商品，价格] 的二级清单

total = 0 
product = []
for p in products:
	total += int(p[1])
	product.append(p[0])

print(f'本次购物购买了： {product}')	
print(f'本次购物总花费：{total}')

with open('products-list.csv', 'w', encoding='utf-8') as f:
	f.write('商品' + ',' + '价格' + '\n')
	for d in products:
		f.write(d[0] + ',' + d[1] + '\n')



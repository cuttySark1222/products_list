products = [] # 建立购物清单

while True:
	name = input("请输入商品名称： ")
	if name == 'q': # 如果使用者输入 q ，程序终止
		break
	price = input("请输入商品价格： ")
	products.append([name, int(price)]) # 购物清单添加 [商品，价格] 的二级清单

total = 0 
product = []
for p in products:
	total += p[1]
	product.append(p[0])

print(f'本次购物购买了： {product}')	
print(f'本次购物总花费：{total}')



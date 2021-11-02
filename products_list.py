import os

# 读取档案
def read_file(file_name):
    products = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 使用者输入
def user_input(products):
    while True:
        name = input("请输入商品名称： ")
        if name == 'q': # 如果使用者输入 q ，程序终止
            break
        price = input("请输入商品价格： ")
        products.append([name, price]) # 购物清单添加 [商品，价格] 的二级清单
    return products

# 打印商品，计算总价格
def cal_total(products):
    total = 0 
    product = []
    for p in products:
        total += int(p[1])
        product.append(p[0])
    print(f'本次购物购买了： {product}')    
    print(f'本次购物总花费：{total}')


# 写入档案
def write_to_file(file_name, products):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('商品' + ',' + '价格' + '\n')
        for d in products:
            f.write(d[0] + ',' + d[1] + '\n')

def main():
    file_name = 'products-list.csv'
    products = []
    if os.path.isfile(file_name):
        products = read_file(file_name)
        print(products)
    else:
        print('找不到档案...')
    products = user_input(products)
    cal_total(products)
    write_to_file(file_name, products)

if __name__ == '__main__':
    main()



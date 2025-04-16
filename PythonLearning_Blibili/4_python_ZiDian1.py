#python字典1

price = { "苹果" : 9, "李子" : 10 , "香蕉" : 6 , "榴莲" : 100 } #记住数据库存储用{}   #the first plan(price = dict(苹果=9, 李子=10, 香蕉=6, 榴莲=100)  )
print('今日水果价格：')                                                           #price=dict()
for fruit in price:                                                             #price['苹果']=9
    print('%s%d元/斤' %(fruit, price[fruit]))                                   #price['李子']=10
print("")                                                                       #price['香蕉']=6
n = int(input('请输入购买水果的种类数量：'))                                         #price['榴莲']=100}
sum_price = 0                                                        #这是个什么玩意儿
for i in range(0, n):
    fruit = input('请输入购买的水果%d的名称:' % (i + 1))                  #为什么是%(i+1)
    num = int(input('请输入购买的水果%d的数量(斤):' % (i + 1)))
    if fruit in price:                                                #防止因输入的水果名不在字典中而报错
        sum_price += price[fruit] * num
print('总价格为%d' % sum_price)
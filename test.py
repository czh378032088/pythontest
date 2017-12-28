from scrapy.cmdline import execute

b = 428575#int(input("请输入："))
a = []

for i in range(b + 1):
    if (i != 0) and (b % i == 0) :
        a.append(i)

print(a)

c = []

for data0 in a:
    if data0 <= 12 :
        for data1 in a:
            if data1 <= 31 :
                c.append([int(b / (data0 * data1)),data0,data1])
            else:
                continue
    else:
        break
print(c)

for item in c:
    if item[0] < 2017 :
        print('出生年月为：' + str(item[0]) + '年' +  str(item[1]) + '月' + str(item[2]) + '日')
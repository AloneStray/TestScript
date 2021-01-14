'''
jmeter参数化，从数据库下载出来的格式是csv  user,'room1','room2' (userid是一个单元格，room都子在一个单元格
需要转化成txt：user;"room1","room2"

'''
import csv
with open('jmeter_datas2020113.csv', 'r') as f:
    reader = csv.reader(f)
    rooms_str = ''
    for line in reader:
        userid = line[0]
        orignal_rooms = line[1].split(",")  # ['6001180456348819', '5912291153901275', '6001300735304611']
        # 怎么给列表中每个元素变成""?   对于空串可以思考成 0+任何数 还是等于任何数
        # 给列表每个元素加双引号
        rooms_str = ''
        for room in orignal_rooms:
            room = '"' + room + '"'
            rooms_str = rooms_str + room + ","
        result = userid + ";" + rooms_str[:-1]
        print(result)
        #要写成追加模式a+
        with open('jemter_data_results.txt', 'a+') as  f:
            f.write(result+'\n')
'''
错误总结：
1.读取csv
2.列表每个元素加双引号   .appen 外层会加单引号  
  空字符串解决，对于空串可以思考成 0+任何数 还是等于任何数
  利用空字符串实现单个元素拼接
3.文件写入要写成追加模式a
'''
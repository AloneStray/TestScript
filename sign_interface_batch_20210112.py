'''
批量读取txt，参数化接口

'''
import requests
import hashlib
import json

def sign_request_single(userid,rooms):
    url = "http://xxx/api/play/timespan"

    data = {"roomIds": rooms, "partnerId": 49752473, "userRole": 0, "userNumber": userid}

    salt = "s9NoLmx5RDbplR8RwlZqGlmqwp3QqnRb"
    params = (json.dumps(data) + salt).replace(" ", "").replace("\n", "")
    signstr = hashlib.md5(params.encode("utf-8")).hexdigest().upper()
    print(signstr)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "sign": signstr
    }

   # res = requests.post(url=url, headers=header,json=data)

# sign_request_single(userid,rooms)


#批量读取txt
with open(file="sign_interface_rooms.txt") as  f:
    for line in f.readlines():
        line = line.strip('\n')  #读取文件去除换行符

        # print(line.split(","))  #str.split("分隔符")  返回的是列表
        userid = str(line.split(",")[0])
        rooms = line.split(",")[1:]
        # print(userid,rooms)
        sign_request_single(userid,rooms)

'''
错误积累：
1.参数化思路（用txt或者excel）
定义好请求函数，打开文件读取每一行的同时循环函数

2.写代码的时候没考虑到，结果都有\n。line = line.strip('\n')  #读取文件去除换行符

3.line.strip("分隔符")  结果是列表 
'''

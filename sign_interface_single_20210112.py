'''
接口签名： 
在接口请求头加入自定义的sign规则

工作中遇到的接口签名规则：
签名算法：
MD5(json+salt).toUpperCase()    json是请求参数需要将json压缩成一行，去掉空格和换行，salt是定值
salt = "s9NoLmx5RDbplR8RwlZqGlmqwp3QqnRb"
1.请求参数与固定值按一定顺序组合成字符串
2.在将组合字符串md5加密
3.得到的结果在全部转换为大写

'''
import requests
import hashlib
import json

def sign_request_single():
    url = "http://xxx/api/play/timespan"

    data = {"roomIds": ["6003051154159140"], "partnerId": 49752473, "userRole": 0, "userNumber": "20420226"}

    salt = "s9NoLmx5RDbplR8RwlZqGlmqwp3QqnRb"
    params = (json.dumps(data) + salt).replace(" ", "").replace("\n", "")

    signstr = hashlib.md5(params.encode("utf-8")).hexdigest().upper()
    print(signstr)
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "sign": signstr
    }

    res = requests.post(url=url, headers=header,json=data)

sign_request_single()

'''
错误积累：
1.python中的字典:
data参数在Python里默认为字典；字典输出默认键值对间有空格;故借助josn.dumps转换为Json字符串后在去除空格
字典类型str()后，会变成单引号

2.json格式的数据必须是双引号

3.md5借助hashlib库实现，
需要三步:(1)创建md5对象 hashlib.md5()
         (2)准备好经过utf8编码的字符串str.encode("utf-8")放入上述括号里
         (3)用md5对象取出值.hexdigest()
         
'''

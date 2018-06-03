# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:08:18 2018

@author: lenovo
"""


import urllib.request as r
print("欢迎使用全球天气APP")
city_pinyin=input("请输入城市拼音:")
address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
import json
data=json.loads(info)
#print(data)

print("1.查看当前城市天气,2.查看其它城市天气，3.保存当前城市")
menno=input("请输入菜单：")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
    city_pinyin=input("请输入城市拼音:")
    address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
    info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    import json
    data=json.loads(info)
    
if menno=="3":
    print("3.保存当前城市")

tm=data["list"][0]["dt_txt"]
temp=data["list"][0]["main"]["temp"]
temp_max=data["list"][0]["main"]["temp_max"]
pressure=data["list"][0]["main"]["pressure"]
description=data["list"][0]["weather"][0]["description"]
print("今天是："+str(tm)+"\n"+"当前天气温度"+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description))

tm=data["list"][7]["dt_txt"]
temp=data["list"][7]["main"]["temp"]
temp_max=data["list"][7]["main"]["temp_max"]
pressure=data["list"][7]["main"]["pressure"]
description=data["list"][7]["weather"][0]["description"]
print("日期："+str(tm)+"\n"+"天气温度："+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description))

tm=data["list"][15]["dt_txt"]
temp=data["list"][15]["main"]["temp"]
temp_max=data["list"][15]["main"]["temp_max"]
pressure=data["list"][15]["main"]["pressure"]
description=data["list"][15]["weather"][0]["description"]
print("日期："+str(tm)+"\n"+"天气温度："+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description))

tm=data["list"][23]["dt_txt"]
temp=data["list"][23]["main"]["temp"]
temp_max=data["list"][23]["main"]["temp_max"]
pressure=data["list"][23]["main"]["pressure"]
description=data["list"][23]["weather"][0]["description"]
print("日期："+str(tm)+"\n"+"天气温度："+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description))


tm=data["list"][31]["dt_txt"]
temp=data["list"][31]["main"]["temp"]
temp_max=data["list"][31]["main"]["temp_max"]
pressure=data["list"][31]["main"]["pressure"]
description=data["list"][31]["weather"][0]["description"]
print("日期："+str(tm)+"\n"+"天气温度："+str(temp)+"\n"+"最大温度"+str(temp_max)+"\n"+"气压"+str(pressure)+"\n"+"天气情况"+str(description))



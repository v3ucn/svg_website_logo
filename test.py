# from fake_useragent import UserAgent
# import requests
# # ua=UserAgent()     # 网络获取
# # 本地获取
# ua = UserAgent(
#     path = r"./test.json"
# )  # 读取本地ua,避免ua报错
# #print(ua.random)
# headers = {}
# headers["User-Agent"] = ua.random

# response = requests.get("https://zoro.to/watch/attack-on-titan-112?ep=3303",
#                         headers=headers)
# print(response.content)

# with open(r'test.html', 'a', encoding='utf-8') as f:
#     results = response.text
#     f.write(results)

# import time
# import datetime


# def composeTime(time1):
#     time2 = datetime.datetime.strptime(time1, "%Y%m%d%H%M%S")
#     time3 = time.mktime(time2.timetuple())
#     time4 = int(time3)
#     return time4

# def getTime(seconds):
#     timeArray = time.localtime(seconds)
#     otherStyleTime = time.strftime("%Y%m%d%H%M", timeArray)
#     print(otherStyleTime)


# if __name__ == '__main__':
#     mytime = composeTime("20220403155921")
#     print(mytime)
#     getTime(mytime)

import random
from collections import Counter
c = Counter()
for _ in range(10000):
    c[100] += 1
print(c)
print(c.values())
print(max(c.values()))

# import math

# def p_from_c(c):

#     po, pb = 0, 0
#     sumN = 0
#     maxTries = math.ceil(1/c)

#     for n in range(maxTries):
#         po = min(1, c*n) * (1-pb)
#         pb = pb + po
#         sumN = sumN + n * po


#     return (1 / sumN)


# #print(p_from_c(0.3))

# def c_from_p(p):
#     cu = p
#     cl = 0.0
#     p1, p2 = 0, 1
#     while True:
#         cm = (cu + cl) / 2
#         p1 = p_from_c(cm)
#         if abs(p1 - p2) <= 0.000000001:
#             break

#         if p1>p:
#             cu = cm 
#         else: 
#             cl = cm
#         p2 = p1

#     return cm



# fail = 1

# print(c_from_p(0.20)*100*fail)

# fail = 2

# print(c_from_p(0.20)*100*fail)

# fail = 3

# print(c_from_p(0.20)*100*fail)



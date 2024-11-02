## kzi
## fb:Khánh Duy(kzi)
import datetime
import time
import random
colors = ['\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[38m', '\033[39m']
anniversary = datetime.date(2021, 3, 6)

while True:
    i = random.randint(0, 9)
    print(colors[i] + anniversary.strftime("%d--%m--%y") + ":ANH YÊU EM HOÀNG ANH", sep="")
    time.sleep(0.01)
    anniversary
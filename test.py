#coding=utf-8

### TEST PyQt5 ###
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Hello PyQt')
#     w.show()
#     sys.exit(app.exec_())

### TEST twstock ###
import twstock
# print(twstock.codes)
from pyplotz.pyplotz import PyplotZ
from pyplotz.pyplotz import plt
# import matplotlib.pyplot as plt
import pandas as pd

stock_2317 = twstock.Stock('2317')
stock_2317_2019 = stock_2317.fetch_from(2019,3)     # 獲取 2019 年 01 月至今日之股票資料
stock_2317_2019_pd = pd.DataFrame(stock_2317_2019)
stock_2317_2019_pd = stock_2317_2019_pd.set_index('date')

stock_4938 = twstock.Stock('4938')
stock_4938_2019 = stock_4938.fetch_from(2019,3)     # 獲取 2019 年 01 月至今日之股票資料
stock_4938_2019_pd = pd.DataFrame(stock_4938_2019)
stock_4938_2019_pd = stock_4938_2019_pd.set_index('date')

pltz = PyplotZ() # create an instance
pltz.enable_chinese()
fig = plt.figure(figsize=(10, 6))
pltz.plot(stock_2317_2019_pd.close, '-' , label='鴻海')
pltz.plot(stock_4938_2019_pd.close, '-' , label='和碩')
# pltz.plot(stock_2317_2019_pd.open, '-' , label='開盤價')
pltz.title('收盤價曲線',loc='right')
# loc->title的位置
pltz.xlabel('日期')
pltz.ylabel('收盤價')
plt.grid(True, axis='y')
pltz.legend()
fig.savefig('test.png')
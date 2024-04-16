from win11toast import toast
import ctypes
import time
m = 30*60    #30分钟
while True:
    time.sleep(m)
    toast('已使用电脑30分钟了,请让你的眼睛放松一下')

input()
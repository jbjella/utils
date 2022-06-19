# Improved version of 6502's answer at https://stackoverflow.com/questions/6169217/replace-console-output-in-python
# My version includes the percentage at the end of the bar instead of just a bar. As long as x is a float, it will work well.
# jbjella - 6/18/2022

import sys

def percentbar_start(title):
    global progress_x
    global percent
    percent = 0
    sys.stdout.write(title + ": [" + "-"*40 + "] ("+str(percent)+"%)"+ chr(8)*46)
    sys.stdout.flush()
    progress_x = 0

def percentbar_progress(x):
    global progress_x
    global percent
    percent = "{:.2f}".format(x)
    x = int(x * 40 // 100)
    sys.stdout.write("#"*(x - progress_x)+ "-"*(40-x) + "] (" + str(percent) + "%)" + chr(8)*(45-x+len(str(percent))))
    sys.stdout.flush()
    progress_x = x

def percentbar_end():
    sys.stdout.write("#"*(40 - progress_x) + "] ("+str(percent)+"%)\n")
    sys.stdout.flush()
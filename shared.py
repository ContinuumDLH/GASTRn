"""
Routines and variables shared among other files in this project
"""
import winsound as ws
import time
from pathlib import Path
import inspect

Click   = "ClickOn.wav"
debug   = False  # set True for debug use

def click ():
    # Sound a click
    ws.PlaySound(Click, ws.SND_ASYNC | ws.SND_FILENAME)

def log (message):
    # Write message to the log file
    global Log
    print (message, file=Log, flush=True)

def openLog():
    # Open a new log file. Rename old log files.
    # Keep 3 most recent log files
    global Log
    maxLog = 2       # 3 log files, 0 .. 2
    new = "logs/log{:n}.txt".format(maxLog)
    if Path(new).is_file ():
        Path(new).unlink ()  # delete oldest log file
    for nLog in range (maxLog-1, -1, -1):
        old = "logs/log{:n}.txt".format (nLog)
        if Path(old).is_file():
            Path(old).rename(new)   # rename to older number
        new = old
    Log = open("logs/log0.txt", "w")    # new log file
    log (time.asctime(time.localtime(time.time()))) # log start time

def logClose ():
    # Close the log file
    global Log
    log("end log")
    Log.close()

def putLineInfo(txt):
    # print a debug message with the line # and txt
    print(inspect.stack()[1][2], txt, flush=True)

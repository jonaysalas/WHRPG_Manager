from datetime import datetime

logName = "WHRPG_Log.txt"

def writeLog(msg):
    '''
    Function to print a message on the Log. The log will add the time mark
    :param msg: the message to add in the Log
    '''
    msg = msg.strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = "[{}]:\n{}\n\n".format(now, msg)
    file = open(logName, 'a')
    file.write(line)
    file.close()


def writeLogErr(msg):
    '''
    Function to print an error message on the Log. The log will add the time mark
    :param msg: the error message to add in the Log
    '''
    msg = msg.strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = "[{}]:\n######ERROR#####\n{}\n\n".format(now, msg)
    file = open(logName, 'a')
    file.write(line)
    file.close()

writeLogErr("ey\n\n")
from datetime import datetime

logName = "WHRPG_Log.txt"

def writeLog(msg):
    msg = msg.strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = "[{}]:\n{}\n\n".format(now, msg)
    file = open(logName, 'a')
    file.write(line)
    file.close()


def writeLogErr(msg):
    msg = msg.strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = "[{}]:\n######ERROR#####\n{}\n\n".format(now, msg)
    file = open(logName, 'a')
    file.write(line)
    file.close()

writeLogErr("ey\n\n")
import os
from datetime import datetime
import calendar
from prettytable import PrettyTable

current_datetime = datetime.utcfromtimestamp(int(calendar.timegm(datetime.utcnow().utctimetuple()))).strftime('%H:%M:%S %d-%m-%Y')

x66 = PrettyTable()
x66.field_names = ["date", "size", "filename", "runtime", "nickname"]
outfile = open('66tick.txt', 'w')
path = 'replay/66tick'
files = sorted(os.listdir(path))
outfile.write('[CYBERSHOKE] Surf Replays (Last Updated ' + current_datetime + ')\n\n')
for file in files:
    if os.stat(path + "/" + file).st_size == 0:
        continue
    ofile = open(path + "/" + file, "rb")
    byte = ofile.read(6)
    bruntime = ofile.read(byte[5])
    byte = ofile.read(1)
    bnickname = ofile.read(byte[0])
    ofile.close()
    runtime = str(bruntime, 'UTF-8')
    print(file)
    nickname = str(bnickname, 'UTF-8')
    x66.add_row([datetime.utcfromtimestamp(int(os.stat(path + "/" + file).st_mtime)).strftime('%H:%M:%S %d-%m-%Y'), str(os.stat(path + "/" + file).st_size), file, runtime, nickname])
outfile.write(str(x66))
outfile.close()

x85 = PrettyTable()
x85.field_names = ["date", "size", "filename", "runtime", "nickname"]
outfile = open('85tick.txt', 'w')
path = 'replay/85tick'
files = sorted(os.listdir(path))
outfile.write('[CYBERSHOKE] Surf Replays (Last Updated ' + current_datetime + ')\n\n')
for file in files:
    if os.stat(path + "/" + file).st_size == 0:
        continue
    ofile = open(path + "/" + file, "rb")
    byte = ofile.read(6)
    bruntime = ofile.read(byte[5])
    byte = ofile.read(1)
    bnickname = ofile.read(byte[0])
    ofile.close()
    runtime = str(bruntime, 'UTF-8')
    print(file)
    nickname = str(bnickname, 'UTF-8')
    x85.add_row([datetime.utcfromtimestamp(int(os.stat(path + "/" + file).st_mtime)).strftime('%H:%M:%S %d-%m-%Y'), str(os.stat(path + "/" + file).st_size), file, runtime, nickname])
outfile.write(str(x85))
outfile.close()

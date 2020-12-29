import subprocess
import platform
import os
import datetime as dt
import time
from array import *
# import winsound

# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second


#import sleep

def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:
        return False

result = array('b', [1, 2, 3, 4, 5, 6])
path_abs = os.path.dirname(os.path.abspath(__file__))
print(path_abs)

# log file

startup_csv_path = str(os.path.join(path_abs, 'results.csv'))
print(startup_csv_path)
with open(startup_csv_path, 'a') as fd:
    fd.write("dt_UDM_8888_1111")
    fd.write("\n")

winsound.Beep(frequency, duration)

all = 0 # 1 - Prints all result, else prints only on inet connection issues
n = 1
j = 1
s_UDM = 0
s_8 = 0
s_1 = 0

while n==1:
    i = 1
    if __name__ == '__main__':
        current_ip_address = ['192.168.1.1', '8.8.8.8', '1.1.1.1']
        time_ping = dt.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        for each in current_ip_address:
            result [i] = ping_ip(each)
            #if result [i]:
            #    print(f"{each} is available")
            #else:
            #    print(f"{each} is not available")
            #print(result[i])
            i = i +1
    s_UDM = s_UDM + result[1]
    s_8 = s_8 + result[2]
    s_1 = s_1 + result[3]
    output_string = (time_ping + " " + str(j)+ " " +
                     str(result[1]) + "_" + str(s_UDM) + "_" + str(round(100 * s_UDM / j, 1)) + " " +
                     str(result[2]) + "_" + str(s_8) + "_" + str(round(100*s_8/j, 1)) + " " +
                     str(result[3]) + "_" + str(s_1) + "_" + str(round(100*s_1/j, 1)))
    if all ==1:
        print(output_string)
    else:
        print(time_ping + " " + str(j))
        if result[2]==0 or result[3]==0:
            print(output_string)
            #winsound.Beep(frequency, duration)

    with open(startup_csv_path, 'a') as fd:
        fd.write(output_string)
        fd.write("\n")
    i=1
    j = j + 1
    time.sleep(1)
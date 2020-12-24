import subprocess
import platform
import os
import datetime as dt
import time
from array import *
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

n=1
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

    output_string = (time_ping + "_"+str(result[1])+"_"+str(result[2])+"_"+str(result[3]))
    print(output_string)
    with open(startup_csv_path, 'a') as fd:
        fd.write(output_string)
        fd.write("\n")
    i=1
    time.sleep(1)
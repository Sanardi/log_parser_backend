
import pandas as pd
import time

logfile = pd.read_table("input-file-10000.txt", delim_whitespace=True, header=None)


logfile.columns = ["Timestamp", "hostname1", "hostname2"]
#i have added a line to the sample logfile in the current Timestamp, so I can test the script, which will process ongoing logfiles and print the output once her hour.

logfile = logfile.append({"Timestamp" : int(time.time()), "hostname1" : "Felipe", "hostname2": "Marzia"}, ignore_index = True)

import time
import sys


def excercise2(logfile):

    output_time = int(time.time()) + 3600
    hostname = input("Please specify hostname: ")
    print(logfile)
    while True:
        output= {}
        logs_from_host = []
        logs_to_host = []
        if int(time.time()) == output_time:

            logs = logfile[logfile["Timestamp"] > (int(time.time()) - 3600)]
            logs = logfile[logfile["Timestamp"] < int(time.time())]
            print(logs)
            logs_from_host = logs[logs["hostname1"] == hostname]
            logs_to_host = logs[logs["hostname2"] == hostname]
            output["connections from specified host"] = logs_from_host["hostname2"].tolist()
            output["connections to specified host"] = logs_to_host["hostname1"].tolist()
            output["most_connections"]: mode(logs["hostname2"].mode(), logs["hostname1"].mode())


            stdoutOrigin=sys.stdout
            sys.stdout = open("hourly_log.txt", "w")
            print(output)
            sys.stdout.close()
            sys.stdout=stdoutOrigin

            return output

excercise2(logfile)

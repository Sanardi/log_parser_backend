
import pandas as pd

logfile = pd.read_table("input-file-10000.txt", delim_whitespace=True, header=None)


logfile.columns = ["Timestamp", "hostname1", "hostname2"]


def return_hostnames(logfile, init_datetime, end_datetime, hostname):
    

   
    logs = logfile[logfile["Timestamp"] > init_datetime]
    logs = logfile[logfile["Timestamp"] < end_datetime]
    logs_to_host = logs[logs["hostname2"] == hostname]
            
    return print(logs_to_host['hostname1'].tolist())


return_hostnames(logfile,1565647204351, 1565733592699, "Shealee")

import pandas as pd

logfile = pd.read_table("input-file-10000.txt", delim_whitespace=True, header=None)
#I a loading here into a Pandas Dataframe which is a fast way to parse through csv files.

logfile.columns = ["Timestamp", "hostname1", "hostname2"]
#renamed the columns just for easier code-reading

def return_hostnames(logfile, init_datetime, end_datetime, hostname):
    

    logs = logfile[logfile["Timestamp"] > init_datetime]
    logs = logfile[logfile["Timestamp"] < end_datetime]
    logs_to_host = logs[logs["hostname2"] == hostname]
            
    return print(logs_to_host['hostname1'].tolist())
    #return the list of those hosts which have connected to the given server in the given period

#this is a test:
return_hostnames(logfile,1565647204351, 1565733592699, "Shealee")
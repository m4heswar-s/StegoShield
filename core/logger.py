from datetime import datetime

#logs of active session
session_logs =[]

def logs(operation, target_file,status):
    current_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    #creating a log action
    entry ={
        "TIME": current_time,
        "OPERATION":operation,
        "FILE":target_file,
        "STATUS": status
    }
    session_logs.append(entry)

    with open("audit_log.txt","a") as f:
        f.write(f"[{current_time}] Operation: {operation} | File: {target_file} |\nStatus: {status}\n\n")
    print(f"[Audit Logged] {operation} on {target_file} at {current_time}")
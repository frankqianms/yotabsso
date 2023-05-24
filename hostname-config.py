import shutil
import os


with open("output.txt", 'r') as f:
    lines = f.readlines()
for line in lines:
    if line.find("PUBLIC_HOSTNAME:") != -1:
        hostname = line.split("PUBLIC_HOSTNAME:")[1].strip()
        break
with open("env/.env.local", 'r') as f:
    lines = f.readlines()
cnt=0
for line in lines:
    if cnt == 2:
        break
    if line.find("AAD_APP_CLIENT_ID=") != -1:
        client_id = line.split("AAD_APP_CLIENT_ID=")[1].strip()
        cnt+=1
    if line.find("TAB_APP_URI=") != -1:
        line_pos = lines.index(line)
        cnt+=1
lines.pop(0)
lines.insert(0, "PUBLIC_HOSTNAME=" + hostname + "\n")
lines.pop(line_pos)
lines.insert(line_pos, "TAB_APP_URI=api://" + hostname + "/" + client_id + "\n")
with open("env/.env.local", 'w') as f:
    f.writelines(lines)

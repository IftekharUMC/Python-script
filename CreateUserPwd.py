import csv
import secrets
import subprocess
from pathlib import Path

cwd = Path.cwd()
print(cwd)

with open("users_in.csv", "r") as file_input, open("users_out.csv", "w") as file_output:
 reader = csv.DictReader(file_input)
 writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames)
 writer.writeheader()

for user in reader:
 user["password"] = secrets.token_hex(8)
 useradd_cmd = ["/sbin/useradd", "-c", user["real_name"], "-m", "-G", "users", "-p", user["password"], user["username"]]
 subprocess.run(useradd_cmd, check=True)

writer.writerow(user)

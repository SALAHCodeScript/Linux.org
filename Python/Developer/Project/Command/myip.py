import os

output = '.out'
os.system(f"ipconfig | grep IPv4 > {output}")

content = []
for line in open(output, "r").readlines():
	content.append(line.strip().split(" "))
os.system(f"rm {output}")

ipaddress = content[0][-1]
print(ipaddress)

os.system(f"rm -f {output}")

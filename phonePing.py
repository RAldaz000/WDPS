import subprocess

# Ask user for file name and distance
fileName = input("Name of run: ")
dis = input("Distance: ")

# ping router with 180 pings at 2 pings/second
p = subprocess.Popen(["ping", "-c180", "-i", ".5", "-D", "google.com"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# read ping data and write into a csv file
output = p.stdout.read().decode('utf-8')
for line in output.splitlines():
    if "time=" in line:
        print(line)
        with open(fileName+'.csv','a',newline='') as f:
            f.write(+dis+","+ line.split(":")[0].split("]")[0][1:]+ line.split(":")[1]+'\n')
from subprocess import PIPE  #connect to input/output/error pipes
import os.path
import subprocess  # subprocess module allows us to create new processes
log=subprocess.run(["git", "log", "-1", "--pretty='%s'"],stdout=PIPE, stderr=PIPE)
log_readable=log.stdout.decode()
print(log_readable)
fname="version.txt"
if(os.path.isfile(fname)):
    s = open(fname, 'r').read()
    segments=s.split('.')
    print(len(segments))
    print(segments[0])
    print(s)
else:
    file = open("version.txt", "w")
    file.write("1.0.0")
    file.close()

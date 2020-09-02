import subprocess


process = subprocess.Popen(
    ['ls', '-at'], 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

stdout, stderr = process.communicate()
stdout, stderr

print(stdout)
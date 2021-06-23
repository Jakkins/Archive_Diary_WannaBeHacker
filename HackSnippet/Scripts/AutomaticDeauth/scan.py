import subprocess

# far partire il processo
# leggere l'output 1 volta

command = ["sudo", "airodump-ng", "wlp0s20f0u1"]

def scan():
    f = open("blah.txt", "w")
    subprocess.call(command)


'''
subprocess.call(command)
'''
'''

'''

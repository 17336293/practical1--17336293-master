'''
Created on 22 Jan 2017

@author: aonghus
'''
if __name__ == '__main__':
    main()

import platform
# noinspection PyUnresolvedReferences
import multiprocessing
# noinspection PyUnresolvedReferences
import socket
# noinspection PyUnresolvedReferences
import psutil

def main():
    #(a)
    #1. Name of Machine
    print("Name of Machine:", platform.machine())

    #2. Operating system name
    print("OS Name:", platform.system())

    #3. Operating System Version
    print("OS Version:", platform.version())

    #4. Number of CPU's
    print("Number of CPU's:", multiprocessing.cpu_count())

    #5 Amount of Memory

    # noinspection PyUnresolvedReferences
    ram = psutil.virtual_memory()
    print("Ram: ", "{:.2f}".format((ram.total)/(1024**3)),"GB")

    #6 IP address of machine
    # noinspection PyUnresolvedReferences
    import socket
    print("IP Address:", socket.gethostbyname(socket.gethostname()))
    return
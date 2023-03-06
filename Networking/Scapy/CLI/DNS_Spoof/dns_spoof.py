import scapy.all as scapy 
from threading import Thread
from time import sleep
from os import system
import  subprocess
###########################################
#DNS flush
system("ipcnfig /flushdns")
system("cls")
###########################################
#Emty list 
l=[]
dic={}
###########################################
#count the list 
def count_list(list_):
    for i in list_:
        count=0
        for j in range(len(list_)):
            if i==list_[j]:
                count+=1
                if count>1:
                    dic[i]=count
    print(dic)
###########################################
#Printing in sniff 
def print_(packet):
    if packet.haslayer(scapy.DNS):
        if packet.haslayer(scapy.DNSRR):
            name=packet[scapy.DNSRR].rrname
            try:
                name=name.decode("ascii")
            except:
                pass 
            l.append(name)
###########################################
#Printing
def thread_printing():
    while True:
        print("Data:-")
        count_list(l)
        sleep(5)
        subprocess.call("ipconfig /flushdns")
        system("cls")
t=Thread(target=thread_printing)
t.daemon=True
t.start()
try:
    scapy.sniff(prn=print_)
except:
    print("printing list")
    pass

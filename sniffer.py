from scapy.all import *
import mysql.connector
port = 0
t = AsyncSniffer()
def start_sniffer():
    t.start()
def stop_sniffer():
    t.stop()
def analysis_output():
    with open('analysis_output',w) as f:
	for results in t.results:
		f.write(results.time - t.results[0].time)
def database_output():
    macs = []
    IPaddrs = []
   # payloads = []
    packets = t.results;
    for packet in packets:
        macs.append((packet['Ether'].src))
        IPaddrs.append((packet['IP'].src))
       # payloads.append(packet['Raw'].load)
    macSQL = "INSERT INTO dos.mac(MAC_Address) VALUES (%s);"
    IPaddrSQL = "INSERT INTO dos.main(IP_Address) VALUES (%s);"
   # payloadSQL = "INSERT INTO content(content) VALUES(%s);"
    dos = mysql.connector.connect(host = "localhost",
                                 user = "root",
                                 database ="dos"
                                 )
    doscursor = dos.cursor()
    print(macs)
    doscursor.executemany(macSQL,macs)
    doscursor.executemany(IPaddrSQL,IPaddrs)
   # doscursor.executemany(payloadSQL,IPaddrs)
    dos.commit()
    


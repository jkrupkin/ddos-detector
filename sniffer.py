from scapy.all import *
port = 0
t = AsyncSniffer()
def start_sniffer():
    t.start()
def stop_sniffer():
    t.stop()
def analysis_output():
    wrpcap("analysis.pcap",t.results)
def database_output():
    pass
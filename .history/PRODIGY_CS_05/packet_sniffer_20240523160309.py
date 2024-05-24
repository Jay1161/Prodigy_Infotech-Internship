





from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
            print(f"Payload: {bytes(tcp_layer.payload)}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Packet: {ip_layer.src}:{udp_layer.sport} -> {ip_layer.dst}:{udp_layer.dport}")
            print(f"Payload: {bytes(udp_layer.payload)}")

def start_sniffing():
    print("Starting packet sniffing...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()

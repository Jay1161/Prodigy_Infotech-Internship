# from scapy.all import sniff
# from scapy.layers.inet import IP, TCP, UDP

# def packet_callback(packet):
#     if IP in packet:
#         ip_layer = packet[IP]
#         print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

#         if TCP in packet:
#             tcp_layer = packet[TCP]
#             print(f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
#             print(f"Payload: {bytes(tcp_layer.payload)}")

#         elif UDP in packet:
#             udp_layer = packet[UDP]
#             print(f"UDP Packet: {ip_layer.src}:{udp_layer.sport} -> {ip_layer.dst}:{udp_layer.dport}")
#             print(f"Payload: {bytes(udp_layer.payload)}")

# def start_sniffing():
#     print("Starting packet sniffing...")
#     sniff(prn=packet_callback, store=0)

# if __name__ == "__main__":
#     start_sniffing()







import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, AsyncSniffer
from scapy.layers.inet import IP, TCP, UDP

# Global variable to control the sniffing process
sniffer = None

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        info = f"IP Packet: {ip_layer.src} -> {ip_layer.dst}\n"

        if TCP in packet:
            tcp_layer = packet[TCP]
            info += f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}\n"
            info += f"Payload: {bytes(tcp_layer.payload)}\n"

        elif UDP in packet:
            udp_layer = packet[UDP]
            info += f"UDP Packet: {ip_layer.src}:{udp_layer.sport} -> {ip_layer.dst}:{udp_layer.dport}\n"
            info += f"Payload: {bytes(udp_layer.payload)}\n"

        display_packet(info)

def display_packet(info):
    packet_display.configure(state='normal')
    packet_display.insert(tk.END, info + "\n")
    packet_display.configure(state='disabled')
    packet_display.yview(tk.END)

def start_sniffing():
    global sniffer
    sniffer = AsyncSniffer(prn=packet_callback, store=0)
    sniffer.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_sniffing():
    global sniffer
    if sniffer:
        sniffer.stop()
        sniffer = None
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def create_gui():
    global packet_display, start_button, stop_button

    root = tk.Tk()
    root.title("Packet Sniffer")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    packet_display = scrolledtext.ScrolledText(main_frame, width=80, height=20, state='disabled')
    packet_display.pack()

    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame, text="Start Sniffing", command=start_sniffing)
    start_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(button_frame, text="Stop Sniffing", command=stop_sniffing, state=tk.DISABLED)
    stop_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


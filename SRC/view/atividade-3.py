import dpkt

def process_tcpdump_file(filename):
    with open(filename, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        
        for timestamp, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            print(eth.pprint(1))

        #     # Check if the packet is an IP packet
        #     if isinstance(eth.data, dpkt.ip.IP):
        #         ip = eth.data
                
                # # Extract source and destination IP addresses
                # src_ip = dpkt.utils.inet_to_str(ip.src)
                # dst_ip = dpkt.utils.inet_to_str(ip.dst)

                # print(f"Timestamp: {timestamp}, Source IP: {src_ip}, Destination IP: {dst_ip}")

# Usage
process_tcpdump_file("cap1.dump")

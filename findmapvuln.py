#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# lendo o xml e imprimindo serviços
def readXml():
    tree = ET.parse('nmap_results.xml')
    root = tree.getroot()

    for host in root.findall('host'):
        for port in host.findall("ports/port"):
            state = port.find("state")

            if state is not None and state.get("state") == "open":
                service = port.find("service")
                cpes = [c.text for c in service.findall("cpe")] if service is not None else []
                print(f"[*] Service: {service.get('name')}")
                print(f"[*] Product: {service.get('product')}")
                print(f"[*] Version: {service.get('version')}")
                print(f"[*] CPEs: {', '.join(cpes) if cpes else 'none'}")
                print("-" * 40)  # separador 


def main():
    readXml()

if __name__ == "__main__":
    main()

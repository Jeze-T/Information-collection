#!/usr/bin/python3
# -*- coding=utf-8 -*-
import nmap
def nmap_host_scan(net):
    nm=nmap.PortScanner()
    res_scan=nm.scan(hosts=net,arguments="-sn -PE -n")
    print("starting:"+res_scan["nmap"]["command_line"])
    host_list=[]
    for ip in res_scan["scan"]:
        try:
            if res_scan["scan"][ip]["status"]["state"]=="up":
                IP=res_scan["scan"][ip]["addresses"]["ipv4"]
                host_list.append(IP)
        except Exception:
            pass
    return host_list
def nmap_port_scan(host,port):
    nm=nmap.PortScanner()
    host_port_os = []
    for ip in host:
        res_scan=nm.scan(hosts=ip,ports=port,arguments=" -A -O")
        print("starting:" + res_scan["nmap"]["command_line"])
        for ip in res_scan["scan"]:
            host_dic = {ip: {"tcp_port": {}, "os": []}}
            try:
                for p in res_scan["scan"][ip]["tcp"]:
                    host_dic[ip]["tcp_port"][p]={}
                    host_dic[ip]["tcp_port"][p]["product"]=res_scan["scan"][ip]["tcp"][p]["product"]
                    host_dic[ip]["tcp_port"][p]["version"] = res_scan["scan"][ip]["tcp"][p]["version"]
                host_dic[ip]["os"].append(res_scan["scan"][ip]["osmatch"][0]["name"])
                host_port_os.append(host_dic)
            except Exception as e:
                print("Eorr:",e)
                pass
    return host_port_os
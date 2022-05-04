#!/usr/bin/python3
# -*- coding=utf-8 -*-
import re
from nmap_test import nmap_host_scan,nmap_port_scan
from pymsf import smb_test


def three(net):
    print("--------第一阶段 探测主机--------")
    #net=input("net/mask:")
    ip_up=nmap_host_scan(net)
    for i in ip_up:
        print(i + " is UP!")
    print("--------第二阶段 探测端口--------")
    host_port_os=nmap_port_scan(ip_up,"0-1024")
    print("各主机开放的TCP端口与操作系统如下：")
    for i in host_port_os:
        print(i)   


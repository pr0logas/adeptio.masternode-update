import os
import re
import sys
import platform
import subprocess

ADEPTIO_PATH = '/usr/bin/adeptio-cli'

    def check_adeptio_mn_ip(self):
        mn_ip = ''
        try:
            netaddr = subprocess.check_output(ADEPTIO_PATH + " masternode status 2> /dev/null | grep netaddr", shell=True)
            if "[" in netaddr and "]" in netaddr:
                ip = re.search('[(.*)]', netaddr)
                mn_ip = ip.group(1)
        except:
            pass
        try:
            netaddr = subprocess.check_output(ADEPTIO_PATH + " masternode status 2> /dev/null | grep netaddr", shell=True)
            if "[" in netaddr and "]" in netaddr:
                ip = re.search('[(.*)]', netaddr)
                mn_ip = ip.group(1)
        except:
            pass
        return mn_ip

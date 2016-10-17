'''
   Wrapper around IPMI for simple machine management
'''

import ipmi
import sys

class lom_ipmi():
    '''
      IPMI commands
    '''

    def check_power(self, power_arg):
        if power_arg in ["on", "off", "cycle"]:
            return True

    def check_ip(self, ip):
        try:
            if int(ip) > 0 and int(ip) < 254:
                return True
        except ValueError as ve:
            print (ve)

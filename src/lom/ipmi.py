'''
   Wrapper around IPMI for simple machine management
'''

class lom_ipmi():
    '''
      IPMI commands
    '''
    def __init__(self):
        self.interface = "ipmitools"
        self.intf_type = "lanplus"
        
       
    def _check_power(self, power_arg):
        '''
           Method to check if a correct power option has been given
        '''
        if power_arg in ["on", "off", "cycle"]:
            return True

    def _check_ip(self, ip):
        '''
           Method to check if an IP quad is valid
        '''
        try:
            if int(ip) > 0 and int(ip) < 254:
                return True
        except ValueError as ve:
            print (ve)

    def interface_type (self, intf_type="lanplus"):
        '''
           Set the interface type
        '''
        self.intf_type = intf_type
        return self

    def connection_auth(self, user, passwd):
        self.user = user
        self.passwd = passwd
        return self

    def command(self, cmd):
        if self._check_power(cmd):
            self.cmd = "chassis power " + cmd
        return self

    def host(self, ip):
        if self._check_ip(ip):
            self.ip = ip
        return self

    def run_command(self):
        try:
            p = subprocess.check_output(self.build_command())
        except CalledProcessError as cpe:
            print(cpe.cmd)
            print(cpe.output)

    def build_command(self):

        if not self.ip:
            raise Exception("IP not given")

        if not self.cmd:
            raise Exception("Command not given")

        return [self.interface, "-v", "-I", self.intf_type, "-H", self.ip,
                     "-U", self.user, "-P", self.passwd, self.cmd ]


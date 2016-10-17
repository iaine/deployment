'''
   Methods to find the ISO netboot file
'''

import os

class ISO():

    def find_netboot_dir(self, tftp_dir):
        '''
           Method to find if the netboot directory exists
        '''
        return os.path.isdir(tftp_dir)

    def make_netboot_dir(self, tftp_dir):
        '''
           Method to make the netboot directory
        '''
        return os.mkdir(tftp, 0755)

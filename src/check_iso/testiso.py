from nose.tools import ok_, eq_, assert_true

import os


def test_tftp_dir_doesnt_exist():
    iso = ISO()
    tftp_dir = iso.find_netboot_dir('tftp')
    assert_false(tftp_dir)

def test_make_tftp_dir():
    iso = ISO()
    tftp = 'tftp'
    iso.make_netboot_dir(tftp)
    tftp_dir = iso.find_netboot_dir(tftp)
    assert_true(tftp_dir)

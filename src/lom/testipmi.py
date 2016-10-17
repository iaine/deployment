from nose.tools import assert_true, assert_false

from ipmi import lom_ipmi

def test_arg_power_options():
    ipmi = lom_ipmi()
    assert_true(ipmi.check_power("on"),True)

def test_false_arg_power_options():
    ipmi = lom_ipmi()
    assert_false(ipmi.check_power("restart"),True)

def test_arg_ip_exists():
    ipmi = lom_ipmi()
    assert_true(ipmi.check_ip("5"),True)

def test_arg_ip_does_not_exist():
    ipmi = lom_ipmi()
    assert_false(ipmi.check_ip(""),True)

def test_arg_ip_not_too_long():
    ipmi = lom_ipmi()
    assert_false(ipmi.check_ip("12345"),True)

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_DEBIAN = 'shellcheck'
PACKAGE_EL = 'ShellCheck'
PACKAGE_BINARY = '/usr/bin/shellcheck'


def test_shellcheck_package_installed(host):
    """
    Tests if shellcheck/ShellCheck is installed.
    """
    assert host.package(PACKAGE_DEBIAN).is_installed or \
        host.package(PACKAGE_EL).is_installed


def test_serverspec_binary_exists(host):
    """
    Tests if shellcheck binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_serverspec_binary_file(host):
    """
    Tests if shellcheck binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_serverspec_binary_which(host):
    """
    Tests the output to confirm shellcheck's binary location.
    """
    assert host.check_output('which shellcheck') == PACKAGE_BINARY

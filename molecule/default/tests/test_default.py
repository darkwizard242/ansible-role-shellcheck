import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


SHELLCHECK_BINARY_PATH = '/usr/bin/shellcheck'
SHELLCHECK_DEBIAN_PACKAGE = 'shellcheck'
SHELLCHECK_EL_PACKAGE = 'ShellCheck'


def test_shellcheck_package_installed(host):
    host.package("SHELLCHECK_DEBIAN_PACKAGE").is_installed or \
      host.package("SHELLCHECK_EL_PACKAGE").is_installed


def test_shellcheck_binary_exists(host):
    host.file('SHELLCHECK_BINARY_PATH').exists


def test_shellcheck_binary_file(host):
    host.file('SHELLCHECK_DEBIAN_BINARY_PATH').is_file


def test_shellcheck_binary_whereis(host):
    host.check_output('whereis shellcheck') == SHELLCHECK_BINARY_PATH

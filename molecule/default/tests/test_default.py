import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_shellcheck_package_installed(host):
    assert host.package("shellcheck").is_installed or \
      host.package("ShellCheck").is_installed


def test_shellcheck_binary_exists(host):
    assert host.file('/usr/bin/shellcheck').exists


def test_shellcheck_binary_file(host):
    assert host.file('/usr/bin/shellcheck').is_file


def test_shellcheck_binary_which(host):
    assert host.check_output('which shellcheck') == '/usr/bin/shellcheck'

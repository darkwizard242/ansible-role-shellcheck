[![build-test](https://github.com/darkwizard242/ansible-role-shellcheck/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-shellcheck/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-shellcheck/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-shellcheck/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/shellcheck) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-shellcheck&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-shellcheck) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-shellcheck&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-shellcheck) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-shellcheck&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-shellcheck) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-shellcheck?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-shellcheck?color=orange&style=flat-square)

# Ansible Role: shellcheck

Role to install (_by default_) [shellcheck](https://github.com/koalaman/shellcheck) package or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
shellcheck_app_debian_package: shellcheck
shellcheck_app_el_package: ShellCheck
shellcheck_desired_state: present
```

### Variables table:

Variable                      | Description
----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
shellcheck_app_debian_package | Defines the app to install on Debian based systems i.e. **shellcheck**
shellcheck_app_el_package     | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **ShellCheck**
shellcheck_desired_state      | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **shellcheck** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.shellcheck
```

For customizing behavior of role (i.e. installation of latest **shellcheck** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.shellcheck
  vars:
    shellcheck_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **shellcheck** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.shellcheck
  vars:
    shellcheck_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-shellcheck/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).

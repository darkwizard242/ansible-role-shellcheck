[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-shellcheck.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-shellcheck) ![Ansible Role](https://img.shields.io/ansible/role/43080?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43080?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43080?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-shellcheck&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-shellcheck) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-shellcheck?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-shellcheck?color=orange&style=flat-square)

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

Variable                      | Value (default) | Description
----------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
shellcheck_app_debian_package | shellcheck      | Defines the app to install on Debian based systems i.e. **shellcheck**
shellcheck_app_el_package     | ShellCheck      | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **ShellCheck**
shellcheck_desired_state      | present         | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).

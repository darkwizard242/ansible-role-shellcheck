
Ansible Role: shellcheck
=========

Role to install (_by default_) `shellcheck` package  or uninstall (_if  passed as var_)  on **Ubuntu** and **CentOS** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
shellcheck_app_debian_package: shellcheck
shellcheck_app_el_package: ShellCheck
shellcheck_desired_state: present
```

Variable `shellcheck_app_debian_package`: Defines the app to install i.e. **shellcheck** on Debian based systems.

Variable `shellcheck_app_el_package`: Defines the app to install i.e. **ShellCheck** on EL based s
ystems.

Variable `shellcheck_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **shellcheck** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.shellcheck
```

For customizing behavior of role (i.e. installation of latest **shellcheck** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.shellcheck
      vars:
        shellcheck_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **shellcheck** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.shellcheck
      vars:
        shellcheck_desired_state: absent
```

License
-------

[MIT](https://github.com/darkwizard242/ansible-role-shellcheck/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).

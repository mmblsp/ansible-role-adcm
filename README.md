ADCM server
=========

[Arenadata docs](https://docs.arenadata.io/ru/ADH/current/get-started/online_install/adcm-install.html)

Requirements
------------

- Availability of Internet access

Role Variables
--------------

- adcm_interfaces: "0.0.0.0"
- adcm_host_port: 8000
- adcm_conteiner_port: 8000
- adcm_host_dir: '/opt/adcm'
- adcm_conteiner_dir: '/adcm/data'

Dependencies
------------

- [role docker](https://github.com/mmblsp/ansible-role-docker.git)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: adcm }

License
-------

Apache 2.0

Author Information
------------------

[VK](https://vk.com/mmblspace)

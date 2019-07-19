# Ansible Linux based Java role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-maven.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-maven.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-maven)

Ansible role used to install Maven on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://maven.apache.org/"><img width="250" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Maven_logo.svg/1280px-Maven_logo.svg.png" /></a>

# Supported Version

* Apache Maven 2.x/3.x

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Trusty/Xenial/Bionic
* Debian Jessie/Strech

# Depend On

* jetune.java

# Usage

* Install Role ``` ansible-galaxy install jetune.maven ```
* use in your playbook
```
---
- hosts: all

  roles:
   - role: jetune.java
     vars:
      from_repo: false
      implementation: OPENJDK
      v_major: 11
      v_minor: 0.1
      build: 13
      os: linux
      arch: x64
      checksum: sha256:7a6bb980b9c91c478421f865087ad2d69086a0583aeeb9e69204785e8e97dcfd
      alternative_priority: 300
      is_default: true

   - role: ansible-role-maven
     vars:
      v_major: 3
      v_minor: 6.1
      is_default: true


```

* You can install more than one Maven version

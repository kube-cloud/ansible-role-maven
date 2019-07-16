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
- hosts: all

  roles:
    - jetune.maven

  vars:
    
    # Configure jetune.java role
	__java_packages:

 	 # JDK packages to install from repo (Open JDK version 8, install alrenative with priority 100 )
 	 - from_repo: true
 	 v_major: 8
 	 alternative_priority: 100
 	 implementation: OPENJDK
 	
   # Configure jetune.maven role 
   __maven_packages:
    - v_major: 3
      v_minor: .6.1
      default: true

```

* You can install more than one Maven version

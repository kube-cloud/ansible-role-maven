import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_maven_installed(host):

    # Maven expected version
    maven_version = '3.6.1'

    # Maven Home Path
    maven_home_path = '/opt/maven/maven-{}'.format(maven_version)

    # Maven archive file
    maven_archive_path = '/tmp/maven-{}.tar.gz'.format(maven_version)

    # Maven Home Dirctory
    maven_home = host.file(maven_home_path)

    # Maven Downloaded file
    maven_archive = host.file(maven_archive_path)

    # Check that Maven Archive exists
    assert maven_archive.exists

    # Check that Maven Archive is File
    assert maven_archive.is_file

    # Check that Maven Home exists
    assert maven_home.exists

    # Check that Maven Home is Directory
    assert maven_home.is_directory

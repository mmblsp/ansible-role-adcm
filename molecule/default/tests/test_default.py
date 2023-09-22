"""Test ADCM server."""
import os
import time

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_adcm_value(host):
    """Test adcm storage."""
    fle = host.file('/opt/adcm')
    assert fle.is_directory


def test_adcm_service(host):
    """Test adcm service."""
    for _ in range(30):
        try:
            output = host.check_output('curl http://localhost:8000')
            break
        except AssertionError:
            time.sleep(1)
    assert host.socket('tcp://0.0.0.0:8000').is_listening
    assert 'Arenadata Cluster Manager' in output

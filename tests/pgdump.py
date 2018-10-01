import pytest
import subprocess

fron pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_call_pg_dump(mocker):
    """
    Utilize pgdump to interact with the databse
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

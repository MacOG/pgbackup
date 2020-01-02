import pytest
import subprocess

from pgbackup import pgdump

url = ""

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a resonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("PosgreSQL client missing"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

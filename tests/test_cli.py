import pytest
from pgbackup import cli

url = "postgres://macog:x8bR7tre@34.219.210.108:80/db_one"

def test_parser_without_driver():
    """
    Without a specified driver teh parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it receives a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver with a destination
    """
    parser = cli.create_parser()

args = parser.parse_args([url, "--driver", "local", "/some/path"])

assert args.driver == "local"
assert args.destination == "/some/path"

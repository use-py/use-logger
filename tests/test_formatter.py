import json

import pytest
from logging import LogRecord
from usepy_plugin_logger.formatters import JsonFormatter


@pytest.fixture
def json_formatter():
    return JsonFormatter()


def test_format(json_formatter):
    json_formatter.with_timestamp = True
    record = LogRecord(
        name="test_logger",
        level=20,
        pathname="/path/to/file.py",
        lineno=10,
        msg="Test message",
        args=None,
        exc_info=None
    )
    result = json.loads(json_formatter.format(record))
    assert result['levelname'] == "INFO"
    assert result['message'] == "Test message"
    assert json_formatter.with_timestamp == ('timestamp' in result.keys())


def test_get_extra_info(json_formatter):
    json_formatter.extra_ignore_keys.remove("pathname")
    record = LogRecord(
        name="test_logger",
        level=40,
        pathname="/path/to/file.py",
        lineno=40,
        msg="Test message",
        args=None,
        exc_info=None
    )
    result = json_formatter.get_extra_info(record)
    assert result == {'levelname': 'ERROR', 'pathname': '/path/to/file.py'}

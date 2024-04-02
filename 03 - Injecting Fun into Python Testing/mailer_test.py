from unittest.mock import MagicMock

import pytest
from mailer import Mailer


@pytest.fixture(name="smtp_server_mock")
def smtp_server():
    return MagicMock()


def test_mailer_send(smtp_server_mock):
    mailer = Mailer(smtp_server_mock)
    mailer.send("to@example.com", "Hello, pytest!")
    smtp_server_mock.sendmail.assert_called_once_with(
        "from@example.com", "to@example.com", "Hello, pytest!"
    )

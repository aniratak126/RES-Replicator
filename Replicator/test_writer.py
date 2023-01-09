import socket, unittest, unittest.mock
from unittest.mock import MagicMock
from unittest import mock
from writer import *

class TestWriter(unittest.TestCase):
    """def test_init(self):
        setup = Writer.__init__(self)
        self.assertIsNone(setup)"""

    @mock.patch('writer.socket')
    def test_send_data(self, mock_test_send_data):
        tw = Writer()
        mock_socket = MagicMock(socket.socket)
        mock_test_send_data.return_value = mock_socket
        tw.client_socket = mock_socket

        self.assertEqual(None, Writer.send_data(tw,1,10))

if __name__ == "__main__":
    unittest.main()
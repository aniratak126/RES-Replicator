import socket, unittest, unittest.mock
from unittest.mock import MagicMock
from unittest import mock
from replicator import *
from data import *

class TestReplicator(unittest.TestCase):
    @mock.patch('replicator.socket')
    def test_send_to_reader(parent, mock_test_send):
        rr = ReplicatorReceiver(parent)
        mock_socket = MagicMock(socket.socket)
        mock_test_send.return_value = mock_socket
        rr.client_socket = mock_socket

        podatak = Data(1,10,0)

        parent.assertEqual(None, ReplicatorReceiver.send_to_reader(rr,podatak))

if __name__ == "__main__":
    unittest.main()
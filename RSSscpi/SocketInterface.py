# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import socket


class SocketInterface(object):
    def __init__(self, ip_address):
        self.ip = ip_address
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(1)  # 1 second timeout
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0)  # Disable Nagle algorithm
        self._socket.connect((self.ip, 5025))

    def install_handler(self, *args):
        pass

    def enable_event(self, *args):
        pass

    @staticmethod
    def open_resource(ip_address):
        return SocketInterface(ip_address)

    def close(self):
        self._socket.close()

    def write(self, string):
        self._socket.send(string + "\n")

    def query(self, string):
        self.write(string)
        r = self._socket.recv(4096)
        while r[-1] != "\n":
            r += self._socket.recv(4096)
        return r

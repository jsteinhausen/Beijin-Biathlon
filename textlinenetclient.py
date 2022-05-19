
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# textlinenetclient.py
#
# Network client class for sending and receiving text lines.
#
# You can use this class for connecting to Swiss Server or AxiCat Server.
#
# Language: Python 3
#
# History:
#
#   2016-10-14  Peter S'heeren, Axiris
#
#      * Created.
#
# -----------------------------------------------------------------------------
#
# Copyright (c) 2016  Peter S'heeren, Axiris
#
# This source text is provided as-is without any implied or expressed
# warranty. The authors don't accept any liability for damages that arise from
# using this source text or from using any software generated from this source
# text.
#
# You're free to copy, modify, and use this source text for any purpose.
#
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


import socket
import re


class TextLineNetClient:


    def __init__(self,host,port):

        # Initialize object variables
        self.auto_commit = False
        self.cmd_buf     = ""
        self.rsp_buf     = ""

        # Connect to the server
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((host,port))


    def __send_cmd_buf(self):
        """
        Send the contents of the command buffer to the client socket.
        """
        total_sent = 0
        cmd_bytes = len(self.cmd_buf)
        while total_sent < cmd_bytes:
            p = str.encode(self.cmd_buf[total_sent:])
            bytes_sent = self.s.send(p)
            if bytes_sent == 0:
                raise TextLineNetClientError("Client socket is broken")
            total_sent += bytes_sent

        self.cmd_buf = ""


    def __send_cmd(self,cmd,force_commit=False):
        """
        Write a command to the command buffer, optionally committing the buffer
        to the client socket.

        Returns: None.
        """
        self.cmd_buf += cmd + "\n"

        if self.auto_commit or force_commit:
            self. __send_cmd_buf()


    def __rcv_rsp(self):
        """
        Receive a response.

        This method is capable of receiving multiple responses. The method will
        always return one response at a time. If more responses are received,
        they're buffered. If no complete response is buffered, the method
        blocks until a response has arrived.

        Returns: String containing response without EOL marker.
        """
        line = ""
        while True:

            # Find the first LF character
            index = self.rsp_buf.find("\n")
            if index >= 0:

                next_start = index + 1

                # The server may report CR->LF as EOL marker
                if self.rsp_buf[index-1] == "\r":
                    index-=1

                # Get the response line without EOL marker
                line = self.rsp_buf[0:index]

                # Trim the line and EOL marker from the response buffer
                self.rsp_buf = self.rsp_buf[next_start:]

                break

            # Receive (blocking mode) a chunk of data bytes/characters from the
            # socket and add it to the response buffer
            chunk = self.s.recv(4096)
            if chunk == '':
                raise TextLineNetClientError("Client socket is broken")
            self.rsp_buf += chunk.decode('utf-8')

            #print("chunk   %d B: %s" % (len(chunk),chunk))
            #print("rsp_buf %d B: %s" % (len(self.rsp_buf),self.rsp_buf))

        #print("line %d B: %s" % (len(line),line))

        return line


    def setAutoCommit(self,enabled):

        self.auto_commit = bool(enabled)


    def commit(self):

        self.__send_cmd_buf()


    def sendCmd(self,cmd,force_commit=False):

        return self.__send_cmd(cmd,bool(force_commit))


    def rcvRsp(self):

        return self.__rcv_rsp()


    def tokenizeLine(self,line):

        # Don't try to understand this academic gibberish, it just works.
        return re.findall(r'"[^"]*"|\'[^\']*\'|[^"\'\s]+',line)


class TextLineNetClientError(Exception):

    pass

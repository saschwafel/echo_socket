import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

    print >>log_buffer, 'connecting to {0} port {1}'.format(*server_address)
    # TODO: connect your socket to the server here.

    #sock.connect(('localhost',10000))
    sock.connect(server_address)

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it

    try:
        print >>log_buffer, 'sending "{0}"'.format(msg)
        # TODO: send your message to the server here.

        #message = sys.argv[1] 
        message = msg
        sock.sendall(message)

        
        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks.  You will want to log them as you receive
        #       each one.  You will also need to check to make sure that
        #       you have received the entire message you sent __before__
        #       closing the socket.
        #
        #       Make sure that you log each chunk you receive.  Use the print
        #       statement below to do it. (The tests expect this log format)

        chunk = ''
        complete_message = []

        while True: 

            chunk = sock.recv(16)

            complete_message.append(chunk)

            print 'received chunk:', chunk


            if len(chunk) < 16:
                
                complete_message = ''.join(complete_message)
                print 'The complete message is: ', complete_message

                #print 'the original message is ', sys.argv[1]
                #print 'the complete_message is ', complete_message

                if complete_message == message:
                    print 'The message was echoed successfully!\n'

                sock.close()
                break


    finally:

        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print >>log_buffer, 'closing socket'

        sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)

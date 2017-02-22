import logging

from dhcplib.server import DHCPProtocol


if __name__ == '__main__':
    import asyncio
    import socket

    from dhcplib import net, getifaddrslib

    logging.basicConfig()
    log = logging.getLogger('dhcplib')
    log.setLevel(logging.DEBUG)

    server_address = '10.99.0.1'
    server_port = 67
    client_port = 68
    iface = getifaddrslib.get_network_interface(server_address)

    log.info('Listen on %s:%s (-> %s)', server_address, server_port, client_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #s.bind((server_address, server_port))
    s.bind(('', server_port))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, iface)

    loop = asyncio.get_event_loop()

    log.info("Starting UDP server")
    #link = net.NetworkLink(server_address, server_port, client_port)
    # One protocol instance will be created to serve all client requests
    listen = loop.create_datagram_endpoint(DHCPProtocol, sock=s)
    #listen = loop.connect_accepted_socket(DHCPProtocol, link)
    transport, protocol = loop.run_until_complete(listen)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('\r', flush=True)
        log.info('Closing...')

    transport.close()
    loop.close()
    log.info('Closed')

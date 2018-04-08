import sys
from pyactor.context import set_context, create_host, serve_forever

if __name__ == "__main__":
    worker_ip_port = sys.argv[1]
    host_ip_port = sys.argv[2]
    worker_name = sys.argv[3]

    set_context()
    host = create_host('http://' + str(worker_ip_port) + '/')

    registry = host.lookup_url('http://' + str(host_ip_port) + '/regis', 'Registry',
                               'Registry')

    registry.bind(worker_name, host)

    serve_forever()

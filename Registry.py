import sys

from pyactor.context import set_context, create_host, serve_forever


class NotFound(Exception):
    pass


class Registry(object):
    _ask = ['get_all', 'bind', 'lookup', 'unbind', 'get_all_names']
    _async = []
    _ref = ['bind', 'lookup']

    def __init__(self):
        self.actors = {}

    def bind(self, name, actor):
        print name, "<- registered in server"
        self.actors[name] = actor

    def unbind(self, name):
        if name in self.actors.keys():
            del self.actors[name]
            print name, "<- unregistered from server"
        else:
            raise NotFound()

    def lookup(self, name):
        if name in self.actors:
            return self.actors[name]
        else:
            return None

    def get_all(self):
        return self.actors.values()

    def get_all_names(self):
        return self.actors.keys()


if __name__ == "__main__":
    ip = sys.argv[1]
    port = 6000
    if len(sys.argv) == 2:
        pass

    elif len(sys.argv) == 3:
        ip = sys.argv[1]
        port = (sys.argv[2])
        try:
            if (int(port) > 65535) or (int(port) < 0):
                print("Error, port must be 0-65535")
                exit(1)
        except ValueError:
            print "Incorrect port. Port must be 0-65535"
            exit(1)

    else:
        print("Incorrect arguments")
        exit(1)

    set_context()
    host = create_host('http://' + str(ip) + ':' + str(port) + '/')

    registry = host.spawn('regis', Registry)

    print 'Registry host(' + ip + ') listening at port ' + str(port)

    serve_forever()

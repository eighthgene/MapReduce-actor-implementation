from MapReduce import MapReduce


class WordCount(MapReduce):
    pass


if __name__ == '__main__':
    mapReduce = WordCount('192.168.0.155', '192.168.0.155:8000', 'Z:/1/2.txt', 'Z:/1/', 'res.txt')
    mapReduce.run()

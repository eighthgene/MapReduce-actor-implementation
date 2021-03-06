# MapReduce actor implementation

This is a simplified model of distributed computing presented by Google, used for parallel computations over very large data sets in computer clusters. This project is simplified [MapReduce](https://en.wikipedia.org/wiki/MapReduce) using implementation of [PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.org/eighthgene/MapReduce-actor-implementation.svg?branch=master)](https://travis-ci.org/eighthgene/MapReduce-actor-implementation)
[![codecov](https://codecov.io/gh/eighthgene/MapReduce-actor-implementation/branch/master/graph/badge.svg)](https://codecov.io/gh/eighthgene/MapReduce-actor-implementation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/70cdb7335c0247a8b07a1bfdad2d4d12)](https://www.codacy.com/app/eighthgene/MapReduce-actor-implementation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=eighthgene/MapReduce-actor-implementation&amp;utm_campaign=Badge_Grade)

## Project architecture
This is a simplified implementation of MapRedus. Model consists of: N-number of workers nodes, 1 reducer and Master (main). It is a framework for computing some sets of distributed tasks using a large number of computers that form a cluster. 

The work of MapReduce consists of two steps: Map and Reduce which we can override to use.
![untitled diagram 2](https://user-images.githubusercontent.com/18737866/38579072-27e1c64e-3d06-11e8-8198-5135d03de87a.jpg)

The modules of implementation:
- **Master.py**: The main program in which one method for starting **run()**
- **Registry.py**: Service of system workers names. Used for lookup bind, unbind, lookup actors in system.
- **MapReduce.py**: Consists of two classes of **actors: Mapper and Reducer**.
- **Worker.py**: Client class to connect to the system.
- **FileHandler.py**: Сlass for splitting the input file.

Auxiliary:
- **Timer.py**: Actor class used to measure the running time

![untitled diagram 3](https://user-images.githubusercontent.com/18737866/38579136-6371968a-3d06-11e8-9f71-3ccd8c2136ae.jpg)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Packages required:

    python, python-dev, python-pip

### Installing

    sudo pip install pyactor

If pip installs pyactor but gives an error with gevent, check that 'python-dev'
is installed and try again with:

    sudo pip install gevent

Or download the source by cloning [PyActor](https://github.com/pedrotgn/pyactor)'s
repository and installing with:

    sudo python setup.py install

If you clone the repository, you will also have access to the tests and a folder
full of examples. Just check the github page and the documentation for a detailed
tutorial.

## How to run
To run the system, follow these steps:

**Step 1:** Start the Registry
    
    python Registry.py [IP] [PORT]
or

    python Registry.py [IP]
 
_NOTE!_ Default port will be **:6000**

**Step 2:** Connect one or more clients (workers) to Registry.

    python Worker.py [IP_WORKER:PORT] [IP_REGISTRY:PORT] [USERNAME]

_NOTE!_ If you run all the workers on the same machine, you need to specify different ports for each of them.

Exemple:
_2 clients in same computer_

    python Worker.py 192.168.0.22:7001 192.168.0.22:6000 user1
    python Worker.py 192.168.0.22:7002 192.168.0.22:6000 user2

**Step 3:** Start HTTP server in the folder where the input file is located.

    python -m SimpleHTTPServer
    
**Step 4:** Create in you program:
- create your own class that is inherited from **Master**
- create class that is inherited from **Mapper** and override function **map()**
    
    ```
    IMPORTANT! 
    This function recive argument **data** (lines of input text) as parametr. 
    ```
Example WordCount function map() and class inherited from Mapper:

```python
class MapImpl(Mapper):
        def map(self, data):
            results = {}
            for line in data:
                line_words = line.split()
                for word in line_words:
                    word = re.sub("[^a-zA-Z]+", "", word)
                    if word != '':
                        word = word.lower()
                        if word in results:
                            results[word] += 1
                        else:
                            results[word] = 1
        return results
```

    ```
    IMPORTANT! 
    map() have to return dictionary.
    ```

- create class that is inherited from **Reducer** and override function **redue()**
Example WordCount function Reduce() and class inherited from Reducer:


```python
class ReduceImpl(Reducer):

    def reduce(self, list_of_dict):
        reduced_dict = {}
        for dictionary in list_of_dict:
            tmp_dict = dict(dictionary)
            reduced_dict = dict(Counter(tmp_dict) + Counter(reduced_dict))
        return reduced_dict
```


**Step 5:** Create instance of your class and pass parameters:
    
    # ip host (Master)
    # IP HTTP Server
    # Input file path
    # Output path
    # Name output file (.txt)
    [IP], [IP_HTTP_SERVER:PORT], [FILE_DIR], [OUTPUT_DIR], [FILE_NAME] 
    
Example:

```python
mapReduce = WordCount('192.168.0.22',
                          '192.168.0.22:8000',
                          './Files/pg2000.txt', './Files', 'result_distributed.txt',
                          'WordCount/MapImpl', 'WordCount/ReduceImpl')
```

**Step 6:** Finally, call function **run()**
  
    mapReduce.run()

    
    
    

## Authors

* **Oleg Sokolov** -    [eighthgene](https://github.com/eighthgene)
* **Enyu Lin** -        [enyuLin](https://github.com/enyuLin)





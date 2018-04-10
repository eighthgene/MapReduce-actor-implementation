# MapReduce actor implementation

This is a simplified model of distributed computing presented by Google, used for parallel computations over very large data sets in computer clusters. This project is simplified [MapReduce](https://en.wikipedia.org/wiki/MapReduce) using implementation of [PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.org/eighthgene/MapReduce-actor-implementation.svg?branch=master)](https://travis-ci.org/eighthgene/MapReduce-actor-implementation)

## Getting Started
This is a simplified implementation of MapRedus. Model consists of: N-number of workers nodes, 1 reducer and Master (main). It is a framework for computing some sets of distributed tasks using a large number of computers that form a cluster. 

The work of MapReduce consists of two steps: Map and Reduce which we can override to use.
![untitled diagram 2](https://user-images.githubusercontent.com/18737866/38579072-27e1c64e-3d06-11e8-8198-5135d03de87a.jpg)

The modules of implementation:
- **Master.py**: The main program in which one method for starting **run()**
- **Registry.py**: Service of system workers names. Used for lookup bind, unbind, lookup actors in system.
- **MapReduce.py**: Consists of two classes of **actors: Master and Reducer**.
- **Worker.py**: Client class to connect to the system.
- **FileHandler.py**: Сlass for splitting the input file.

Auxiliary:
- **Timer.py**: Actor class used to measure the running time



![untitled diagram 3](https://user-images.githubusercontent.com/18737866/38579136-6371968a-3d06-11e8-9f71-3ccd8c2136ae.jpg)






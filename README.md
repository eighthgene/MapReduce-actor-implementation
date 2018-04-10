# MapReduce actor implementation

This is a simplified model of distributed computing presented by Google, used for parallel computations over very large data sets in computer clusters. This project is simplified [MapReduce](https://en.wikipedia.org/wiki/MapReduce) using implementation of [PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.org/eighthgene/MapReduce-actor-implementation.svg?branch=master)](https://travis-ci.org/eighthgene/MapReduce-actor-implementation)

## Project architecture
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
1- Start the Registry
    
    python Registry.py [IP] [PORT]
or
    ```
    python Registry.py [IP]
    ```
_NOTE!_ Default port will bee **:6000**


   

## Authors

* **Oleg Sokolov** -    [eighthgene](https://github.com/eighthgene)
* **Enyu Lin** -        [enyuLin](https://github.com/enyuLin)





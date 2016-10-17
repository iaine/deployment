#!/bin/bash

echo "Running tests with Python2"

nosetests


echo "Running tests with Python 3"
python3 -m "nose" 


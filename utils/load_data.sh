#!/bin/bash

# wget https://data.acfr.usyd.edu.au/ag/treecrops/2016-multifruit/acfr-multifruit-2016.zip
gdown 1wJGYONDsaVZ0z2b-ovMcntGvR_JGrfq0
echo "Unpacking zip archive..."
unzip -q acfr-fruit-dataset.zip
echo "Unpacking done!"
rm acfr-fruit-dataset.zip

mkdir data
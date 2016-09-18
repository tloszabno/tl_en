# tl_en
Lern english words with translations by system notifications


## Requirements

* python
* pip installer
* make

## Configure

Please edit file tl_en/config.py and enter valid path to dictionary to var WORDS_DICTIONARY_PATH.
Dictionary should be in format:
word1_en - translation1 - some description1 - some sample1 etc...
word2_en - translation2 - some description2 - some sample2 etc...

## Run

* sudo make
* make run
* make clean


## TODO

* Create client side api (to stop, hold daemon, etc)
* Read files with word groups, and add possibility to decide from which group show words

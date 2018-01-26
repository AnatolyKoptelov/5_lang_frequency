# Frequency Analysis of Words


Application for counting words frequency on a text. File path of this text file is  command line required argument.
By default, it works with encoded utf_8 files, but sometimes your files can have a different encoding. 
You can use optional parameter **-c** for decode an original file. This application supports these codecs:

 - utf_8
 - cp1251
 - koi8_r
 - cp866
 - mac_cyrillic
 
Use optional parameter **-q** for number of words setting on output

# Quickstart

Example of script launch on Linux, Python 3.*:

```
$ python lang_frequency.py examles_of_texts/roman.txt

the     11819
of      7747
and     3944
to      3345
in      2487
a       1983
was     1553
by      1261
that    1149
his     1146
```
Use -h option for read application info:
```
$ python lang_frequency.py -h
usage: lang_frequency.py [-h] [-q [QUANTITY]]
                         [-c [{utf_8,cp1251,koi8_r,cp866,mac_cyrillic}]]
                         path

Frequency Analysis of Words

positional arguments:
  path                  File path

optional arguments:
  -h, --help            show this help message and exit
  -q [QUANTITY], --quantity [QUANTITY]
                        How many frequent words to display
  -c [{utf_8,cp1251,koi8_r,cp866,mac_cyrillic}], --codec [{utf_8,cp1251,koi8_r,cp866,mac_cyrillic}]
                        Use for decode a original file
```

# Future

In the next release will be add **-r** command line option for less frequent words displaying

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

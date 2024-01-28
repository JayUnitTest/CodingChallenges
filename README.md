# CODING CHALLENGES | Honing Python Skills

- [CODING CHALLENGES | Honing Python Skills](#coding-challenges--honing-python-skills)
  - [The Challenges:](#the-challenges)
    - [1. Building Your Own Cat-Tool](#1-building-your-own-cat-tool)
      - [what is click? (quick summary)](#what-is-click-quick-summary)
      - [Progress](#progress)
        - [current commands available.](#current-commands-available)

Here I will be completing coding challenges set by John Crickett.

>These are weekly coding challenges aimed to help software engineers level up their skills through deliberate practice.

I aim to use these challenges to progress my skills in Python. 

To get more information on the challenges, [click here](https://codingchallenges.fyi/challenges/intro/)

## The Challenges:
### 1. Building Your Own [Cat-Tool](https://github.com/JayUnitTest/CodingChallenges/tree/main/cat-tool)
  
This challenge is to build your own version of the Unix Command line tool **cat**. 

Originally, I began with argparse. However, through recommendation I am now using [Click](https://click.palletsprojects.com/en/8.1.x/). 

#### what is click? (quick summary)
>Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box. It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.


#### Progress

- Step Zero completed - test files received to test solution with.
- Step 1 completed - open specific file on the command line and write its contents to standard out. 
- Step 2 completed - Can read the input from standard in.
- Step 3 completed -  Can concatenate files
- step 4 completed -  number the lines as they’re printed out

##### current commands available.
```
% python cccat.py --help

Usage: cccat.py [OPTIONS] [FILENAMES]...

Options:
  -n      Number the lines outputted to the console
  --help  Show this message and exit.
```
```
% python cccat.py test.txt

"Your heart is the size of an ocean. Go find yourself in its hidden depths."
"The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
"Thinking is the capital, Enterprise is the way, Hard Work is the solution."
"If You Can'T Make It Good, At Least Make It Look Good."
"Heart be brave. If you cannot be brave, just go. Love's glory is not a small thing."
...
```
```
head -n1 test.txt | python cccat.py

"Your heart is the size of an ocean. Go find yourself in its hidden depths."
```
```
% python cccat.py test.txt test2.txt

concatenates (nargs=-1) files. 
```
```
% head -n3 test.txt | python cccat.py -n

1: "Your heart is the size of an ocean. Go find yourself in its hidden depths."
2: "The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
3: "Thinking is the capital, Enterprise is the way, Hard Work is the solution."
```
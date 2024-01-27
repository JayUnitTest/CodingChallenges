# CODING CHALLENGES | Honing Python Skills

- [CODING CHALLENGES | Honing Python Skills](#coding-challenges--honing-python-skills)
  - [The Challenges:](#the-challenges)
    - [1. Building Your Own Cat-Tool](#1-building-your-own-cat-tool)
    - [what is click? (quick summary)](#what-is-click-quick-summary)

Here I will be completing coding challenges set by John Crickett.

>These are weekly coding challenges aimed to help software engineers level up their skills through deliberate practice.

I aim to use these challenges to progress my skills in Python. 

To get more information on the challenges, [click here](https://codingchallenges.fyi/challenges/intro/)

## The Challenges:
### 1. Building Your Own [Cat-Tool](https://github.com/JayUnitTest/CodingChallenges/tree/main/cat-tool)
  
This challenge is to build your own version of the Unix Command line tool **cat**. 

Originally, I began with argparse. However, through recommendation I am now using [Click](https://click.palletsprojects.com/en/8.1.x/). 

### what is click? (quick summary)
>Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box. It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.


Progress: 

- Step Zero completed - test files received to test solution with.
- Step 1 completed - open specific file on the command line and write its contents to standard out. 
- Step 2 completed - Can read the input from standard in.

current commands available.
```
% python cccat.py --help
Usage: cccat.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  cat
  head
```
```
% python cccat.py head test.txt
returning line(s)...

"Your heart is the size of an ocean. Go find yourself in its hidden depths."
"The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
"Thinking is the capital, Enterprise is the way, Hard Work is the solution."
"If You Can'T Make It Good, At Least Make It Look Good."
"Heart be brave. If you cannot be brave, just go. Love's glory is not a small thing."
```

```
% python cccat.py head -n1 test.txt
returning line(s)...

"Your heart is the size of an ocean. Go find yourself in its hidden depths."
```
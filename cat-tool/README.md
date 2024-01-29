# Building Your Own [Cat-Tool](https://github.com/JayUnitTest/CodingChallenges/tree/main/cat-tool)

This challenge is to build your own version of the Unix Command line tool **cat**.

Originally, I began with argparse. However, through recommendation I am now using [Click](https://click.palletsprojects.com/en/8.1.x/).

#### what is click? (quick summary)

> Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box. It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

#### Progress

0.  Step Zero completed - test files received to test solution with.
1.  Step 1 completed - open specific file on the command line and write its contents to standard out.
2.  Step 2 completed - Can read the input from standard in.
3.  Step 3 completed - Can concatenate files
4.  Step 4 completed - number the lines as they’re printed out
5.  Step 5 Completed - Number lines but exclude blank lines from being numbered in output

## How to Use the Cat Tool

To get started, I followed Click's quickstart guide that you can find [here](https://click.palletsprojects.com/en/8.1.x/quickstart/)

A virtual environment was used for this project as recommended. This solves the problem of of any clashes of different versions of python or different versions of libraries across projects.

1. **Clone the Repo**:

   ```bash
   git clone https://github.com/JayUnitTest/CodingChallenges.git
   ```

2. **Navigate into the cat-tool Project**:

   ```bash
   cd codingchallenges/cat-tool
   ```

3. **Create a Virtual Environment**:

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:

   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies**:

   ```bash
   pip install click
   ```

   Now you're good to go! The list of commands is available below and how to use them

### Commands

```bash
% python cccat.py --help
```

Output:

```
Usage: cccat.py [OPTIONS] [FILENAMES]...

Options:
  -n      Number the lines outputted to the console
  -b      Number lines but exclude blank lines being numbered in output.
  --help  Show this message and exit.
```

```bash
% python cccat.py test.txt
```

Output:

```
"Your heart is the size of an ocean. Go find yourself in its hidden depths."
"The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
"Thinking is the capital, Enterprise is the way, Hard Work is the solution."
"If You Can'T Make It Good, At Least Make It Look Good."
"Heart be brave. If you cannot be brave, just go. Love's glory is not a small thing."
...
```

```bash
head -n1 test.txt | python cccat.py
```

Output:

```
"Your heart is the size of an ocean. Go find yourself in its hidden depths."
```

```bash
% python cccat.py test.txt test2.txt
```

Output:

```
concatenates (nargs=-1) files.
```

```bash
% head -n3 test.txt | python cccat.py -n
```

Output:

```
1: "Your heart is the size of an ocean. Go find yourself in its hidden depths."
2: "The Bay of Bengal is hit frequently by cyclones. The months of November and May, in particular, are dangerous in this regard."
3: "Thinking is the capital, Enterprise is the way, Hard Work is the solution."
```

Number lines and blank lines to output

```bash
sed G test2.txt | python cccat.py -n | head -n5
```

Output:

```
1: "I Don'T Believe In Failure. It Is Not Failure If You Enjoyed The Process."
2:
3: "Do not get elated at any victory, for all such victory is subject to the will of God."
4:
5: "Wear gratitude like a cloak and it will feed every corner of your life."
```

Number lines but excludes blank lines from being numbered
sed G is used to add extra blank lines.

```bash
sed G test2.txt | python cccat.py -b | head -n5
```

Output:

```
1: "I Don'T Believe In Failure. It Is Not Failure If You Enjoyed The Process."

3: "Do not get elated at any victory, for all such victory is subject to the will of God."

5: "Wear gratitude like a cloak and it will feed every corner of your life."
```

## What I learned during this challenge:

This is the first time I've built my own version of the Unix command-line tool cat, so there were, of course, many learning experiences:

**Click**: Click was entirely new to me. Prior to this, I had only partially worked with argparse, and even then, it wasn't extensive. Click was quite intuitive to use once I got past my self-conflicted confusion.

**Taking a step back**: I originally began this project head-on and tried to immediately start coming up with the solutions. Next time, I will digest what it is that I'm trying to accomplish, especially when facing new things:

- What is the challenge?
- What is the technology?
- Why is it used?
- How is it used?

I have already learned a lot from my first challenge, and I will carry this onto the next! And then the next! And then the NEXT!
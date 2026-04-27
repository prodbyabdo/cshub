# Repetition

## Contents of Lecture:

```
 Introduction
 The Pre-Test Loop (while loop).
 The Post-Test Loop (do while loop).
 Counted Loops (for loop).
 Homework number (4) delivered next week
```
## Introduction

 The programs developed so far have used sequence and/or selection.
 The logical flow of the program is from top to bottom.
 If selection is used then some of the steps may be omitted.

 Many problems require that steps be repeated.
 This is commonly known as looping, repetition or iteration.

 It is called looping because logically it forms a loop as instructions are executed one
after the other in the forward direction then control jumps back to the start of the loop
and this is repeated again, and again.

 To perform repetition successfully we need to know two things:
 The instructions are to be repeated (e.g. lines 5 through 10)
 When to stop looping.

 There are three different loop constructs that can be used:

1. The Pre-Test Loop (while loop).
2. The Post-Test Loop (do while loop).
3. Counted Loops (for loop).

## The Pre-Test Loop (while loop):

```
While (condition)
Statement
...
Statement
EndLoop
```
```
NO
```
```
Yes
```

 The key feature of the pre-test loop is that we test to see whether or not to continue
before executing the body of the loop. The effect of this is that we might not execute
the body at all.

 So, if we're designing a program that has a section which might be executed 0 or
more time (that is we're not guaranteed that it will be executed at all), a pre-test
structure is what we want.

## The Post-Test Loop (do while loop).

 As you might expect, if we don't test to determine whether or not to continue until
after we've executed the block, the loop body will always be executed at least once.
This distinguishes it from the pre-test loop.

## Counted Loops (for loop)

 For loop allows a statement to be executed a specified number of times.
 It is begin with a loop control variable: assigned a specific initial value.
 This control variable in then incremented (or decremented) by a specified amount
each time around the loop until a specified terminating value is reached at which time
the statement following the loop is then executed.

 For loop is a very powerful tool to use with arrays (a topic covered later).
 This loop is a specialized construct for iterating a specific number of times, often
called a "counted loop". The general form is:

```
NO
```
```
Yes
```
```
Do
Statement
...
Statement
While (condition)
```

### Example:

Write a program that output number from 1 to 10 using the two alternative
solutions (The Pre-Test Loop, the Post-Test Loop and Counted loop):

```
For initial value to final value
Statements
UpdateStatment
EndLoop
```
```
NO
```
```
InitialStatment
```
```
Condition
```
```
Statments...
```
```
YES
```
```
UpdateStatment
```


## Homework number (4) delivered next week

1. By using for loop write pseudo code print line of five stars, after that draw
    flowchart.
2. Write a program that output number from 1 to 10 every number followed by star,
    using the two alternative solutions (The Pre-Test Loop, the Post-Test Loop and
    Counted loop)



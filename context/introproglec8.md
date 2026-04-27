# Accumulator and Counter

Contents of Lecture:
 Introduction
 Counting
 Accumulating
 Homework number (5) delivered next week

## Introduction

 We have two common operations served by repetition structures:
 Counting operations
 Accumulating operations.

## Counting

 The counting is a very important operation in programming.
 We will count to:
 perform calculations (i.e. averaging numbers)
 Count to determine if we need to keep on looping in a while, do..while block.

 Counting is accomplished in logic by defining a variable and adding or subtracting a
value to/from the variable during each repetition loop.

 If you add to the counter on each loop, the counter value increases (incrementing).
 If we subtract on each loop, we count down (decrementing) with the counter.

 We can count by ones or by larger numbers.
 Here are some counting examples illustrated in pseudo code and flow chart:


Example (1):

 The counting activity in a program is accomplished by defining and initializing a
variable and placing that variable inside the loop.

 With each repetition of the loop, a value is added to the counter to increment or a
value is subtracted from the counter to decrement.

### 1. Begin

### 2. Set 0 to count

### 3. Set 0 to countDown

### 4. Set 0 to countByFive

### 5. While count <= 10

### count equals count + 1

### countDown equals countDown – 1

### countByFive equals countByFive + 5

### EndLoop

### 6. Display count, countDown, countByFive

### 7. End

```
Start
```
### Set 0 to count

### Set 0 to countDown

### Set 0 to countByFive

```
NO
```
```
YES
```
### count = count + 1

### countDown = countDown – 1

### countByFive = countByFive + 5

```
Display count, countDown, countByFive
```
```
End
```
```
If
(count<=10)?
```

Example (2): write pseudocode and draw flowchart to Count the number of four items
weighting over 20 kg.

### 1. Begin

### 2. Set 0 to count

### 3. Set 0 to cntover

### 4. While (count < 4)

### Get num

### If ( num > 20)

### cntover  cntover +

### EndIf

### count  count +

### EndLoop

### 5. Display “Number Over 20:” cntover

### 6. End

```
NO
```
```
Start
```
```
End
```
### Set 0 to count

```
If
```
### (count< 4)?

### cntover = cntover +

```
YES
```
### Set 0 to cntover

```
Display “Number Over 20:” cntover
```
### Get num

```
If
```
### (num > 20)?

```
YES
```
```
NO
```
### count = count +


## Accumulating

 Accumulating is also a popular operation used in program logic.
 With accumulation, and accumulator variable is designated to accumulate numbers in
a variable.

 The statements necessary to perform accumulation look very similar to the counting
statements.

 Instead of incrementing a counter variable by a set number, we will be taking some
value or identifier and add this to the accumulator variable on each repetition.

 The effect is that the accumulator variable grows (summarizes) on each pass of the
loop.

 In the following pseudo code and flow chart example, we use a counter and
accumulator variables to calculate a test average of five test scores.


## Homework number (5) delivered next week:

1) Write a pseudo code and flowchart to display the multiplication table for number
four.
2) Modify question (1) to display the multiplication table for number entered by the
user.
3) Write a pseudo code and draw flow chart to read ten numbers and compute their
average using iterations.
4) Write a program to calculate the total of a series of student’s marks. The user initially
inputs the number of marks to be input. Students' marks are whole numbers. Assume
marks input by the user are valid (0...100).



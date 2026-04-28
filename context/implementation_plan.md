# Course Summary Tab — year1sem2introprog.html
# Implementation Plan (Revised)

## Context

This plan targets the file `year1sem2introprog.html` hosted at:
`https://prodbyabdo.github.io/cshub/year1sem2introprog.html`

The agent has access to the following lecture PDFs which are the **sole source of truth**
for all content. Do not invent, paraphrase loosely, or add content not found in these files:

| File | Covers |
|------|--------|
| `context\introproglec1.md` | Introduction to Computers & Hardware |
| `context\introproglec2.md` | Computer Software, Languages |
| `context\introproglec3.md` | Program Development Life Cycle, Constants & Variables |
| `context\introproglec4.md` | Pseudocode |
| `context\introproglec5.md` | Flowcharts |
| `context\introproglec6.md` | Branching |
| `context\introproglec7.md` | Repetition / Loops |
| `context\introproglec8.md` | Accumulator and Counter |

---

## Summary of Changes

1. **Tab bar**: Insert a new first tab button `Course Summary` (id: `course-summary`), active by default.
   Rename the existing first tab from `Subject Summary` → `Java Summary`.
2. **Tab content**: Add a new `<div id="course-summary" class="tab-content active">` inserted
   **before** the existing `#summary` div.
3. **Existing `#summary` div**: Remove `active` from its class — it is no longer the default tab.
4. **JS/CSS**: No changes. The existing `openTab()` function and CSS handle any number of tabs.
5. **Lec2 Java note**: Add a small note card at the top of §11 (Loops) in the Java Summary tab
   stating that §11 covers both Java Lec1 and Lec2 content.

---

## Tab Bar Change (locate the existing tab bar buttons)

Current (find this block):
```html
Subject Summary
Practice Exam
Java Tutorials
Java Compiler
```

Replace with:
```html
Course Summary
Java Summary
Practice Exam
Java Tutorials
Java Compiler
```

Note: the exact class names and onclick attribute format may differ slightly in the actual file.
Match the existing pattern exactly — do not guess.

---

## Existing `#summary` div

Find: `<div id="summary" class="tab-content active">`
Replace with: `<div id="summary" class="tab-content">`

---

## New `#course-summary` div — Insert before `#summary`

Insert the following div immediately before the `#summary` div.
Use the **exact same CSS classes** already used in the page (`.section-title`, `.card`, `.sheet`, `<pre><code>`, etc.).
Match the visual style of the existing §1–§12 Java content precisely.

---

## Content Specification — §1 through §8

Use **exact wording from the lecture PDFs** wherever the plan quotes the source.
Do not paraphrase definitions. Lecture wording is in quotes below.

---

### §1 — Introduction to Computers (LEC1_074920.pdf)

**Card: Definition**
- "A computer is a machine that performs a variety of tasks according to specific instructions.
  It's capable of performing computations and making logical decisions at speeds millions and even
  billions of times faster than human beings can."
- Example from lecture: "many of today's personal computers can perform hundreds of millions of
  additions per second."
- Two components of a computer system: **Hardware** and **Software**

**Card: Computer Hardware**
- "Computer hardware is the collection of physical elements that constitutes a computer system."
- Examples: keyboard, screen, mouse, disks, memory, CD-ROM, processing units
- "Almost every computer may be seen as being divided into six logical units."

**Table: Six Logical Units**
Render as a `.sheet` table with two columns: Unit Name | Description

| Unit | Description |
|------|-------------|
| Input Unit | Allows the user to enter information into the system. Obtains information from input devices (keyboard, mouse, touchpad, webcam, microphone, joystick, image scanner) and places it at the disposal of other units. |
| Output Unit | Takes processed information and places it on output devices. Most output is displayed on screens, printed on paper, or used to control other devices. |
| Memory Unit | Stores information. RAM (Random Access Memory) is volatile — stores programs and data while in use. ROM (Read Only Memory) is non-volatile — contains fundamental instructions that cannot be lost or changed. |
| Arithmetic and Logic Unit (ALU) | Performs all arithmetic and logic operations. Examples: addition, subtraction, comparison. |
| Central Processing Unit (CPU) | Supervises the overall operation of the computer. Tells the input unit when to read into memory, tells the ALU when to compute, tells the output unit when to send data to output devices. |
| Secondary Storage | Permanent storage for programs and data. Uses magnetic tapes, magnetic disks, and CD-ROMs. |

---

### §2 — Computer Software (LEC2_074843.pdf)

**Card: Definitions**
- "Software is computer programs that run on a computer. Software is instructions that can be
  stored and run by hardware."
- "Hardware is directed by the software to execute any command or instruction."
- "A computer program is a set of instructions used to operate a computer to produce a specific result."
- "Programming languages is a languages used to create computer programs."
- "Computer programming mean writing a computer programs by a programmer using programming language."

**Card: Machine Languages**
- "Machine languages are the lowest level of computer languages. Programs written in machine language
  consist of entirely of 1s and 0s."
- "Programs in machine language can control directly to the computer's hardware."
- A machine language instruction has two parts:
  - **Instruction part (opcode):** leftmost group of bits; tells the computer the operation to perform
  - **Address part:** specifies the memory address of the data

Example from lecture:
```
00101010 000000000001 000000000010
10011001 000000000010 000000000011
```

**Card: Assembly Languages**
- "Assembly languages perform the same tasks as machine languages, but use symbolic names for
  (opcode) and operands instead of 1s and 0s."
- Must be translated into machine language before execution (Assembly → Machine Language translation)
- Machine and assembly languages are called **low-level languages** — closest to computer hardware

Example from lecture:
```
LOAD BASEPAY
ADD OVERPAY
STORE GROSSPAY
```

**Card: High-Level Programming Languages**
- "High-level programming languages create computer programs using instructions that much easier to
  understand than machine or assembly language instructions."
- Must be translated into a low-level language using a **compiler**
- "A compiler is a program that translates programming code written in a high-level language into a
  low-level format."
- Each line in a high-level language program is called a **statement**. Example: `Result = (First + Second)*Third`
- Two translation methods:
  - **Interpreted language:** each statement translated and executed immediately upon translation;
    the program doing this is an **interpreter**
  - **Compiled language:** all statements translated as a complete unit before any statement executes;
    the program doing this is a **compiler**
- Examples from lecture: FORTRAN, COBOL, BASIC, PASCAL, C, C++, JAVA

**Card: Application vs System Software**
- **Application software:** "programs written to perform particular tasks required by the users"
- **System software:** "the collection of programs that must be available to any computer system for
  it to operate"
- "The most important system software is the operating system."
- OS examples: MS-DOS, UNIX, MS WINDOWS
- **Multitasking systems:** operating systems that allow users to run multiple programs simultaneously
- Language translators are also system software

---

### §3 — The Program Development Life Cycle (LEC3_074911.pdf)

**Card: Overview**
- "Programmers do not sit down and start writing code right away when trying to make a computer program."
- "Instead, they follow an organized plan or methodology that breaks the process or problem into a
  series of tasks."

**Numbered steps (render as a styled ordered list or step cards):**
1. Problem Definition
2. Problem Analysis
3. Algorithm design and representation (Pseudocode or flowchart)
4. Coding and debugging

**Card: Step 1 — Problem Definition**
- "This stage is the formal definition of the task."
- Includes: specification of inputs and outputs, processing requirements, system constraints,
  error handling methods
- "This step is very critical for the completion of a satisfactory program."
- "It is impossible to solve a problem by using a computer, without a clear understanding and
  identification of the problem."
- "A clearly defined problem is already half the solution."
- Example problem used throughout the lecture: *"Create a program that will know how much older
  one person is than another."*

**Card: Step 2 — Problem Analysis**
- Break the problem into smaller, simpler sub-problems
- Example: Input = first age, second age. Output = difference of ages.

**Card: Step 3 — Algorithm Design**
- "An Algorithm is a clear and unambiguous specification of the steps needed to solve a problem.
  It may be expressed in either Human language (English, Arabic), through a graphical representation
  like a flowchart or through a pseudocode, which is a cross between human language and a
  programming language."
- Show all three representations of the age-difference example:

Human language:
```
1. Ask user for first age.
2. Ask user for second age.
3. Subtract second age from first age.
4. Print result.
```

Pseudocode:
```
1. Begin
2. Get first_age
3. Get second_age
4. Result ← first_age – second_age
5. Display Result
6. End.
```

(Flowchart: note that the flowchart diagram from the PDF is not reproducible as an image;
render a simple text note: "See lecture flowchart for the graphical representation.")

**Card: Step 4 — Coding and Debugging**
- "After constructing the algorithm, it is now possible to create the source code."
- "Most of the time, after the programmer has written the program, the program isn't 100% working
  right away."
- Debugging: process of fixing errors (bugs) in a program

Two types of errors:

1. **Compile-Time Errors**
   - "Occur if there is a syntax error in the code."
   - "The compiler will detect the error and the program won't even compile."
   - Example: "Forgetting a semi-colon at the end of a statement or misspelling a certain command"

2. **Runtime Errors**
   - "Compilers aren't perfect and so can't catch all errors at compile time."
   - Example: infinite loops — "the same piece of code keeps executing over and over again infinitely"
   - "The program compiles fine into an executable file. However, and unfortunately, when the
     end-user runs the program, the program (or even their whole computer) freezes up."
   - Other examples: incorrect value computed, wrong thing happens

**Card: Constants and Variables**
- "Constants and variables are two entities which are used to store information (technically called
  data) in your program."
- "Constant is a value that never changes as the instructions in a program are followed."
- "Variable is a value that does change as the instructions in a program are followed."
- Both are given names used to refer to memory locations instead of memory addresses
- "You should always use names that are most meaningful to the end user"

**Four naming rules (from lecture — exact wording):**
1. Name a constant or variable according to what it represents.
2. Do not use spaces in a constant or variable name.
3. Start a constant or variable name with a letter, not a number.
4. Do not use a dash or hyphen in a name (the computer will think it a subtraction sign),
   an underscore is fine.

---

### §4 — Pseudocode (LEC4_074916.pdf)

**Card: Definition**
- "Pseudo code is a nonstandard English-like programming language used by programmers to model
  logic and instructions."
- "Pseudo-Code is simply a numbered list of instructions to perform some task."
- "Pseudo code is called a programming language even through it cannot be excluded by a computer."
- "It is designed for planning purposes only."
- "By nonstandard, if you open five books on programming, all would have pseudo code examples but
  all of those examples would look somewhat different."
- "Pseudo code provides us with a way to concentrate on just logic structures without be constrained
  by the syntax rules of a particular programming language."
- "Generally, flowcharts work well for small problems but Pseudo code is used for larger problems."

**Card: Basics of Writing Pseudocode**

**1 — Receiving information**
Keywords: `Get`, `Read`, `Input`
```
Get filename
Read class number
Input radius
```

**2 — Outputting information**
Keywords: `Print`, `Write`, `Output`, `Display`
```
Print 'Program Completed'
Write student names
Display area
```
`Prompt` is used to explain what variable should be input:
```
Prompt user to enter the radius
```

**3 — Arithmetic**
Either mathematical symbols or words:
```
Multiply Length by Width to Compute Area
Area = Length * Width
```
Words and equivalent symbols:
- Parentheses or ( )
- Add or +
- Subtract or –
- Multiply or *
- Divide or /
- Modulus or %

`Compute` and `Calculate` are also valid:
```
Compute degrees Celsius
C = (F – 32) / 1.8
```

**4 — Assigning values**
`Initialize` or `Set` for initial values:
```
Set total_price to 0
Initialize PI to 3.14
```
`=` or `←` for result of processing:
```
total_price ← cost_price + sales_tax
```

**Card: Examples**

**A. Find the Summation of two numbers:**
```
1. Begin
2. Prompt user to enter for number_one
3. Get number_one
4. Prompt user for to enter number_two
5. Get number_two
6. sum ← number_one + number_two
7. Display sum
8. End
```

**B. Calculating the Circle area:**
```
1. Begin
2. Initialize PI to 3.14
3. Prompt user to enter radius
4. Read radius
5. area ← PI * radius * radius
6. Print area
7. End
```

**C. Calculating the Rectangle area:**
```
1. Begin
2. Prompt user to enter Length
3. Input Length
4. Prompt user to enter Width
5. Input Width
6. Multiply Length by Width to Compute Area
7. Output Area
8. End
```

---

### §5 — Flowcharts (LEC5_092519.pdf)

**Card: Definition**
- "A flowchart is a design tool used to graphically represent the logic in a solution."
- "Flowcharts typically do not display programming language commands. Rather, they state the
  concept in English or mathematical notation."
- "You can use any symbols in creating your flowcharts, as long as you are consistent in using them."

**Table: Flowchart Symbols**
Render as a `.sheet` table. For each row, use a simple inline SVG to illustrate the shape.
Columns: SVG shape | Symbol Name | Meaning

| Shape (SVG) | Symbol Name | Meaning |
|-------------|-------------|---------|
| Rectangle | Process Symbol | "Represents the process of executing a defined operation or groups of operations that results in a change in value, form, or location of information. Also functions as the default symbol when no other symbol is available." |
| Parallelogram | Input/Output (I/O) Symbol | "Represents an I/O function, which makes data available for processing (input) or displaying (output) of processed information." |
| Arrow line | Flow line Symbol | "Represents the sequence of available information and executable operations. The lines connect other symbols, and the arrowheads are mandatory only for right-to-left and bottom-to top flow." |
| Rectangle with torn right edge | Annotation Symbol | "Represents the addition of descriptive information, comments, or explanatory notes as clarification." |
| Diamond | Decision Symbol | "Represents a decision that determines which of a number of alternative paths is to be followed." |
| Oval / Rounded rectangle | Terminal Symbol | "Represents the beginning, end, or a point of interruption or delay in a program." |
| Rectangle with double vertical lines | Predefined Process Symbol | "Represents a named process consisting of one or more operations or program steps that are specified elsewhere." |
| Small circle | Connector Symbol | "Represents any entry from, or exit to, another part of the flowchart. Also serves as an off-page connector." |

**Card: Example — Sum, Average and Product of Three Numbers**
Show pseudocode and note that the flowchart mirrors it:
```
1. Begin
2. Prompt user to enter no1, no2, no3
3. Get no1, no2, no3
4. Sum ← no1 + no2 + no3
5. Avg ← Sum / 3
6. Prd ← no1 * no2 * no3
7. Display Sum, Avg, Prd
8. End
```

---

### §6 — Branching (LEC6_092556.pdf)

**Card: Introduction**
- "A program is usually not limited to a linear sequence of instructions."
- "Branching statements allows us to redirect the flow of program execution."
- "Branch statements that allow us to select and execute specific blocks of code while skipping
  other sections."

**Card: Conditional Structure**
- "In practice, the computer is presented not with a true / false statement, but with a question
  having a 'Yes' or 'No' answer using relational operators ( >, <, >=, <=, =, ≠ )."
- The decision symbol (diamond) is the only flowchart symbol that may have more than one exit.
- Example values from lecture (A=10, B=20, K=5, SALES=10000):

| Condition | Answer |
|-----------|--------|
| If (A = B)? | No |
| If (B > A)? | Yes |
| If (K <= 25)? | Yes |
| If (SALES >= $500,000)? | Yes |

**Card: Simple If**
- "If we have a code that we sometimes want to execute and sometimes we want to skip we can use
  if statement."
- "If this condition is true, statement is executed. If it is false, statement is ignored (not
  executed) and the program continues right after this conditional structure."

Pseudocode example — display "hundred" if num_1 equals 100:
```
1. Begin
2. Prompt user for num_1
3. Get num_1
4. If (num_1=100)
     Display hundred
   EndIf
5. End
```

**Card: If-Else Statement**
Structure:
```
If (condition)
  Statement1
Else
  Statement2
EndIf
```

Pseudocode example — output the greater of num_1 and num_2:
```
1. Begin
2. Prompt user for num_1, num_2
3. Get num_1, num_2
4. If (num_1 > num_2)
     Display num_1
   Else
     Display num_2
   EndIf
5. End
```

**Card: Nested If Statement**
- "By using nested if, it is possible to combine several conditions."
- "Only the statements following the first condition that is found to be true will be executed,
  all other statements will be skipped."
- "The statements of the final Else will be executed if none of the conditions are true."

Structure:
```
If (condition1)
  -- statements
elsIf (condition2)
  -- more statements
elsIf (condition3)
  -- more statements
...
elseIf (condition n)
  -- statement n
Else
  -- other statements
EndIf
```

Pseudocode example — student grade based on degree:
```
1. Begin
2. Prompt user to enter student's degree
3. Read grade
4. If student's degree is greater than or equal to 80
     Write "A"
   elseIf student's degree is greater than or equal to 70
     Write "B"
   elseIf student's degree is greater than or equal to 50
     Write "C"
   else
     Write "F"
   EndIf
5. End
```

---

### §7 — Repetition (LEC7_092645.pdf)

**Card: Introduction**
- "Many problems require that steps be repeated."
- "This is commonly known as looping, repetition or iteration."
- "It is called looping because logically it forms a loop as instructions are executed one after
  the other in the forward direction then control jumps back to the start of the loop."
- To perform repetition successfully, two things are needed:
  1. The instructions that are to be repeated
  2. When to stop looping
- Three loop constructs:
  1. The Pre-Test Loop (while loop)
  2. The Post-Test Loop (do while loop)
  3. Counted Loops (for loop)

**Card: Pre-Test Loop (while loop)**
- "The key feature of the pre-test loop is that we test to see whether or not to continue before
  executing the body of the loop. The effect of this is that we might not execute the body at all."
- Use when the body may need to execute **0 or more times**

Structure:
```
While (condition)
  Statement
  …
  Statement
EndLoop
```

**Card: Post-Test Loop (do while loop)**
- "If we don't test to determine whether or not to continue until after we've executed the block,
  the loop body will always be executed at least once. This distinguishes it from the pre-test loop."
- Use when the body must execute **at least once**

Structure:
```
Do
  Statement
  …
  Statement
While (condition)
```

**Card: Counted Loop (for loop)**
- "For loop allows a statement to be executed a specified number of times."
- Begins with a loop control variable assigned a specific initial value
- The control variable is incremented (or decremented) by a specified amount each iteration
  until a terminating value is reached
- "For loop is a very powerful tool to use with arrays (a topic covered later)."
- "This loop is a specialized construct for iterating a specific number of times, often called
  a 'counted loop'."

Structure:
```
For initial value to final value
  Statements
  UpdateStatement
EndLoop
```

**Card: Example — Output numbers 1 to 10**
Show all three loop types (from lecture):

While loop:
```
1. Begin
2. Set 1 to i
3. While (i <= 10)
     Display i
     i ← i + 1
   EndLoop
4. End
```

Do-While loop:
```
1. Begin
2. Set 1 to i
3. Do
     Display i
     i ← i + 1
   While (i <= 10)
4. End
```

For loop:
```
1. Begin
2. For i = 1 to 10
     Display i
     i ← i + 1
   EndLoop
3. End
```

---

### §8 — Accumulator and Counter (LEC8_092725.pdf)

**Card: Introduction**
- "We have two common operations served by repetition structures: Counting operations and
  Accumulating operations."

**Card: Counting**
- "The counting is a very important operation in programming."
- Uses of counting: perform calculations (e.g. averaging), determine when to stop looping
- "Counting is accomplished in logic by defining a variable and adding or subtracting a value
  to/from the variable during each repetition loop."
- "If you add to the counter on each loop, the counter value increases (incrementing)."
- "If we subtract on each loop, we count down (decrementing) with the counter."
- "We can count by ones or by larger numbers."

**Card: Counting — Example 1**
```
1. Begin
2. Set 0 to count
3. Set 0 to countDown
4. Set 0 to countByFive
5. While count <= 10
     count equals count + 1
     countDown equals countDown – 1
     countByFive equals countByFive + 5
   EndLoop
6. Display count, countDown, countByFive
7. End
```

**Card: Counting — Example 2**
"Write pseudocode and draw flowchart to Count the number of four items weighting over 20 kg."
```
1. Begin
2. Set 0 to count
3. Set 0 to cntover
4. While (count < 4)
     Get num
     If (num > 20)
       cntover ← cntover + 1
     EndIf
     count ← count + 1
   EndLoop
5. Display "Number Over 20:" cntover
6. End
```

**Card: Accumulating**
- "With accumulation, an accumulator variable is designated to accumulate numbers in a variable."
- "Instead of incrementing a counter variable by a set number, we will be taking some value or
  identifier and add this to the accumulator variable on each repetition."
- "The effect is that the accumulator variable grows (summarizes) on each pass of the loop."
- Counter vs Accumulator distinction:
  - **Counter:** increments by a fixed set number each loop
  - **Accumulator:** adds a varying value (an identifier/input) each loop

Note from lecture: The PDF shows a pseudocode and flowchart example of calculating a test average
of five test scores using both a counter and accumulator. If the full pseudocode is visible in the
PDF, include it here verbatim.

---

## Lec2 Java Note (in Java Summary tab, top of §11 Loops)

Add a small note card at the very top of the §11 Loops section in the existing `#summary` div:

> **Note:** This section covers content from both **Java Lecture 1** and **Java Lecture 2**.
> Java Lecture 2 is a reinforcement of loop structures (while, do-while, for, nested loops,
> break, continue) with additional examples. All loop content is consolidated here.

---

## Practice Exam Expansion

Add **new questions** to the Practice Exam tab, replace the old ones
Use the same HTML structure as the existing 4 questions.
Questions must be drawn strictly from lecture content. Suggested questions:

Section 1: 80 Multiple Choice Questions
Which logical unit of the computer is capable of performing computations and making logical decisions?
 a) Input Unit b) Output Unit c) Arithmetic and Logic Unit (ALU) d) Memory Unit
Which device is considered hardware?
 a) Operating System b) Keyboard c) Java Program d) Compiler
The unit that obtaining information from various input devices is the:
 a) Memory Unit b) Output Unit c) Input Unit d) CPU
Which memory is volatile and stores your program and data while you are using the computer?
 a) ROM b) RAM c) Secondary Storage d) Hard Disk
Which unit takes processed information and makes it available outside the computer?
 a) ALU b) CPU c) Output Unit d) Input Unit
Secondary storage devices include which of the following?
 a) RAM b) Cache c) Magnetic disks d) CPU
The "opcode" in a machine language instruction tells the computer:
 a) The memory address of the data b) The name of the programmer c) The operation to be performed d) The speed of the processor
Programs written in 1s and 0s are in which language?
 a) Assembly language b) High-level language c) Machine language d) Pseudocode
A program that translates high-level code as a complete unit is a(n):
 a) Interpreter b) Compiler c) Assembler d) Linker
Which language uses symbolic names for opcodes and operands?
 a) Machine language b) C++ c) Assembly language d) Java
Languages closest to computer hardware are called:
 a) High-level languages b) Low-level languages c) Object-oriented languages d) Compiled languages
Which of the following is an example of an Operating System?
 a) MS-DOS b) JAVA c) COBOL d) BASIC
Programs written to perform particular tasks required by users are:
 a) System software b) Application software c) Machine language d) Translators
What is the most important type of system software?
 a) Word Processor b) Spreadsheet c) Operating system d) Game
What is the first step in the Program Development Life Cycle?
 a) Problem Analysis b) Coding c) Problem Definition d) Algorithm design
The stage involving breaking a problem into smaller and simpler sub-problems is:
 a) Problem Definition b) Problem Analysis c) Debugging d) Translation
An "Algorithm" is defined as:
 a) A computer language b) A clear and unambiguous specification of steps to solve a problem c) A physical part of the computer d) A syntax error
The process of fixing errors or "bugs" in a program is called:
 a) Analyzing b) Debugging c) Compiling d) Running
A syntax error, such as a missing semicolon, is a:
 a) Runtime error b) Logic error c) Compile-time error d) System error
An infinite loop is typically an example of a:
 a) Syntax error b) Compile-time error c) Runtime error d) Hardware error
A value that never changes during program execution is a:
 a) Variable b) Constant c) Method d) Statement
Which rule applies to naming variables?
 a) Can start with a number b) Can contain spaces c) Must start with a letter d) Can use dashes
Which tool graphically represents the logic in a solution?
 a) Pseudocode b) Flowchart c) Compiler d) Java Virtual Machine
In pseudocode, which keyword is used for input from the keyboard?
 a) Print b) Display c) Get d) Prompt
The pseudocode keyword "Prompt" is used to:
 a) Receive data b) Output data c) Explain what variable should be input d) Perform arithmetic
Which symbol is used for the modulus operation in pseudocode?
 a) / b) * c) % d) +
In a flowchart, what does the rectangle symbol represent?
 a) Decision b) Input/Output c) Process d) Terminal
The diamond symbol in a flowchart indicates a:
 a) Terminal b) Decision c) Data flow d) Predefined process
Which symbol marks the beginning or end of a flowchart?
 a) Process symbol b) Terminal symbol c) Connector symbol d) Annotation symbol
What is the only flowchart symbol that can have more than one exit arrow?
 a) Process b) Input c) Decision d) Terminal
Branching statements allow a program to:
 a) Repeat code b) Redirect the flow of execution c) Define variables d) Delete data
Which relational operator means "not equal"?
 a) == b) ≠ c) >= d) <=
The Simple If statement executes a block ONLY if the condition is:
 a) False b) True c) Infinite d) Signed
Which structure is used to combine several different conditions?
 a) Simple If b) Nested If c) While loop d) Terminal symbol
Iteration is another word for:
 a) Branching b) Repetition c) Selection d) Debugging
A "Pre-Test" loop tests the condition:
 a) After the body executes b) During the body execution c) Before the body executes d) Only once
Which loop is guaranteed to execute at least once?
 a) While loop b) Do-while loop c) For loop d) Nested loop
A "Counted Loop" is generally implemented as a:
 a) While loop b) Do-while loop c) For loop d) Simple If
Adding a value to a counter on each loop is called:
 a) Decrementing b) Accumulating c) Incrementing d) Branching
An accumulator variable is used to:
 a) Count loop passes b) Summarize growing values c) Terminate a loop d) Name constants
Java was originally developed by:
 a) Microsoft b) Sun Microsystems c) IBM d) Apple
Which Java edition is used for web applications?
 a) Java SE b) Java ME c) Java EE d) JavaFX
Java is platform-independent because it compiles into:
 a) Machine code b) Assembly c) Bytecode d) Pseudocode
The entry point for every Java program is the:
 a) Main method b) Class constructor c) System class d) Compiler
Which character marks the end of a Java statement?
 a) : b) ; c) . d) ,
In Java, which data type is used to store text?
 a) int b) float c) String d) char
Single-line comments in Java start with:
 a) /* b) // c) # d) --
Which keyword creates a constant/read-only variable in Java?
 a) static b) const c) final d) void
Automatic conversion of a smaller type to a larger type (e.g., int to double) is:
 a) Narrowing casting b) Widening casting c) Manual casting d) Concatenation
Narrowing casting in Java must be done:
 a) Automatically b) Manually c) By the JRE d) Using the + operator
Which operator returns the division remainder?
 a) / b) % c) * d) ++
The "equal to" comparison operator in Java is:
 a) = b) == c) === d) equals
The logical "AND" operator is represented by:
 a) || b) ! c) && d) &
Which String method converts a string to all capital letters?
 a) toUpper() b) toUpperCase() c) length() d) concat()
The switch statement selects one of many:
 a) Variables b) Loops c) Code blocks d) Flow lines
In a switch statement, which keyword runs if there is no match?
 a) break b) else c) default d) continue
Which statement is used to skip one iteration of a loop?
 a) break b) exit c) continue d) stop
A byte data type can store numbers from:
 a) -128 to 127 b) 0 to 255 c) -32,768 to 32,767 d) -100 to 100
Which Java loop is often called a "counted loop"?
 a) while b) do-while c) for d) simple if
What is "bytecode" executed by?
 a) The CPU directly b) The Java Virtual Machine (JVM) c) The Compiler d) The Hard Disk
The diamond symbol in flowcharts is the only symbol that:
 a) Has no exit arrow b) Is used for Start c) May have more than one exit arrow d) Represents a process
The process of testing the condition after executing the loop body is called:
 a) Pre-Test b) Post-Test c) Logic Test d) Compilation
"Set total to 0" in pseudocode is an example of:
 a) Output b) Initialization c) Decision d) Condition
Which stage of PDLC specifies inputs and outputs?
 a) Problem Definition b) Coding c) Debugging d) Repetition
A machine language instruction's "address part" specifies:
 a) The opcode b) The memory location of data c) The programmer's email d) The variable name
Operating systems like MS Windows are:
 a) Application Software b) Hardware c) System Software d) Low-level languages
Which logical operator reverses the result of a condition?
 a) && b) || c) ! d) !=
Java is case-sensitive, so "MyClass" and "myclass" are:
 a) The same b) Different c) Ignored d) Keywords
Text in Java must be wrapped in:
 a) Single quotes b) Parentheses c) Double quotes d) Curly braces
Which method prints text and adds a new line?
 a) print() b) println() c) write() d) output()
The primitive type for single characters is:
 a) String b) char c) byte d) boolean
What is the result of 7 % 3?
 a) 2 b) 1 c) 0 d) 2.33
Widening casting is done:
 a) Manually b) Automatically c) By the user d) Not at all
The break statement in a switch is used to:
 a) Start a loop b) Stop execution from "falling through" c) Exit the entire program d) Declare a default case
A "nested loop" means:
 a) A loop that never ends b) A loop inside another loop c) A loop with multiple conditions d) A loop that runs backwards
JVM stands for:
 a) Java Variable Method b) Java Virtual Machine c) Just Valid Memory d) Joint View Map
Which is NOT a primitive data type?
 a) int b) float c) String d) boolean
What happens if you forget double quotes for text in Java?
 a) It works normally b) It results in an error c) It becomes a comment d) It is ignored
How many billion devices run Java today?
 a) 1 billion b) 2 billion c) Over 3 billion d) 10 billion
The ++ operator in Java is used for:
 a) Addition b) Decrementing c) Incrementing d) Concatenation

--------------------------------------------------------------------------------
Section 2: 40 True or False Questions
Hardware is directed by software to execute commands. (True)
RAM is non-volatile memory. (False - ROM is non-volatile)
Machine language consists entirely of 1s and 0s. (True)
An assembler translates high-level languages into machine language. (False - It translates assembly)
Multitasking systems allow users to run multiple programs. (True)
Programmers start writing code immediately without a plan. (False)
Inadequate identification of a problem leads to poor performance. (True)
A variable name can start with a number. (False)
Flowcharts are generally better for larger problems than pseudocode. (False)
Pseudocode cannot be executed by a computer. (True)
The diamond symbol in a flowchart is for Input/Output. (False - It's for decisions)
The terminal symbol represents the beginning or end of a program. (True)
Branching statements allow specific code blocks to be skipped. (True)
Relational operators include things like > and <. (True)
A "Post-Test" loop executes the body at least once. (True)
Counting operations can only increment by one. (False)
Java was developed by Sun Microsystems. (True)
Every Java application must have a main() method. (True)
Curly braces {} mark the start and end of code blocks in Java. (True)
Primitive data types include String. (False - String is non-primitive)
Narrowing casting is done automatically. (False - It is manual)
The final keyword makes a variable read-only. (True)
The + operator can concatenate two strings. (True)
In a switch statement, the default keyword is required. (False - but recommended)
The break statement jumps to the next iteration of a loop. (False - it exits the loop)
"Bytecode" is platform-independent. (True)
An interpreter translates high-level code as a complete unit. (False - that is a compiler)
Arithmetic operations include addition and multiplication. (True)
The Simple If executes if a condition is false. (False)
Loops reduce errors and make code more readable. (True)
JVM stands for Java Video Library. (False)
JDK includes everything a developer needs to write Java. (True)
Java is owned by Microsoft. (False - Oracle)
double stores more precision than float. (True)
The toLowerCase() method changes text to all caps. (False)
The indexOf() method finds the position of a substring. (True)
A flowchart process symbol result in a change in information. (True)
Connector symbols serve as off-page connectors. (True)
Variables must be declared with a type before use in Java. (True)
Nested loops execute the inner loop for each outer iteration. (True)

--------------------------------------------------------------------------------
Section 3: 20 Non-Java Coding Questions (Lectures 1-8)
Write the pseudocode to find the product of three numbers (no1, no2, no3).
Write the pseudocode to find the average of three numbers (no, no2, no3).
Express a solution in human language to ask for a radius and print area.
Write pseudocode for a program that outputs "hundred" if a number equals 100.
Create a pseudocode algorithm that outputs "A" if a grade is ≥ 80, otherwise "F".
Draw the flowchart sequence to compute the sum of two numbers.
Write the pseudocode to display the multiplication table for number 4.
Write a pseudocode algorithm to calculate the sum and average of five scores.
Write a branching algorithm to output the larger of two numbers.
Design a loop in pseudocode to display numbers 1 to 10.
Write pseudocode to count how many of four items weigh over 20 kg.
Create a pseudocode structure for a nested if assigning A (≥ 80), B (≥ 70), C (≥ 50), and F.
Write pseudocode for calculating a 3% commission on costs ≥ $300.
Use pseudocode to initialize PI to 3.14 and read a radius.
Write an algorithm using a "While loop" to decrement a counter from 10 to 1.
Describe the purpose of an Annotation symbol in a flowchart.
What keyword is used in pseudocode to assign an initial value?
Write pseudocode to compute Celsius from Fahrenheit (C=(F−32)/1.8).
Write pseudocode to read ten numbers and find their total using iteration.
Describe the difference in logic flow between a While and a Do-While pseudocode construct.

--------------------------------------------------------------------------------
Section 4: 30 "Hard" Java Questions (Java Fundamentals)
What is the exact signature of the entry point method in a Java application?
Explain why System.out.println(Hello); produces an error.
How does the JVM enable platform independence for Java programs?
Define the difference in functionality between the JDK and the JRE.
What is the memory size and numerical range of the short data type?
Why must narrowing casting be done manually with parentheses?
Explain the result of int x = 9; double y = x; and name the process.
In a switch statement, what happens if the break statement is omitted?
How many decimal digits of precision does a double provide?
What is the difference between System.out.print() and System.out.println()?
Which primitive type is the most common for storing whole numbers?
Describe the rules for naming a variable in Java.
Explain the functionality of the default keyword in a switch statement.
What is the specific return value type of comparison operators?
Write the code for a nested if statement checking if a number is both positive and greater than 10.
How do you find the total number of characters in a String object?
Explain the behavior of a do-while loop when the condition is false from the start.
Identify the three parts of a for loop header and their purposes.
What is "Type Casting" in the context of primitive data types?
Which built-in String method is used to compare content instead of memory address?
Write a code snippet to convert "Java Programming" to all lowercase.
What suffix is required for a floating-point literal in Java (e.g., 5.99)?
Explain the difference between the operators & and &&.
How many times will a nested loop run if the outer runs twice and the inner runs three times?
What happens to the decimal portion of a double when cast to an int?
Which data type is used to store values with only two possible states?
Explain the use of the continue keyword inside a repetition structure.
What is the purpose of the Scanner class in Java input?
Why is Java considered an Object-Oriented Programming (OOP) language?
What error occurs if the class name does not match the filename in Java?

--------------------------------------------------------------------------------
Answersheet
MCQ Answers
c | 2. b | 3. c | 4. b | 5. c | 6. c | 7. c | 8. c | 9. b | 10. c
b | 12. a | 13. b | 14. c | 15. c | 16. b | 17. b | 18. b | 19. c | 20. c
b | 22. c | 23. b | 24. c | 25. c | 26. c | 27. c | 28. b | 29. b | 30. c
b | 32. b | 33. b | 34. b | 35. b | 36. c | 37. b | 38. c | 39. c | 40. b
b | 42. c | 43. c | 44. a | 45. b | 46. c | 47. b | 48. c | 49. b | 50. b
b | 52. b | 53. c | 54. b | 55. c | 56. c | 57. c | 58. a | 59. c | 60. b
c | 62. b | 63. b | 64. a | 65. b | 66. c | 67. c | 68. b | 69. c | 70. b
b | 72. b | 73. b | 74. b | 75. b | 76. b | 77. c | 78. b | 79. c | 80. c
True/False Answers
T | 2. F | 3. T | 4. F | 5. T | 6. F | 7. T | 8. F | 9. F | 10. T
F | 12. T | 13. T | 14. T | 15. T | 16. F | 17. T | 18. T | 19. T | 20. F
F | 22. T | 23. T | 24. F | 25. F | 26. T | 27. F | 28. T | 29. F | 30. T
F | 32. T | 33. F | 34. T | 35. F | 36. T | 37. T | 38. T | 39. T | 40. T
Coding Answers (Non-Java)
Begin -> Get no1, no2, no3 -> prod = no1 * no2 * no3 -> Display prod -> End
Begin -> Get no, no2, no3 -> sum = no+no2+no3 -> avg = sum/3 -> Display avg -> End
If (num = 100) Display "hundred" EndIf
If grade >= 80 Write "A" Else Write "F" EndIf
For i = 1 to 10 Display 4 * i EndLoop
Set num to 1 -> While num <= 10 Display num -> num = num + 1 EndLoop
If degree >= 80 Write "A" elseIf degree >= 70 Write "B" elseIf degree >= 50 Write "C" Else Write "F" EndIf
C = (F - 32) / 1.8
Set total to 0 -> Set count to 1 -> While count <= 10 -> Get num -> total = total + num -> count = count + 1 EndLoop
Hard Java Answers
public static void main(String[] args)
It lacks double quotes; Java thinks Hello is a variable name.
It creates universal bytecode that runs on any OS's JVM.
Because it converts a larger type to smaller, risking data loss (truncation).
9.0; Widening casting.
Fall-through: code continues to execute the next case.
15 to 16 decimal digits.
It will execute exactly once before stopping.
Init (runs once), Condition (checked before), Update (after execution).
.equals()
f (e.g., 5.99f).
6 times (2∗3).
It is truncated (deleted).
It organizes design around "objects" (data/behavior) rather than just logic.
A compile-time error occurs.


---

## Verification Plan

### Manual
- Open the file in a browser; default tab should be **Course Summary**.
- Click each tab: Course Summary, Java Summary, Practice Exam, Java Tutorials, Java Compiler —
  all should switch correctly.
- Confirm the existing Java Summary content (§1–§12) still renders correctly under the renamed tab.
- Confirm the Lec2 note card appears at the top of §11.
- Confirm all 8 theory sections appear in the Course Summary tab with correct content and styling.
- Confirm 20 new Practice Exam questions appear with correct structure.

### Content Check
- Every definition in §1–§8 must match the wording in the corresponding lecture PDF.
- Pseudocode blocks must use `<pre><code>` and match the lecture exactly (including step numbers,
  arrows ←, and indentation).
- No content should appear that is not sourced from the uploaded lecture PDFs.
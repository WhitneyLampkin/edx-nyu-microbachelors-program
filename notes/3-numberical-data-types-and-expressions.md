# Lecture 3: Numerical Data Types and Arithmetic Expressions

[[_TOC_]]

## Introduction
- Three fundamental constructs of programming languages
    - Data (built-in types)
        - int
        - float
        - bool
        - str
        - list
        - tuple
        - dict
        - ***Programmer defined types
    - Expressions
        - I/O expressions
        - Assignment expressions
        - Boolean expressions
    - Control Flow
        - Sequential
        - Branching
            - if
            - if/else
            - if/elif/else
        - Iterative
            - while
            - for
        - Function calls
        - Exceptions

## The _int_ Data Type
- Kind of data: integer numbers (pos & neg)
- Inner representation inside of memory?
    - 26 (base 10) = 11010 (base 2)
    - What about -26?
- Approaches to represent signed numbers in binary (0s & 1s)
    - Sign and Magnitude: First bit on the left represents the sign and the rest the actual number
        - This isn't how programming languages do it
    - Two's Complement
        - In a k-bit two's complement representation of a number
            - Positive int is (k-1)-bit unsigned binary representation, padded with a 0 to its left
            - Negative int: 2^k - additive inverse = neg int
                - sum of a neg `int` and its additive inverse is 2^k
                - 2^k = 2^8 = 100000000
- **Summary**: Inner representation of `int` numbers use the 2's complement method.

### Python Literals
- Forms of Data
    - Variables = x, y,...
        - Assigned values
    - Python Literals = 6, -6, 7.3, "abc",...
        - No definition needed
    - Data assignments: Variable = Python literal

### Python Arithmetic Operators
- +, -, *, /, **, //, %
- Exponents: 10^2=100 would be written as 10**2=10 in Python
- Remainders: 
    - Ex. 13/5 = 2R3
        - 13 div 5 = 2
            - Python: 13//5
        - 13 mod 5 = 3
            - Python: 13%5
- Unlike other programming languages, Python allows // and % for float numbers.

### Summary
**Kind of data**: Integer numbers

**Inner representation**: The numbers are represented in memory using the 2's complement method.

**Python literals**: 3, 4, -6, 3954,...

**Arithmetic Operators**: +, -, *, /, **, // (div), % (mod)

## The _float_ Data Type
- Python accepts both 8.9753-3 and 0.008975 for float numbers

### Summary
**Kind of data**: Real numbers (includes decimals and fractions)

**Inner representation**: The float numbers are represented by the floating point method (IEEE-754).

**Python literals**: -3.4, 6.0, 0.008975, 8.9753-3,...

**Arithmetic Operators**: +,-,*,/,**,//,%,...

## Resources
1. [Wikipedia: Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Floating-point_numbers)
# Module 1: Data wrangling with Python
## Sprint 1: Python mastery
### Part 5: Calculator

For the Sprint 1 project I was supposed to create a Python package that is capable of conducting basic calculator-like functions, including:
1. Addition/ Subtraction;
2. Multiplication/ Division;
3. Taking (n) root of a number;
4. Resetting memory.

Calculator is capable of accepting both integers and float numbers.

## How to use it?

### 1. First of all let's install package.
``` shell
pip install pavadinimas
```
### 2. Import module "Calculator" from a package

```python
from taurokalkas import calc
```
### 3. Create an instance of the Calculator class:

```python
calculator = Calculator()
```

*<b>Important note</b>: By default calculator's memory is set to 0.0


<center> <h1><u> Main functions</u></center>

## Addition
To add a value to the in-memory value, use the `add(value)` method:
```python
calculator.add(5.0)
```
This will add 5.0 to the in-memory value and return the new value.

## Subtraction
To subtract a value from the in-memory value, use the `subtract(value)` method:
```python
calculator.subtract(3.0)
``` 
This will subtract 3.0 from the in-memory value and return the new value.

## Multiplication
To multiply the in-memory value by a value, use the `multiply(value)` method:
```python
calculator.multiply(4.0)
``` 
This will multiply the in-memory value by 4.0 and return the new value.

## Division
To divide the in-memory value by a value, use the `divide(value)` method:
```python
calculator.divide(2.0)
``` 
This will divide the in-memory value by 2.0 and return the new value.

## Root
To take the nth root of the in-memory value, use the `root(value)` method:
```python
calculator.root(2)
```
This will take the square root of the in-memory value and return the new value.

## Reset
To reset the in-memory value to 0.0, use the `reset()` method:
```python   
calculator.reset()
```
This will reset the in-memory value to 0.0 and return the new value.


## Example

```python
from boring_calculator import Calculator

calculator = Calculator()

calculator.add(5.0)         # returns 5.0
calculator.subtract(3.0)    # returns 2.0
calculator.multiply(4.0)    # returns 8.0
calculator.divide(2.0)      # returns 4.0
calculator.root(2)          # returns 2.0
calculator.reset()          # returns 0.0
```


<center> <h1><u> Thank you for you attention!

Have a good day!</u></center>         
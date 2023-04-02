<h1><p style="font-family: 'Brush Script MT', cursive;">Hello!</h1></p>
For the Module1 Sprint 1 project I was supposed to create a Python package that is capable of conducting basic calculator-like functions, including:
<li> Addition/ Subtraction;
<li> Multiplication/ Division;
<li> Taking (n) root of a number;
<li> Resetting memory.

<n>

<b>IMPORTANT note!</b> Calculator is capable of accepting both integers and float numbers.

## How to use it?

### 1. First of all, let's install the package.
``` shell
pip install pavadinimas
```
### 2. Import module "Calculator" from a package

```python
from TACalculator.calculator import Calculator
```
### 3. Create an instance of the Calculator class:

```python
calculator = Calculator()
```

*<b>IMPORTANT note</b>: By default calculator's memory is set to 0.0


<center> <h1><u> Main functions</u></center>

## Addition
To add a value to the in-memory value, use the `add(value)` method. This will add 12.0 to the memory value and will return the new value.
```python
calculator.add(12.0)
```


## Subtraction
To subtract a value from the in-memory value, use the `subtract(value)` method. This will subtract 5.0 from the memory value and will return the new value.
```python
calculator.subtract(5.0)
``` 


## Multiplication
To multiply the memory value by a value, use the `multiply(value)` method. This will multiply the memory value by 6.0 and will return the new value.
```python
calculator.multiply(6.0)
``` 


## Division
To divide the memory value by a value, use the `divide(value)` method. This will divide the memory value by 2.0 and will return the new value.
```python
calculator.divide(2.0)
``` 


## Root
To take the 1/nth root of the memory value, use the `root(value)` method. This will take the third level root of the memory value and will return the new value.
```python
calculator.root(3)
```

## Reset
To reset the memory value to 0.0, use the `reset()` method. This will reset the memory value to 0.0 and will return the new value.
```python   
calculator.reset()
```

## Example

```python
from calculator import Calculator

calculator = Calculator()

calculator.add(5.0)         # returns 5.0
calculator.subtract(3.0)    # returns 2.0
calculator.multiply(4.0)    # returns 8.0
calculator.divide(2.0)      # returns 4.0
calculator.root(2)          # returns 2.0
calculator.reset()          # returns 0.0
```


<center> <h2> Thank you for you attention!

Have a good day!</center>         
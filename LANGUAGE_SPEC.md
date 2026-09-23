# PradPyLang Language Specification

**Version:** 1.0.0

---

## 1. Overview

PradPyLang is an interpreted programming language implemented in Python.

PradPyLang programs use the `.prad` file extension.

Example:

```prad
show("Hello, World!")
```

---

## 2. Comments

PradPyLang supports single-line and multi-line comments.

### Single-line Comments

Single-line comments begin with `#`.

```prad
# This is a comment

show("Hello")
```

Everything from `#` until the end of the line is ignored.

### Multi-line Comments

Multi-line comments begin and end with `##`.

```prad
##
This is a
multi-line comment.
##

show("Hello")
```

Everything between the opening and closing `##` is ignored.

---

## 3. Values and Data Types

PradPyLang supports:

- Integers
- Decimal numbers
- Strings
- Booleans
- Lists
- Empty

### Integers

```prad
keep age = 18
```

### Decimal Numbers

```prad
keep price = 99.5
```

### Strings

Strings use double quotes.

```prad
keep name = "PradPyLang"
```

Supported escape sequences include:

```text
\"   Double quote
\\   Backslash
\n   New line
\t   Tab
```

### Booleans

PradPyLang uses:

```prad
yes
no
```

Example:

```prad
keep active = yes
```

### Lists

Lists use square brackets.

```prad
keep numbers = [1, 2, 3, 4, 5]
```

### Empty

`empty` represents the absence of a value.

```prad
keep value = empty
```

A task can also return `empty`:

```prad
task example() {
    return
}
```

---

## 4. Variables

Variables are declared using `keep`.

```prad
keep name = "PradPy"
keep age = 18
```

Variables can be reassigned:

```prad
age = 20
```

---

## 5. Assignment

PradPyLang supports normal and compound assignment.

### Normal Assignment

```prad
age = 20
```

### Compound Assignment

```prad
age += 1
age -= 1
age *= 2
age /= 2
```

Assignment requires an existing variable.

---

## 6. Output

The `show` statement evaluates and displays a value.

```prad
show("Hello")
show(20)
```

Variables can also be displayed:

```prad
keep name = "PradPy"
show(name)
```

The `empty` value is displayed as:

```text
empty
```

---

## Input

User input is read using the `ask()` expression.

### `ask()`

```prad
ask("prompt")
```

`ask()` displays a prompt, waits for keyboard input, and returns the entered value as a string.

Example:

```prad
keep name = ask("What is your name? ")

show("Hello, " + name)
```

### `number()`

Use `number()` to convert user input into an integer or decimal number.

```prad
keep age = number(ask("How old are you? "))
```

Examples:

```text
number("10")   → 10
number("10.5") → 10.5
```

### `boolean()`

Use `boolean()` to convert `yes` or `no` input into a boolean value.

```prad
keep answer = boolean(ask("Continue? "))

when answer {
    show("Continuing")
}
```

Accepted values:

```text
yes → true
no  → false
```

### `list()`

Use `list()` to convert comma-separated input into a list.

```prad
keep values = list(ask("Enter values: "))

show(values)
```

Example input:

```text
1, 2.5, hello, yes, no
```

produces a list containing:

```text
[1, 2.5, "hello", true, false]
```

`list()` currently supports numbers, strings, and `yes`/`no` boolean values separated by commas.

## 7. Operators

### Arithmetic Operators

| Operator | Description |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |

Example:

```prad
keep result = 10 + 5
```

### Comparison Operators

| Operator | Description |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `>=` | Greater than or equal |
| `<` | Less than |
| `<=` | Less than or equal |

Comparison expressions produce boolean values.

### Logical Operators

PradPyLang supports:

```text
and
or
not
```

Example:

```prad
keep age = 20
keep active = yes

when age >= 18 and active {
    show("Allowed")
}
```

### Unary Operators

The `not` operator can negate a boolean expression.

```prad
keep active = yes

show(not active)
```

Numeric unary operators are also supported.

---

## 8. Conditional Statements

PradPyLang provides:

- `when`
- `orwhen`
- `otherwise`

### When

```prad
when age >= 18 {
    show("Adult")
}
```

### Orwhen

```prad
when age >= 18 {
    show("Adult")
} orwhen age >= 13 {
    show("Teenager")
}
```

### Otherwise

```prad
when age >= 18 {
    show("Adult")
} otherwise {
    show("Child")
}
```

A conditional chain can contain multiple `orwhen` branches followed by an optional `otherwise` branch.

---

## 9. Repeat Loop

The `repeat` statement executes a block repeatedly.

```prad
repeat 5 {
    show("Hello")
}
```

---

## 10. Each Loop

The `each` statement iterates over a list.

```prad
keep numbers = [1, 2, 3, 4, 5]

each number in numbers {
    show(number)
}
```

The loop variable is available inside the loop body.

---

## 11. Lists

Lists are ordered collections of values.

```prad
keep numbers = [10, 20, 30]
```

### List Concatenation

The `+` operator can concatenate lists.

```prad
keep first = [1, 2]
keep second = [3, 4]

show(first + second)
```

### List Repetition

The `*` operator can repeat a list using an integer multiplier.

```prad
keep numbers = [1, 2]

show(numbers * 3)
```

### List Iteration

Lists can be processed using `each`.

```prad
each number in numbers {
    show(number)
}
```

---

## 12. Tasks

Tasks are PradPyLang's function mechanism.

A task is declared using the `task` keyword.

```prad
task greet(name) {
    show("Hello, " + name)
}
```

A task is called by its name:

```prad
greet("PradPy")
```

---

## 13. Task Parameters

Tasks can accept multiple parameters.

```prad
task add(a, b) {
    return a + b
}
```

Arguments are supplied when calling the task:

```prad
keep result = add(10, 20)
show(result)
```

The number of arguments must match the number of parameters.

---

## 14. Return

The `return` statement exits the current task and optionally provides a value.

```prad
task add(a, b) {
    return a + b
}
```

A task may also use a bare `return`:

```prad
task example() {
    return
}
```

A bare `return` produces the `empty` value.

Using `return` outside a task produces a runtime error.

---

## 15. Recursion

Tasks may call themselves recursively.

Example:

```prad
task factorial(n) {
    when n <= 1 {
        return 1
    }

    return n * factorial(n - 1)
}

show(factorial(5))
```

Output:

```text
120
```

---

## 16. Scope

Tasks create a local scope.

A task can access variables from its parent environment:

```prad
keep value = 10

task show_value() {
    show(value)
}

show_value()
```

A task can also modify an existing variable from its parent scope:

```prad
keep value = 10

task update() {
    value = 20
}

update()
show(value)
```

Variables created inside a task are local to that task.

```prad
task example() {
    keep local = 10
}

example()
```

`local` does not become available outside the task.

Local variables can shadow variables from a parent scope.

---

## 17. Function Calls

A task call consists of a task name followed by parentheses containing zero or more arguments.

```prad
greet()
```

or:

```prad
add(10, 20)
```

Calling an undefined task produces a runtime error.

---

## 18. Error Categories

PradPyLang separates errors into three categories.

### Lexer Errors

Lexer errors occur while converting source code into tokens.

Examples include:

- Invalid characters
- Invalid numbers
- Invalid escape sequences
- Unterminated strings
- Unterminated multi-line comments

### Parser Errors

Parser errors occur when tokens do not follow the language grammar.

### Runtime Errors

Runtime errors occur while executing a valid program.

Examples include:

- Undefined variables
- Undefined tasks
- Invalid operands
- Division by zero
- Modulo by zero
- Invalid `return`
- Incorrect task argument counts

---

## 19. Runtime Type Rules

PradPyLang validates operations at runtime.

Arithmetic operations cannot be performed on boolean values.

Ordering comparisons cannot be performed on boolean values or lists.

Invalid operations produce PradPyLang runtime errors rather than exposing Python implementation errors directly to the user.

Equality operations are supported between values.

---

## 20. Source Files

PradPyLang source files use the `.prad` extension.

Example:

```text
hello.prad
```

A program consists of a sequence of declarations and statements.

---

## 21. Complete Example

The following program combines several PradPyLang features:

```prad
keep numbers = [1, 2, 3, 4, 5]

task square(n) {
    return n * n
}

each number in numbers {
    show(square(number))
}
```

Output:

```text
1
4
9
16
25
```

---

## 22. Version

This document describes the **PradPyLang 1.0.0** language specification.

The language specification may evolve in future versions as new language features are introduced.

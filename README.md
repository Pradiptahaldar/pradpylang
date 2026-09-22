# PradPyLang

> A modern interpreted programming language built from scratch in Python.

**Version:** 1.0.0
**License:** MIT
**Repository:** https://github.com/Pradiptahaldar/pradpylang

---

## About

**PradPyLang** is a custom interpreted programming language designed and implemented from scratch in Python.

The project includes its own lexer, parser, abstract syntax tree, runtime environment, interpreter, functions/tasks, control flow, error handling, and language syntax.

PradPyLang uses the `.prad` file extension.

Example:

```prad
show("Hello, World!")
```

---

## Features

PradPyLang currently supports:

* Variables
* Integers and decimal numbers
* Strings
* Boolean values
* The `empty` value
* Lists
* Arithmetic operators
* Comparison operators
* Logical operators
* Unary operators
* Variable assignment
* Compound assignment
* Conditional statements
* `when`
* `orwhen`
* `otherwise`
* `repeat` loops
* `each` loops
* Tasks/functions
* Function parameters and arguments
* Return values
* Recursion
* Local task scope
* Parent-scope variable access
* Single-line comments
* Multi-line comments
* Runtime type validation
* Custom lexer, parser, and runtime errors

---

## Hello World

Create a file named `hello.prad`:

```prad
show("Hello, World!")
```

---

## Variables

Variables are declared using `keep`.

```prad
keep name = "PradPy"
keep age = 18

show(name)
show(age)
```

Variables can also be reassigned:

```prad
age = 20
```

Compound assignment is supported:

```prad
age += 1
age -= 1
age *= 2
age /= 2
```

---

## Conditions

PradPyLang provides `when`, `orwhen`, and `otherwise`.

```prad
keep age = 20

when age >= 18 {
    show("Adult")
} orwhen age >= 13 {
    show("Teenager")
} otherwise {
    show("Child")
}
```

---

## Loops

### Repeat

```prad
repeat 5 {
    show("Hello")
}
```

### Each

```prad
keep numbers = [1, 2, 3, 4, 5]

each number in numbers {
    show(number)
}
```

---

## Lists

Lists can be created using square brackets:

```prad
keep numbers = [10, 20, 30, 40, 50]

show(numbers)
```

Lists support concatenation:

```prad
show(numbers + [60, 70])
```

and repetition:

```prad
show(numbers * 2)
```

Lists can also be iterated with `each`:

```prad
each number in numbers {
    show(number)
}
```

---

## Tasks

Functions are called **tasks** in PradPyLang.

```prad
task greet(name) {
    show("Hello, " + name)
}

greet("PradPy")
```

Tasks can accept multiple parameters and return values:

```prad
task add(a, b) {
    return a + b
}

keep result = add(10, 20)
show(result)
```

---

## Recursion

Tasks can call themselves recursively.

```prad
task factorial(n) {
    when n <= 1 {
        return 1
    }

    return n * factorial(n - 1)
}

keep result = factorial(5)
show(result)
```

Output:

```text
120
```

---

## Comments

### Single-line comments

```prad
# This is a comment

show("Hello")
```

### Multi-line comments

```prad
##
This is a
multi-line comment.
##

show("Hello")
```

Comments are ignored by the lexer and are not executed by the interpreter.

---

## Empty Value

PradPyLang provides an `empty` value.

```prad
keep value = empty

show(value)
```

The interpreter displays:

```text
empty
```

A task can also return `empty` using a bare `return`:

```prad
task example() {
    return
}
```

---

## Operators

### Arithmetic

```text
+
-
*
/
%
```

### Comparison

```text
==
!=
>
>=
<
<=
```

### Logical

```text
and
or
not
```

### Assignment

```text
=
+=
-=
*=
/=
```

---

## Project Structure

```text
pradpylang/
│
├── examples/
│   ├── hello.prad
│   ├── variables.prad
│   ├── conditions.prad
│   ├── loops.prad
│   ├── lists.prad
│   ├── tasks.prad
│   ├── recursion.prad
│   └── comments.prad
│
├── src/
│   ├── lexer/
│   ├── tokens/
│   ├── parser/
│   ├── prad_ast/
│   ├── runtime/
│   ├── interpreter/
│   ├── errors/
│   ├── operators/
│   └── main.py
│
├── LANGUAGE_SPEC.md
├── LICENSE
└── README.md
```

---

## Running PradPyLang

At the current development stage, a `.prad` program can be executed through the Python entry point:

```bash
python src/main.py examples/hello.prad
```

For another program:

```bash
python src/main.py examples/recursion.prad
```

The project is planned to provide a dedicated `pradpy` command as part of the final CLI/package integration.

---

## Examples

The repository includes example programs demonstrating the main language features:

| Example           | Demonstrates                         |
| ----------------- | ------------------------------------ |
| `hello.prad`      | Basic output                         |
| `variables.prad`  | Variables and assignment             |
| `conditions.prad` | Conditional statements               |
| `loops.prad`      | `repeat` and `each`                  |
| `lists.prad`      | Lists and list operations            |
| `tasks.prad`      | Tasks, parameters, and return values |
| `recursion.prad`  | Recursive tasks                      |
| `comments.prad`   | Single-line and multi-line comments  |

---

## Language Specification

For the formal language syntax and specification, see:

`LANGUAGE_SPEC.md`

---

## Development

PradPyLang is implemented in Python and is structured around the major stages of an interpreter:

```text
Source Code
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
AST
    ↓
Interpreter
    ↓
Runtime
```

The project is being developed as an independent programming language and interpreter.

---

## Roadmap

The project is progressing toward a complete developer experience around PradPyLang.

Planned work includes:

* Dedicated CLI command
* Python package/installation support
* VS Code language support
* Syntax highlighting
* VS Code Run integration
* Improved developer tooling
* Documentation improvements
* Further language features

---

## Contributing

Contributions, ideas, bug reports, and discussions are welcome.

If you find an issue or have an idea for improving PradPyLang, please open an issue or submit a pull request on GitHub.

---

## License

PradPyLang is released under the **MIT License**.

See the [`LICENSE`](LICENSE) file for the complete license text.

---

## Author

**Pradipta Haldar**

GitHub: https://github.com/Pradiptahaldar

---

## Project

GitHub repository:

https://github.com/Pradiptahaldar/pradpylang

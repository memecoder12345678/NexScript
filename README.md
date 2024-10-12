# NexScript Programming Language - Introduction 🖥️

**Author:** `memecoder`

**Language:** `Python`

---

**NexScript** is a custom programming language designed for ease of use and flexibility, focusing on straightforward syntax and powerful features. Below is an overview of the language's key elements and how they work.

## Basic Syntax

NexScript supports various expressions and statements, including conditional logic, loops, function definitions, and more.

### Expressions
- **Expression Assignment**: 
  - `SET IDENTIFIER = expr` - Assigns an expression to an identifier.
- **Compound Expressions**: 
  - Supports logical operations using `AND` and `OR`.

### Built-in Function

- **ECHO**: Outputs a value or string.
- **INPUT**: Receives input from the user.
- **INPUT_INT**: Receives input as an integer.
- **INPUT_FLOAT**: Receives input as a float.
- **CLEAR**: Clears the screen.
- **IS-NUM**: Checks if a value is a number.
- **IS_STR**: Checks if a value is a string.
- **IS_LIST**: Checks if a value is a list.
- **IS_FUNC**: Checks if a value is a function.
- **APPEND**: Adds an item to a list.
- **POP**: Removes an item from a list.
- **EXTEND**: Extends a list with additional items.
- **LEN**: Gets the length of a list.
- **STR**: convert numerical formats to strings.


### Statements
- **Statement Types**: 
  - `RETURN expr` - Returns an expression if provided.
  - `CONTINUE` - Skips to the next iteration in a loop.
  - `BREAK` - Exits the loop.
  - General expression handling.

### Arithmetic Operations
- **Arithmetic Expressions**: 
  - Supports addition, subtraction, multiplication, division, and power operations.
  - Expressions are evaluated with standard operator precedence.

### Function Calls and Definitions
- **Function Definitions**: 
  - Functions can be defined with `FUNC` and can accept multiple parameters.
  - Supports returning a single expression or multiple statements within the function body.
- **Function Calls**: 
  - Functions are called by name, passing in arguments enclosed in parentheses.

### Conditional Statements
- **If Expressions**: 
  - Supports `IF`, `ELIF`, and `ELSE` for conditional logic.
  - Conditions can either be followed by a single statement or multiple statements enclosed by `END`.
- **For and While Expressions**: 
  - `FOR` loops allow iteration with an optional `STEP`.
  - `WHILE` expressions provide a mechanism for repeating code blocks based on conditions.

### Lists and Data Structures
- **List Expressions**: 
  - Lists can be defined using square brackets, containing comma-separated expressions.

### Example Code Snippets

```nexscript
SET X = INPUT_INT("Enter any integer (X): ")

$ If-else condition
IF x >= 10 THEN
  ECHO("X is greater than 10 or equal to 10")
ELIF x >= 5 THEN
  ECHO("X is greater than 5 or equal to 5")
ELSE
  ECHO("X is less than 5")
END
```

### Comment Example

```nexscript
$ This is a comment
```

## Installation

### Git and Python Installation

#### Windows
1. **Install Git**:
   - Download and install Git from the official website:
     [https://git-scm.com/](https://git-scm.com/)
2. **Install Python**:
   - Download and install Python from the official website:
     [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### Linux
1. **Install Git**:
   - Use your package manager to install Git. For example, on Debian/Ubuntu:
     ```bash
     sudo apt install git
     ```
   - On Fedora:
     ```bash
     sudo dnf install git
     ```
2. **Install Python**:
   - On Debian/Ubuntu:
     ```bash
     sudo apt install python3
     ```
   - On Fedora:
     ```bash
     sudo dnf install python3
     ```

### Cloning the Repository 
Once Git and Python are installed:

1. Open the terminal or command prompt.
2. Navigate to the directory where you want to clone the repository. For example, on Windows:
   ```cmd
   cd C:\Users\<your username>
   ```
3. Use the `git clone` command followed by the repository URL:
   ```bash
   git clone https://github.com/memecoder12345678/NexScript.git
   ```

## Running a NexScript File

To run a `.nex` file, you can use the `NexRun` script. Follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the project directory. For example, on Windows:
   ```bash
   cd C:\Users\<yourusername>\NexScript\NexScript
   ```
3. Run the following command:
   ```bash
   python NexRun.py path\to\your\file.nex
   ```

Where:
- `NexRun.py` is the script that interprets and runs your NexScript programs.
- `path\to\your\file.nex` is the path to the NexScript file you want to execute.
---
NexScript provides an intuitive and powerful way to build programs with a focus on readability and simplicity. This language is ideal for both beginners and advanced users looking for a flexible scripting solution. You can also refer to the `grammar.txt` file for more details on the language's grammar and syntax 📝🚀

---
If you have any questions, please contact us via email at: [memecoder17@gmail.com](mailto:memecoder17@gmail.com)
---


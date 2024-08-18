## NexScript Programming Language - Introduction 🖥️

**NexScript** is a custom programming language designed for ease of use and flexibility, focusing on straightforward syntax and powerful features. Below is an overview of the language's key elements and how they work.

### Basic Syntax

NexScript supports various expressions and statements, including conditional logic, loops, function definitions, and more.

#### Statements
- **Newline Handling**: Statements can be separated by newlines. Multiple statements can be written with newlines in between.
- **Statement Types**: 
  - `RETURN expr` - Returns an expression if provided.
  - `CONTINUE` - Skips to the next iteration in a loop.
  - `BREAK` - Exits the loop.
  - General expression handling.

#### Expressions
- **Expression Assignment**: 
  - `SET IDENTIFIER = expr` - Assigns an expression to an identifier.
- **Compound Expressions**: 
  - Supports logical operations using `AND` and `OR`.

#### Arithmetic Operations
- **Arithmetic Expressions**: 
  - Supports addition, subtraction, multiplication, division, and power operations.
  - Expressions are evaluated with standard operator precedence.

#### Function Calls and Definitions
- **Function Definitions**: 
  - Functions can be defined with `FUNC` and can accept multiple parameters.
  - Supports returning a single expression or multiple statements within the function body.
- **Function Calls**: 
  - Functions are called by name, passing in arguments enclosed in parentheses.

#### Conditional Statements
- **If Expressions**: 
  - Supports `IF`, `ELIF`, and `ELSE` for conditional logic.
  - Conditions can either be followed by a single statement or multiple statements enclosed by `END`.
- **For and Loop Expressions**: 
  - `FOR` loops allow iteration with an optional `STEP`.
  - `LOOP` expressions provide a mechanism for repeating code blocks based on conditions.

#### Lists and Data Structures
- **List Expressions**: 
  - Lists can be defined using square brackets, containing comma-separated expressions.

### Example Code Snippets

```nexscript
$ Define x with an initial value
SET x = 15

$ If-else condition
IF x > 10 THEN
  ECHO("X is greater than 10")
ELIF x > 5 THEN
  ECHO("X is greater than 5 but less than or equal to 10")
ELSE
  ECHO("X is 5 or less")
END
```
### Comment Example

```nexscript
$ This is a comment
```

## Installation

Ensure that you have `Python` and `Git`.

1. **Clone the repository**:
    - Open command prompt.
    - Use the `git clone` command followed by the repository URL:
    ```sh
    git clone https://github.com/memecoder12345678/NexScript.git
    ```

3. **Navigate to the project directory**:
    ```sh
    cd NexScript\NexScript
    ```
## Running a NexScript File

To run a `.nex` file, follow these steps:

1. **Open `shell.py` in the `NexScript\NexScript` directory**:
    ```sh
    python shell.py
    ```

2. **Enter the path to your `.nex` file**:
    After running `shell.py`, you can execute your NexScript file by simply typing the path to the file with the `.nex` extension in the NexShell.

    Example:
    ```sh
    path\to\your\file.nex
    ```

    Where:
    - `shell.py` is the script that interprets and runs your NexScript programs.
    - `path\to\your\file.nex` is the path to the NexScript file you want to execute.

  By following these steps, your `.nex` script will be processed and executed by the NexScript interpreter.

---

NexScript provides an intuitive and powerful way to build programs with a focus on readability and simplicity. This language is ideal for both beginners and advanced users looking for a flexible scripting solution.

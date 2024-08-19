## NexScript Programming Language - Introduction 🖥️

**NexScript** is a custom programming language designed for ease of use and flexibility, focusing on straightforward syntax and powerful features. Below is an overview of the language's key elements and how they work.

### Basic Syntax

NexScript supports various expressions and statements, including conditional logic, loops, function definitions, and more.

#### Statements
- **Newline Handling**: Statements can be separated by newlines. Multiple statements can be written with newlines characters `;` or `\n` in between.

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

- **Comment Usage**: Comments in NexScript must be placed at the beginning of a line. Avoid using comments in the same line as code, especially when using newline characters `\n` or semicolons `;`.



## Installation

Ensure that you have `Python` and `Git`.

**Clone the repository**:
- Open command prompt.
**NOTE**: It is advisable to clone the repository into a default or standard directory to avoid potential issues. For example, you might choose `Documents` or a similar directory.
- Navigate to the directory where you want to clone the repository. For example:
  ```cmd
  cd C:\Users\<your username>
  ```
- Use the `git clone` command followed by the repository URL:
  ```cmd
  git clone https://github.com/memecoder12345678/NexScript.git
  ```

## Running a NexScript File

To run a `.nex` file, you can use the `NexRun` script. Follow these steps:

**Using NexRun to execute a `.nex` file**:
- Open command prompt.
1. Navigate to the project directory.
  ```cmd
  cd C:\Users\<your username>\NexScript\NexScript
  ```
2. Enter the path to your `.nex` file:
  ```cmd
  python NexRun.py path\to\your\file.nex
  ```

  Where:
  - `NexRun.py` is the script that interprets and runs your NexScript programs.
  - `path\to\your\file.nex` is the path to the NexScript file you want to execute.

By following these steps, your `.nex` script will be processed and executed by the NexScript interpreter.

.

### ⚠️ Platform Compatibility Warning

- **Current Support**: NexScript is currently only available for Windows.

- **Upcoming Support**: A Linux version is planned for future release.

- **No macOS Support**: There are no plans to support macOS at this time.

--- 

NexScript provides an intuitive and powerful way to build programs with a focus on readability and simplicity. This language is ideal for both beginners and advanced users looking for a flexible scripting solution. You can also refer to the `grammar.txt` file for more details on the language's grammar and syntax 📝🚀

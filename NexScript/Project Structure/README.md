# Project Structure

```plaintext
Repository
 ├── NexScript/
 │    ├── grammar/
 │    │   └── grammar.txt
 │    ├── test/
 │    │   ├── README.md
 │    │   ├── test-1.nex
 │    │   ├── test-2.nex
 │    │   └── test-3.nex
 │    ├── Project Structure/
 │    │   └── README.md
 │    ├── docs/
 │    │   ├── Code-of-Conduct.md
 │    │   └── Contributing.md
 │    ├── NexRun.py
 │    ├── NexScript.py
 │    ├── shell.py
 │    └── strings_error.py
 └── README.md

```

## **Repository**
This is the root directory of the NexScript project, containing all the necessary files and folders for the project. It includes:

- **NexScript/**: The main directory for the NexScript source code and related files.
  - **grammar/**: Contains the syntax definition for the NexScript language.
    - `grammar.txt`: Defines the grammar rules for NexScript. This text file describes how various elements of the language (e.g., expressions, statements, loops) are defined and how they should behave during interpretation or compilation.
  
  - **test/**: Holds test files to ensure the NexScript code functions correctly.
    - `README.md`: Documentation providing guidance on how to perform the tests in this folder.
    - `test-1.nex`, `test-2.nex`, `test-3.nex`: Test files written in NexScript to verify different language features. These files likely contain different test cases for debugging and feature verification.

  - **Project Structure/**: This folder contains documentation that explains the project's structure, helping other developers understand the organization.
    - `README.md`: Describes the structure and organization of the NexScript project, providing guidelines for key directories and files.

  - **docs/**: Contains documentation related to project guidelines and rules for contributors.
    - `Code-of-Conduct.md`: Describes the expected behavior for contributors to maintain a friendly and professional work environment.
    - `Contributing.md`: Provides instructions on how to contribute to the project, including details on pull requests, reporting bugs, or suggesting new features.

  - **NexRun.py**: The main execution file for NexScript. This Python script is responsible for reading and executing NexScript code from `.nex` files. Running this file will execute the commands written in NexScript.

  - **NexScript.py**: This file likely contains the core interpreter for NexScript. It handles the syntax and semantics defined in `grammar.txt`, making the language run by interpreting the code.

  - **shell.py**: Provides a command-line interface (CLI) or shell for NexScript, allowing users to input commands directly and see results immediately. It's a useful tool for quick development and testing.

  - **strings_error.py**: Contains error definitions or handling routines. When errors occur during NexScript execution, this file provides messages that help developers understand the problem.

- **README.md**: This file is located at the root of the repository. It typically serves as the entry point for anyone visiting the repository, offering an overview of the project, installation instructions, usage guidelines, and contribution information.


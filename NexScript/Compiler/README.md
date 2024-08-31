# nex2exec.py

`nex2exec.py` is a tool for compiling NexScript code into executable files for operating systems such as macOS, Windows, and Linux with x86_64 architecture. This tool uses PyInstaller for the compilation process.

## Features

- **Supported Operating Systems**:
  - macOS
  - Windows
  - Linux

- **Supported Architecture**:
  - x86_64
  - **Note**:
      - To create files for operating          systems with architectures different from x86_64, you will need to build a bootloader tailored to the architecture of that operating system

## Installation

Before using `nex2exec.py`, make sure that PyInstaller is installed. You can install PyInstaller by running:

```bash
pip install pyinstaller
```

**Note:** If you prefer to use a different compiler instead of PyInstaller, you can modify the compiler in the `nex2exec` source code. However, ensure that the compiler you choose is correctly installed and configured.

## Usage

To compile NexScript code, use the following command:

```bash
python nex2exec.py <file.nex>
```

where `<file.nex>` is the NexScript source file you want to compile into an executable.

## Example

Suppose you have a NexScript source file named `example.nex`. To compile this file into an executable, run the following command:

```bash
python nex2exec.py example.nex
```

## Notes

- Ensure all necessary dependencies are installed.
- If you encounter errors during compilation, check the configuration and version of PyInstaller or the alternative compiler you are using.

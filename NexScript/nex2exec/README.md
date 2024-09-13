# nex2exec.py

`nex2exec.py` is a tool designed to convert NexScript code into executable files for various operating systems, including macOS, Windows, and Linux, with x86_64 architecture. This tool utilizes PyInstaller for the compilation process.

## Features

- **Supported Operating Systems**:
  - macOS
  - Windows
  - Linux

- **Supported Architecture**:
  - x86_64

- **Note**: For creating executables for operating systems with architectures other than x86_64, you will need to develop a bootloader specific to the architecture of the target operating system.

## Installation

Before using `nex2exec.py`, ensure that PyInstaller is installed. You can install PyInstaller with the following command:

```bash
pip install pyinstaller
# or pip3 install pyinstaller
```

**Note:** If you prefer using a different compiler instead of PyInstaller, you can modify the conversion process in the `nex2exec.py` source code. Ensure that the chosen compiler is properly installed and configured.

## Usage

To convert NexScript code, use the following command:

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

- Ensure that all necessary dependencies are installed.
- If you encounter errors during compilation, check the configuration and version of PyInstaller or the alternative compiler you are using.

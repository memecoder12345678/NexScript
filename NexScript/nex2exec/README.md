# nex2exec.py

`nex2exec.py` is a tool designed to convert NexScript code into executable files for various operating systems, including macOS, Windows, and Linux, with x86_64 architecture. This tool supports both PyInstaller and Nuitka for the compilation process.

## Features

- **Supported Operating Systems**:
  - macOS
  - Windows
  - Linux

- **Supported Architecture**:
  - x86_64

- **Note**: For creating executables for operating systems with architectures other than x86_64, you will need to develop a bootloader specific to the target operating system's architecture.

## Installation

Before using `nex2exec.py`, ensure that either PyInstaller or Nuitka is installed. You can install them using the following commands:

### Install PyInstaller

```bash
pip install pyinstaller
# or pip3 install pyinstaller
```

### Install Nuitka

```bash
pip install nuitka
# or pip3 install nuitka
```

**Note:** If you prefer to use a different compiler instead of PyInstaller or Nuitka, you can modify the conversion process in the `nex2exec.py` source code. Ensure that the chosen compiler is properly installed and configured.

## Usage

To convert NexScript code, use the following command:

```bash
python nex2exec.py <compiler> <file.nex>
```

where:
- `<compiler>` can be `--pyinstaller` or `--nuitka` to specify which compiler to use.
- `<file.nex>` is the NexScript source file you want to compile into an executable.

## Example

Suppose you have a NexScript source file named `example.nex`. To compile this file into an executable using PyInstaller, run the following command:

```bash
python nex2exec.py --pyinstaller example.nex
```

To compile this file using Nuitka, run the following command:

```bash
python nex2exec.py --nuitka example.nex
```

## Notes

- Ensure that all necessary dependencies are installed.
- If you encounter errors during compilation, check the configuration and version of PyInstaller or Nuitka, or the alternative compiler you are using.

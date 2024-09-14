# nex2exec (v1.2.0, September 2024, 23:34)
import os
import sys
import random
version = sys.version_info
if version.major == 3 and version.minor == 12:
    pass
else:
    print(f"Error: Python 3.12 is required. Current version is {version.major}.{version.minor}.{version.micro}")
    exit(1)
tempfile = "tempfile[" + str(random.randint(0, 9999999999)) + "].py"
def clear_code(code):
    cleaned_lines = []
    inside_string = False
    for line in code.splitlines():
        new_line = ""
        for char in line:
            if char == '"' and not inside_string:
                inside_string = True
            elif char == '"' and inside_string:
                inside_string = False
            if char == '$' and not inside_string:
                break
            new_line += char
        if new_line.strip():
            cleaned_lines.append(new_line)
    return "\n".join(cleaned_lines)
def main():
    global tempfile
    if len(sys.argv) != 3:
        print("Usage: python nex2exe.py <compiler> <file_name.nex>")
        print("Compiler options: '--pyinstaller' or '--nuitka'")
        return
    compiler = sys.argv[1].lower()
    file_name = sys.argv[2]
    if not file_name.endswith('.nex'):
        print("Error: The file must have a .nex extension")
        return
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found")
        return
    if compiler not in ['--pyinstaller', '--nuitka']:
        print("Error: Compiler must be '--pyinstaller' or '--nuitka'")
        return
    try:
        with open(file_name, 'r') as file:
            code = file.read()
        code_clean = clear_code(code)
        filename = os.path.basename(file_name)
        code_in_file = f"""
import NexScript
text = '''
{code_clean}
'''
result, error = NexScript.run('{filename}', text)
if error:
    if hasattr(error, 'as_string'):
        print(error.as_string())
    else:
        print(error)
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))
"""
        with open(tempfile, "w") as f:
            f.write(code_in_file)
        print("The program is being compiled...")
        if compiler == '--pyinstaller':
            rs = os.system(f"pyinstaller --onefile --name {filename.replace('.nex', '')} {tempfile}")
        elif compiler == '--nuitka':
            rs = os.system(f"nuitka --standalone --onefile --output-dir=dist {tempfile}")
        if rs == 0:
            print("The program has been compiled successfully!")
            if os.name == 'nt':
                print(f"The executable file is located in the 'dist' subdirectory of the Compiler directory: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', filename.replace('.nex', '.exe'))}")
            else:
                print(f"The executable file is located in the 'dist' subdirectory of the Compiler directory: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', filename.replace('.nex', ''))}")
        else:
            print("An error occurred during compilation!")
            return
        try:
            if os.path.exists(tempfile):
                os.remove(tempfile)
        except Exception as e:
            print(f"Error: Unable to delete the temporary file: {e}")
            return
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")
        return 
if __name__ == "__main__":
    main()

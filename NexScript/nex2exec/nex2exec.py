# nex2exec (v1.3.0, September 2024, 23:34)
import sys
import os
import uuid
import random
import time
import hashlib
tempfile = f'tempfile[{hashlib.sha256((str(random.randint(0, 10**40)) + str(uuid.uuid4()) + str(time.time())).encode()).hexdigest()}].py'
def clear_code(code):
    cleaned_lines = []
    inside_string = False
    for line in code.splitlines():
        new_line = ''
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
    return '\n'.join(cleaned_lines)
def main():
    global tempfile
    if len(sys.argv) != 3:
        print('Usage: python nex2exe.py <compiler> <file_name.nex>')
        print("Compiler options: '--pyinstaller' or '--nuitka'")
        return
    compiler = sys.argv[1].lower()
    file_name = sys.argv[2]
    if not file_name.endswith('.nex'):
        print('Error: The file must have a .nex extension')
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
        with open(tempfile, 'w') as f:
            f.write(code_in_file)
        print('The program is being compiled...')
        if compiler == '--pyinstaller':
            rs = os.system(f'pyinstaller --onefile --name {filename[:-4]} {tempfile}')
        elif compiler == '--nuitka':
            rs = os.system(f'nuitka --standalone --onefile --output-file={filename[:-4]} --output-dir=dist {tempfile}')
        if rs == 0:
            print('The program has been compiled successfully!')
            if os.name == 'nt':
                print(f"The executable file is located in the 'dist' subdirectory of the Compiler directory: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', filename[:-4] + '.exe')}")

            else:
                print(f"The executable file is located in the 'dist' subdirectory of the Compiler directory: {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', filename[:-4])}")
        else:
            print('An error occurred during compilation!')
            return
        try:
            if os.path.exists(tempfile):
                os.remove(tempfile)
        except Exception as e:
            print(f'Error: Unable to delete the temporary file: {e}')
            return
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")
        return 
if __name__ == '__main__':
    main()

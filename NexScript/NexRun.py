import NexScript
import sys
import os
def clear(text):
    lines = text.splitlines()
    filtered_lines = [line for line in lines if not line.strip().startswith('$')]
    return '\n'.join(filtered_lines)
def main():
    if len(sys.argv) != 2:
        print("Usage: python NexRun.py <file_name.nex>")
        return
    file_name = sys.argv[1]
    if not file_name.endswith('.nex'):
        print("Error: The file must have a .nex extension")
        return
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found")
        return
    try:
        with open(file_name, 'r') as file:
            code = file.read()
        code_clean = clear(code)
        result, error = NexScript.run(file_name, code_clean)
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
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")
        return 
if __name__ == "__main__":
    main()
import NexScript
import sys
import os
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
    if len(sys.argv) != 2:
        print('Usage: python NexRun.py <file_name.nex>')
        return
    file_name = sys.argv[1]
    if not file_name.endswith('.nex'):
        print('Error: The file must have a .nex extension')
        return
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found")
        return
    try:
        with open(file_name, 'r') as file:
            code = file.read()
        if clear_code(code).strip() == '':
            print('Error: The file is empty')
            return
        result, error = NexScript.run(file_name, code)
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
    except Exception as e:
        print(f'An error occurred: {e}')
        return
if __name__ == '__main__':
    main()

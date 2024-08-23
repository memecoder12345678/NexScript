import NexScript
print('NexScript (v1.5.0, Aug 21 2024, 15:24:32)\nTIP: Use command "EXIT" to exit.')
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
while True:
    text = input('>>> ')
    text = clear_code(text)
    if text.strip() == "": continue
    if text == "EXIT": break
    result, error = NexScript.run('<stdin>', text)
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

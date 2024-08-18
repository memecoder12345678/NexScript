import NexScript
while True:
    text = input('>>> ')
    if text.strip() == "": continue
    result, error = NexScript.run('<stdin>', text)
    if '$' in text:
        lines = text.splitlines()
        filtered_lines = [line for line in lines if '$' not in line]
        text = '\n'.join(filtered_lines)
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

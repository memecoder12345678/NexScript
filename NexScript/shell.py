import NexScript
while True:
    text = input('>>> ')
    if '$' in text:
        lines = text.splitlines()
        filtered_lines = [line for line in lines if '$' not in line]
        text = '\n'.join(filtered_lines)
    if not text.split(): pass
    else: 
        result, error = NexScript.run('<stdin>', text)
        if error: print(error.as_string())
        else: print(result)

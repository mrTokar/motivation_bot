
def parce_blocks(filename: str, sep_line: str):
    """Return text between `sep_line`"""
    with open(filename, encoding="utf-8") as file:
        text = ''
        for line in file:
            if (line == sep_line + '\n') or (line == sep_line and text):
                yield text
                text = ''
            else:
                text += line
        yield text


if __name__ == "__main__":
    for block in parce_blocks('test.txt', '---'):
        print('Block:')
        print(block, end='')
        print('===')
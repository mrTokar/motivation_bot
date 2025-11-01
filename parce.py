
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
        if text: yield text


def get_messages(filename: str, sep_line: str):
    """Return cortege (id, meassage) from `filename` separated by `sep_line`"""
    with open(filename, encoding="utf-8") as file:
        vk_id = None
        message = ""
        for line in file:
            if (line.strip().isdigit()):
                vk_id = int(line.strip())
            elif (line == sep_line + '\n') or (line == sep_line):
                if vk_id is not None:
                    yield vk_id, message.strip()
                vk_id = None
                message = ""
            else:
                message += line
        if vk_id is not None: yield vk_id, message.strip()  


if __name__ == "__main__":
    for vk_id, mes in get_messages('source\\motivational_messages.txt', '================================================================================'):
        print("User:", vk_id)
        print("Message:", mes)
        print("-----")
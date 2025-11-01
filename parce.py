import json

def get_messages_from_json(filename:str):
    """Return cortege (id, meassage) from `filename` in json format"""
    with open(filename, encoding="utf-8") as file:
        json_data = json.load(file)
    for key, value in json_data.items():
        yield int(key), value

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
   for vk_id, text in get_messages_from_json("source\motivational_messages.json"):
       print(f"{vk_id}\n{text}\n---")

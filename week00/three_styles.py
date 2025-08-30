def exists_1(target: str, data: str) -> bool:
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def exists_2(target: str, data: str) -> bool:
    result = False
    for i in range(len(data)):
        if data[i] == target:
            result = True
            break
    return result


def exists_3(target: str, data: str) -> bool:
    found = False
    i = 0
    while not found and i < len(data):
        found = data[i] == target
        i += 1
    return found


def exists_4(target: str, data: str) -> bool:
    if target is None:
        raise ValueError("Argument 'target' cannot be None")
    if len(data) is None:
        raise ValueError("Argument 'data' cannot be None")
    if not isinstance(data, list):
        raise ValueError("Argument 'data' must be a list")
    if len(data) == 0:
        raise ValueError("List 'data' cannot be empty")
    found = False
    i = 0
    while not found and i < len(data):
        found = data[i] == target
        i += 1
    return found

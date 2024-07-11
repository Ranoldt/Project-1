def read_calls(file: open) -> {(str, str): int}:
    call_dict = {}
    for line in file:
        line = line.strip().split(':')
        for val in line[1:]:
            call_tuple = (line[0], val)
            if call_tuple in call_dict:
                call_dict[call_tuple] += 1
            else:
                call_dict[call_tuple] = 1
    return call_dict


def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    call_dict = {}
    for call in calls:
        if call[0] in call_dict:
            call_dict[call[0]][call[1]] = calls[call]
        else:
            call_dict[call[0]] = {call[1]: calls[call]}
    return call_dict

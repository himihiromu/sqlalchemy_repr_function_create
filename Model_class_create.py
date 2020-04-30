def create_model(string_list):
    file_line = []
    variable_list = []
    class_name = ""
    for s in string_list:
        tmp_str = s.split()
        if not tmp_str:
            continue
        if tmp_str[0] == "from":
            file_line.append(s[:-1])
        elif tmp_str[0] == "import":
            file_line.append(s[:-1])
        elif tmp_str[0] == "class":
            if variable_list:
                file_line.extend(init_create(variable_list))
                file_line.extend(repr_create(class_name, variable_list))
            class_name = tmp_str[1].split('(')[0]
            file_line.append('\n')
            file_line.append(s)
            variable_list = []
        else:
            file_line.append(s[:-1])
            variable_list.append(tmp_str[0])

    file_line.extend(init_create(variable_list))
    file_line.extend(repr_create(class_name, variable_list))
    return file_line


def init_create(string_list):
    ans_list = ["\n\tdef __init__(self"]
    for s in string_list:
        ans_list[0] += ", " + s
        ans_list.append("\t\tself." + s + " = " + s)
    ans_list[0] += '):'
    return ans_list


def repr_create(class_name, string_list):
    ans_list = ["\n\tdef __repr__(self):", "\t\treturn "]
    ans_list[1] += '"<' + class_name + '(' + "='%s', ".join(string_list) + "='%s')>" + '" % ('
    ans_list[1] += "self." + ", self.".join(string_list)
    ans_list[1] = ans_list[1][:-2] + ')'
    return ans_list


if __name__ == "__main__":
    file_name = input("ファイル名：")
    with open(file_name) as rf:
        sl = rf.readlines()
        change_text = create_model(sl)

    with open(file_name, mode='w') as wf:
        wf.write('\n'.join(change_text))
        wf.write('\n')

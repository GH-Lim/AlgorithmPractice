def is_num(f_arg):
    for char in f_arg:
        if not (ord('0') <= ord(char) <= ord('9')):     # compare with ASCII
            return False
    return True


def is_alph(f_arg):
    for char in f_arg:
        if not (ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')):
            return False
    return True


def is_valid_command(command, flag_rule):
    cur_rule = ""                                       # init current rule
    check_arg = 1                                       # check if flag has argument
    # check_flag = dict(flag_rule.keys())
    # print(check_flag)
    for i in range(1, len(command)):
        if command[i][0] != '-':                        # is not flag
            if cur_rule == "":                          # has no flag
                return False
            elif cur_rule == "NULL":                    # if NULL, next must be flags
                return False
            elif cur_rule == "NUMBER":
                if not is_num(command[i]):
                    return False
                cur_rule = ""                           # ONLY one argument follows NUMBER flag
            elif cur_rule == "NUMBERS":
                if not is_num(command[i]):
                    return False
            elif cur_rule == "STRING":
                if not is_alph(command[i]):
                    return False
                cur_rule = ""                           # ONLY one argument follows STRING flag
            elif cur_rule == "STRINGS":
                if not is_alph(command[i]):
                    return False
            check_arg = 1
            continue
        if not check_arg:
            return False                                # no argument in the previous flag
        check_arg = 0
        cur_flag = command[i]
        if cur_flag not in flag_rule:                   # invalid flag
            return False
        if cur_flag in flag_rule:
            rule = flag_rule[cur_flag]
            if rule == "STRING" or rule == "STRINGS" or rule == "NUMBER" or rule == "NUMBERS":
                if i + 1 >= len(command):               # no next arg
                    return False
            if rule == "NULL":
                check_arg = 1
            cur_rule = rule
    return True


def solution(program, flag_rules, commands):
    answer = []

    flag_rule_dict = dict()                             # dict to save flag rules
    flag_alias_dict = dict()                            # dict to save flag alias
    for flag_rule in flag_rules:
        flag_rule_split = flag_rule.split()             # split by space (' ')
        if len(flag_rule_split) == 2:
            flag_name, flag_argument_type = flag_rule_split
            flag_rule_dict[flag_name] = flag_argument_type  # save flag rule
        if len(flag_rule_split) == 3:
            nickname, alias, origin = flag_rule_split
            flag_alias_dict[nickname] = origin

    for command in commands:
        command_split = command.split()                 # split by space (' ')
        if len(command_split) < 1:
            answer.append(False)
            continue
        if program != command_split[0]:
            answer.append(False)                        # first arg is program name
            continue                                    # if False, check next arg
        if not is_valid_command(command_split, flag_rule_dict):
            answer.append(False)
            continue
        answer.append(True)
    return answer

solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"])
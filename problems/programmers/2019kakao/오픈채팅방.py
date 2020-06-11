def solution(record):
    logs = []
    users = {}
    for log in record:
        comm = log.split()
        if comm[0] == 'Enter':
            _, u_id, name = comm
            users[u_id] = name
            logs.append([u_id, 0])
        elif comm[0] == 'Leave':
            _, u_id = comm
            logs.append([u_id, 1])
        else:
            _, u_id, name = comm
            users[u_id] = name
    answer = []
    for log in logs:
        u_id, com = log
        if com:
            answer.append(f'{users[u_id]}님이 나갔습니다.')
        else:
            answer.append(f'{users[u_id]}님이 들어왔습니다.')
    return answer
def solution(record):
    answer = []
    users = {}
    for log in record:
        comm = log.split()
        if comm[0] == 'Enter':
            _, u_id, name = comm
            users[u_id] = name
            answer.append(f'{name}님이 들어왔습니다.')
        elif comm[0] == 'Leave':
            _, u_id = comm
            answer.append(f'{users[u_id]}님이 나갔습니다.')
            users.pop(u_id)
        else:
            _, u_id, name = comm
            users[u_id] = name
    return answer
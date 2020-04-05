def solution(directory, command):
    answer = []

    for comm in command:
        comm = comm.split()
        if comm[0] == 'mkdir':
            directory.append(comm[1])
        elif comm[0] == 'cp':
            temp = []
            for dir in directory:
                if dir[:len(comm[1])] == comm[1]:
                    sub_dir = comm[1].split('/')
                    temp.append(dir[len(comm[1]) - len(sub_dir[-1]):])
            if comm[2] == '/':
                for dir in temp:
                    directory.append('/' + dir)
                continue
            for dir in temp:
                directory.append(comm[2] + '/' + dir)
        elif comm[0] == 'rm':
            idx = 0
            while idx < len(directory):

                if directory[idx][:len(comm[1])] == comm[1]:
                    del directory[idx]
                    continue
                idx += 1
    answer = directory
    answer.sort()
    return answer

d = [
"/",
"/hello",
"/he/llo",
"/hello/tmp",
"/root",
"/ro/ot",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
c = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

solution(d, c)
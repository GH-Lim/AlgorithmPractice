def solution(dataSource, tags):
    answer = []

    tag_dict = {}
    for data in dataSource:
        for i in range(1, len(data)):
            if data[i] not in tag_dict:
                tag_dict[data[i]] = {data[0]}
            else:
                tag_dict[data[i]].add(data[0])
    temp = {}
    for tag in tags:
        for data in tag_dict[tag]:
            if data not in temp:
                temp[data] = 1
            else:
                temp[data] += 1
    temp = temp
    temp = [[k, -v] for k, v in sorted(temp.items(), key=(lambda x:x[1]))]
    temp = sorted(temp, key=(lambda x:x[1]), reverse=True)
    temp = reversed(temp)
    answer = [k for k, v in temp]
    return answer


d = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
t = ["t1", "t2", "t3"]

solution(d, t)
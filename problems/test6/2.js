function solution(arr) {
  const ana = arr.reduce((acc, cur, i) => {
    let a = cur.toString().split("").sort().join("");
    acc.push(a);
    return acc;
  }, []);
  const result = [...new Set(ana)];
  return result.length;
}
console.log(solution([112, 1814, 121, 1481, 1184])); // 2
console.log(solution([123, 456, 789, 321, 654, 987])); // 3
console.log(solution([1, 2, 3, 1, 2, 3, 4])); // 4
console.log(solution([123, 234, 213, 432, 234, 1234, 2341, 12345, 324])); // 5

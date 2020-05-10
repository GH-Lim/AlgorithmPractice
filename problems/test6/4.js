function solution(weights) {
  let arr = weights.map((e) => [e, 1]);
  arr.sort((a, b) => a[0] - b[0]);
  let flag = true;
  while (flag) {
    flag = false;
    let i = 1;
    while (i < arr.length) {
      if (arr[i - 1][0] === arr[i][0]) {
        arr.splice(i - 1, 2, [arr[i][0] * 2, arr[i - 1][1] + arr[i][1]]);
        arr.sort((a, b) => a[0] - b[0]);
        flag = true;
      } else {
        i++;
      }
    }
  }
  arr.sort((a, b) => b[1] - a[1]);
  return arr[0][1];
}

console.log(solution([2, 2, 2, 2, 3, 3, 5, 6])); // 4
console.log(solution([3, 3, 3, 3, 3, 3, 12])); // 5
console.log(solution([16, 16, 16, 16, 16, 16, 16, 16, 1, 1, 2, 4, 4])); // 8
console.log(solution([1])); // 1

function solution(arr) {
  var answer = 0;
  while (arr.length !== 1 || arr[0] !== 1) {
    let cnt = 1;
    let temp = 1001;
    let tempArr = [];
    arr.forEach((e) => {
      if (temp === 1001) {
        temp = e;
      } else {
        if (e === temp) {
          cnt += 1;
        } else {
          tempArr.push(cnt);
          cnt = 1;
          temp = e;
        }
      }
    });
    tempArr.push(cnt);
    answer += 1;
    arr = tempArr;
  }
  return answer;
}

console.log(solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3])); // 6
console.log(solution([1, 2, 3])); // 3
console.log(solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2])); // 5
console.log(solution([2])); // 1
console.log(solution([1])) // 0


function solution(reqs) {
  let answer = [];
  const reqMap = reqs.map((e) => {
    return e.split(" ");
  });
  let accounts = {};
  for (const req of reqMap) {
    if (req[0] === "CREATE") {
      if (accounts[req[1]]) {
        answer.push(403);
      } else {
        accounts[req[1]] = {
          limit: -req[2],
          cash: 0,
        };
        answer.push(200);
      }
    } else if (req[0] === "DEPOSIT") {
      if (accounts[req[1]]) {
        accounts[req[1]]["cash"] += parseInt(req[2]);
        answer.push(200);
      } else {
        answer.push(404);
      }
    } else {
      if (accounts[req[1]]) {
        if (accounts[req[1]]) {
          if (accounts[req[1]]["cash"] - req[2] < accounts[req[1]]["limit"]) {
            answer.push(403);
          } else {
            accounts[req[1]]["cash"] -= req[2];
            answer.push(200);
          }
        }
      } else {
        answer.push(404);
      }
    }
  }
  return answer;
}

console.log(
  solution([
    "DEPOSIT 3a 10000",
    "CREATE 3a 300000",
    "WITHDRAW 3a 150000",
    "WITHDRAW 3a 150001",
  ])
);
// [404, 200, 200, 403]
console.log(
  solution(["CREATE 3a 10000", "CREATE 3a 20000", "CREATE 2bw 30000"])
);
// 	[200, 403, 200]

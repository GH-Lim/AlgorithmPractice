function solution(s) {
  let answer = [];
  const s_list = s.replace('{{', '').replace('}}', '').split('},{')
  let obj = {}
  s_list.forEach(e => {
    let num_list = e.split(',')
    obj[num_list.length] = num_list
  });
  let prev = []
  for (let i = 0; i < s_list.length; i++) {
    answer.push(parseInt(obj[i + 1].filter(x => !prev.includes(x))))
    prev = obj[i + 1]
  }
  return answer;
}


console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
/*
// 이렇게 풀 수도 있구나..
function solution(s) {
  return JSON.parse(s.replace(/{/g, '[').replace(/}/g, ']'))
  .sort((a, b) => a.length - b.length)
  .reduce((arr, v, n) => {
      if (n) {
          return arr.concat(v.filter(f => !arr.includes(f)));
      }
      return v;
  }, []);
}
*/
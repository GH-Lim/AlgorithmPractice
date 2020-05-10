function solution(str1, str2) {
  const corr = 65536
  str1 = str1.toUpperCase()
  str2 = str2.toUpperCase()
  const arr1 = devide(str1)
  const arr2 = devide(str2)
  arr1.sort()
  arr2.sort()
  let intersection = arr1.reduce((acc, cur, i) => {
    if (arr2.includes(cur)) {
      acc.push(cur)
      arr2.splice(arr2.indexOf(cur), 1)
    }
    return acc
  }, [])
  let union = arr1.concat(arr2)
  if (union.length === 0) {
    return corr
  }
  return parseInt(intersection.length / union.length * corr);
}
function devide(str) {
  return str.split('').reduce((acc, cur, i) => {
    // if (/[A-Z]/.test(cur)) {
    //   if (acc.length === 0 || acc[acc.length - 1].length === 2) {
    //     acc.push(cur)
    //   } else if (i === str.length - 1) {
    //     acc[acc.length - 1] += cur
    //   } else {
    //     acc[acc.length - 1] += cur
    //     acc.push(cur)
    //   }
    // } else {
    //   if (acc[acc.length - 1].length === 1) {
    //     acc.pop()
    //   }
    // }
    // return acc
    if (i === 0) return acc
    if (/[A-Z]/.test(str[i - 1]) && /[A-Z]/.test(cur)) {
      acc.push(str[i - 1] + cur)
    }
    return acc
  },[])
}

console.log(solution("aa1+aa2", "AAAA12"));

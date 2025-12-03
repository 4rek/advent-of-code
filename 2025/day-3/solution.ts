function findTwoMaximums(str: string) {
    let max = "0";
    let max2 = "0";

    for (let ch of str.trim()) {
      const idx = str.indexOf(ch)

      if (ch > max && idx < str.length - 1) {
        max = ch
        max2 = "0"
      } else if(ch > max2) {
        max2 = ch
      }
    }

    return [max, max2]
}

export function partOne(data: string[]): number {
  return data.map(line => {
    const maximums = findTwoMaximums(line);
    return Number(maximums[0] + maximums[1])
  }).reduce((sum, i) => sum + i, 0)
}

function getLargest12Numbers(str: string) {
  const n = str.length;
  const keep = 12;
  const toRemove = n - keep;
  
  const chars = str.trim().split('');
  const result = [];
  let removed = 0;
  
  for (let i = 0; i < n; i++) {
    while (result.length > 0 && 
           result[result.length - 1] < chars[i] && 
           removed < toRemove) {
      result.pop();
      removed++;
    }
    result.push(chars[i]);
  }
  
  return result.slice(0, keep).join('');
}

export function partTwo(data: string[]): number {
  return data.map(line =>Number(getLargest12Numbers(line))).reduce((sum, i) => sum + i, 0)

}

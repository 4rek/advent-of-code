export function partOne(data: string[]): number {
  const ranges = data[0].split("\n").map(range => {
    const [start, end] = range.split("-").map(Number);
    return { start, end };
  });
  
  const ids = data[1].split("\n").map(Number);
  
  let result = 0;

  for (let id of ids) {
    // Check if id falls within any range
    const inRange = ranges.some(({ start, end }) => id >= start && id <= end);
    if (inRange) {
      result += 1;
    }
  }

  return result;
}

export function partTwo(data: string[]): number {
  //  const ranges = data[0].split("\n").map(range => {
  //   const [start, end] = range.split("-").map(Number);
  //   return { start, end };
  // });
  
  // const freshIngredients = new Set<number>();

  // for (let range of ranges) {
  //   for (let i = range.start; i <= range.end; i++) {
  //     freshIngredients.add(i);
  //   }
  // }

  // return freshIngredients.size;
  const ranges = data[0].split("\n").map(range => {
    const [start, end] = range.split("-").map(Number);
    return { start, end };
  });
  
  // Sort ranges by start position
  ranges.sort((a, b) => a.start - b.start);
  
  // Merge overlapping ranges
  const merged: Array<{ start: number; end: number }> = [];
  
  for (let range of ranges) {
    if (merged.length === 0) {
      merged.push(range);
    } else {
      const last = merged[merged.length - 1];
      
      // Check if current range overlaps or is adjacent to the last merged range
      if (range.start <= last.end + 1) {
        // Merge by extending the end if necessary
        last.end = Math.max(last.end, range.end);
      } else {
        // No overlap, add as new range
        merged.push(range);
      }
    }
  }
  
  // Count total numbers across all merged ranges
  let result = 0;
  for (let range of merged) {
    result += (range.end - range.start + 1);
  }
  
  return result;
}

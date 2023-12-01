
export function partOne(data: string, chunkSize: number): number {
  const chars = data.split("");

  let counter = 0;

  for (let i = chunkSize - 1; i < chars.length; i++) {
    const substring = data.slice(i - chunkSize, i);
    const substringSet = new Set(substring.split(""));
    if (substringSet.size === chunkSize) {
      counter = i;
      break;
    }
  }

  return counter;
}
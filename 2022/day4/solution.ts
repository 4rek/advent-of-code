
export function partOne(data: string[]): number {
  return data.map(row => {
    const [x, y] = row.split(',');

    const [a, b] = x.split('-').map(Number);
    const [c, d] = y.split('-').map(Number);

    return (a <= c && b >= d) || (c <= a && d >= b) ? 1 : 0;
  }).reduce((acc: number, item: number) => acc + item, 0);
}

export function partTwo(data: string[]): number {
  return data.map(row => {
    const [x, y] = row.split(',');

    const [a, b] = x.split('-').map(Number);
    const [c, d] = y.split('-').map(Number);

    return (a <= c && b >= d) || (c <= a && d >= b) || (b >= c && d >= a) ? 1 : 0;
  }).reduce((acc: number, item: number) => acc + item, 0);
}

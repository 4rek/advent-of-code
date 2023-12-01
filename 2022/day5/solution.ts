
export function partOne(data: string[], initialStack: string[]): string {
  const stack = [...initialStack];

  data.forEach(row => {
    const instruction = row.split(' ').map(Number);

    const amount = instruction[1];
    const from = instruction[3] - 1;
    const to = instruction[5] - 1;

    const copy = stack[from];

    stack[from] = copy.slice(0, copy.length - amount);
    stack[to] = stack[to] + copy.slice(copy.length - amount, copy.length).split("").reverse().join("");
  })

  return stack.map(item => item.charAt(item.length - 1)).join("");
}

export function partTwo(data: string[], initialStack: string[]): string {
  const stack = [...initialStack];

  data.forEach(row => {
    const instruction = row.split(' ').map(Number);

    const amount = instruction[1];
    const from = instruction[3] - 1;
    const to = instruction[5] - 1;

    const copy = stack[from];

    stack[from] = copy.slice(0, copy.length - amount);
    stack[to] = stack[to] + copy.slice(copy.length - amount, copy.length);
  })

  return stack.map(item => item.charAt(item.length - 1)).join("");
}

export function partOne(data: string[]): number {
  let value = 1;

  const values: number[] = [0];

  for (let i = 0; i < data.length; i++) {
    const [command, argument] = data[i].split(" ");

    switch (command) {
      case "noop":
        values.push(value);
        break;
      case "addx":
        values.push(value);
        values.push(value);
        value += Number(argument);
    }
  }

  const indexes = [20, 60, 100, 140, 180, 220];

  return indexes.reduce((acc, index) => acc + (index * values[index]), 0);
}

export function partTwo(data: string[]): number {
  const crtRow1 = new Array(40).fill(".");
  const crtRow2 = new Array(40).fill(".");
  const crtRow3 = new Array(40).fill(".");
  const crtRow4 = new Array(40).fill(".");
  const crtRow5 = new Array(40).fill(".");
  const crtRow6 = new Array(40).fill(".");

  const crt = [
    crtRow1,
    crtRow2,
    crtRow3,
    crtRow4,
    crtRow5,
    crtRow6,
  ];

  let x = 1;

  const values: number[] = [];

  for (let i = 0; i < data.length; i++) {
    const [command, argument] = data[i].split(" ");

    switch (command) {
      case "noop":
        values.push(x);
        break;
      case "addx":
        values.push(x);
        values.push(x);
        x += Number(argument);
    }
  }

  for (let j = 1; j < values.length; j++) {
    const a = Math.floor(j / 40);
    const b = j - 1 - (a * 40);
    const v = values[j - 1]
    const sprite = [v, v + 1, v + 2];

    if (sprite.includes(b + 1)) {
      crt[a][b] = "X";
    }
  }

  const image = crt.map(row => row.join(""))

  return 321;
}


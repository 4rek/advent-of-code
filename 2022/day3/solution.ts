const priorities = {
  a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7, h: 8, i: 9, j: 10, k: 11,
  l: 12, m: 13, n: 14, o: 15, p: 16, q: 17, r: 18, s: 19, t: 20,
  u: 21, v: 22, w: 23, x: 24, y: 25, z: 26,

  A: 27, B: 28, C: 29, D: 30, E: 31, F: 32, G: 33, H: 34, I: 35, J: 36, K: 37,
  L: 38, M: 39, N: 40, O: 41, P: 42, Q: 43, R: 44, S: 45, T: 46,
  U: 47, V: 48, W: 49, X: 50, Y: 51, Z: 52
}

export function partOne(data: string[]): number {
  let score = 0;
  let sets: Set<string>[] = [];

  for (let x in data) {
    let duplicates: Set<string> = new Set();

    const sliceAt = Math.floor(data[x].length / 2);
    const firstHalf = data[x].slice(0, sliceAt);
    const secondHalf = data[x].slice(sliceAt, data[x].length);

    for (let i = 0; i <= firstHalf.length; i++) {
      if (secondHalf.includes(firstHalf[i])) {
        duplicates.add(firstHalf[i]);
      }
    }

    sets.push(duplicates);
  }

  sets.forEach(set => {
    set.forEach(i => {
      score = score + priorities[i]
    })
  });

  return score;
}

export function partTwo(data: string[]): number {
  let score = 0;
  let sets: Set<string>[] = [];

  let counter = 0;

  while (counter < data.length) {
    let duplicates: Set<string> = new Set();

    const first = data[counter];
    const second = data[counter + 1];
    const third = data[counter + 2];

    for (let i = 0; i <= first.length; i++) {
      if (second.includes(first[i]) && third.includes(first[i])) {
        duplicates.add(first[i]);
      }
    }

    sets.push(duplicates);

    counter = counter + 3;
  }

  sets.forEach(set => {
    set.forEach(i => {
      score = score + priorities[i]
    })
  });

  return score;
}

function isTreeVisible(matrix: number[][], row: number, col: number): boolean {
  const tree = matrix[row][col];

  const width = matrix[0].length;
  const height = matrix.length;

  if (row === 0 || row === height - 1 || col === 0 || col === width - 1) {
    return true; // edges always visible
  }

  const visible = [
    true, // top 0
    true, // bottom 1
    true, // left 2
    true, // right 3
  ]

  const debug = false;

  if (debug) console.log(`debugging for ${tree} at (${row},${col})`);


  // check top and bottom
  for (let i = 0; i < height; i++) {
    if (i === row) {
      continue;
    }

    if (matrix[i][col] >= tree) {
      const key = i > row ? 1 : 0;
      visible[key] = false;
    }
  }
  // check left and right
  for (let i = 0; i < width; i++) {
    if (i === col) {
      continue;
    }

    if (matrix[row][i] >= tree) {
      const key = i > col ? 3 : 2;
      visible[key] = false;
    }
  }

  return visible.filter(el => el === false).length !== 4;
}

export function partOne(data: string[]): number {
  const matrix = data.map(row => row.split("").map(Number));
  const width = matrix[0].length;
  const height = matrix.length;

  let visibleCount = 0;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      if (isTreeVisible(matrix, i, j)) {
        visibleCount += 1;
      }
    }
  }

  return visibleCount;
}

function calculateScore(matrix: number[][], row: number, col: number): number {
  const tree = matrix[row][col];
  const width = matrix[0].length;
  const height = matrix.length;

  const scores = [
    0, // top
    0, // bottom
    0, // left
    0 // right
  ];

  for (let i = (row + 1); i < height; i++) {
    scores[1] += 1;

    if (matrix[i][col] >= tree) {
      break;
    }
  }

  for (let i = (row - 1); i >= 0; i--) {
    scores[0] += 1;

    if (matrix[i][col] >= tree) {
      break;
    }
  }

  for (let i = (col - 1); i >= 0; i--) {
    scores[2] += 1;

    if (matrix[row][i] >= tree) {
      break;
    }
  }

  for (let i = (col + 1); i < width; i++) {
    scores[3] += 1;

    if (matrix[row][i] >= tree) {
      break;
    }
  }

  return scores.reduce((acc, s) => acc * s, 1);
}

export function partTwo(data: string[]): number {
  const matrix = data.map(row => row.split("").map(Number));
  const width = matrix[0].length;
  const height = matrix.length;

  let score = 0;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      const scoreForTree = calculateScore(matrix, i, j);
      score = scoreForTree > score ? scoreForTree : score;
    }
  }


  return score;
}

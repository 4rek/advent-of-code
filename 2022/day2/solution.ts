enum Score {
  Lose = 0,
  Draw = 3,
  Win = 6
}

const Figures = {
  X: {
    drawsWith: 'A',
    winsWith: 'C',
    losesWith: 'B',
    score: 1
  },
  Y: {
    drawsWith: 'B',
    winsWith: 'A',
    losesWith: 'C',
    score: 2
  },
  Z: {
    drawsWith: 'C',
    winsWith: 'B',
    losesWith: 'A',
    score: 3
  },
}

export function partOne(data: string[]): number {
  return data
    .map(item => item.split(' '))
    .map(move => {
      const [opponentsMove, myMove] = move;
      const figure = Figures[myMove];

      if (opponentsMove === figure.drawsWith) {
        return Score.Draw + figure.score;
      }

      if (opponentsMove === figure.winsWith) {
        return Score.Win + figure.score;
      };

      return Score.Lose + figure.score;
    })
    .reduce((acc, score) => acc + score, 0);
}

export function partTwo(data: string[]): number {
  return data
    .map(item => item.split(' '))
    .map(move => {
      const [opponentsMove, expectedOutcome] = move;

      switch (expectedOutcome) {
        case 'X':
          const i = Object.keys(Figures).find(i => Figures[i].losesWith === opponentsMove);
          return Score.Lose + Figures[i!].score;
        case 'Y':
          const j = Object.keys(Figures).find(i => Figures[i].drawsWith === opponentsMove);
          return Score.Draw + Figures[j!].score;
        case 'Z':
          const k = Object.keys(Figures).find(i => Figures[i].winsWith === opponentsMove);
          return Score.Win + Figures[k!].score;
      }

    })
    .reduce((acc, score) => acc + score, 0);
}

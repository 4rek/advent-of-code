type Direction = 'D' | 'U' | 'L' | 'R';

class Point {
  constructor(public x: number, public y: number) {
    this.x = x;
    this.y = y;
  }

  move(direction: Direction, steps: number) {
    switch (direction) {
      case 'D':
        this.x = this.x + steps;
        break;
      case 'U':
        this.x = this.x - steps;
        break;
      case 'L':
        this.y = this.y - steps;
        break;
      case 'R':
        this.y = this.y + steps;
    }
  }

  getCoordinates(): string {
    return `${this.x},${this.y}`;
  }

  isAdjacent(target: Point): boolean {
    if (this.x === target.x && this.y === target.y) {
      return true;
    }

    if (Math.abs(this.x - target.x) > 1 || Math.abs(this.y - target.y) > 1) {
      return false;
    }

    return true;
  }

  follow(target: Point) {
    let direction: Direction;
    let additionalDirection: Direction | null = null;

    if (this.x === target.x) {
      direction = this.y > target.y ? "L" : "R";
    } else if (this.y === target.y) {
      direction = this.x > target.x ? "U" : "D";
    } else {
      direction = this.x > target.x ? 'U' : 'D';
      additionalDirection = this.y > target.y ? "L" : "R";
    }

    this.move(direction, 1);
    if (additionalDirection) this.move(additionalDirection, 1);
  }
}

export function partOne(data: string[]): number {
  const head: Point = new Point(0, 0);
  const tail: Point = new Point(0, 0);

  const visitedPoints: Set<string> = new Set();
  visitedPoints.add(tail.getCoordinates());

  for (let i = 0; i < data.length; i++) {
    const [direction, steps] = data[i].split(" ") as [Direction, string];

    for (let j = 0; j < Number(steps); j++) {
      head.move(direction, 1);

      if (!tail.isAdjacent(head)) {
        tail.follow(head);
        visitedPoints.add(tail.getCoordinates());
      }
    }
  }

  return visitedPoints.size;
}

export function partTwo(data: string[]): number {
  const [start, end] = [0, 0];
  const head: Point = new Point(start, end);

  const tail1: Point = new Point(start, end);
  const tail2: Point = new Point(start, end);
  const tail3: Point = new Point(start, end);
  const tail4: Point = new Point(start, end);
  const tail5: Point = new Point(start, end);
  const tail6: Point = new Point(start, end);
  const tail7: Point = new Point(start, end);
  const tail8: Point = new Point(start, end);
  const tail9: Point = new Point(start, end);

  const tails: Point[] = [
    tail1,
    tail2,
    tail3,
    tail4,
    tail5,
    tail6,
    tail7,
    tail8,
    tail9
  ]

  const visitedPoints: Set<string> = new Set();
  visitedPoints.add(tails[8].getCoordinates());

  for (let i = 0; i < data.length; i++) {
    const [direction, steps] = data[i].split(" ") as [Direction, string];

    for (let j = 0; j < Number(steps); j++) {
      head.move(direction, 1);

      for (let k = 0; k < tails.length; k++) {
        const currentTail = tails[k];
        const targetToFollow = k === 0 ? head : tails[k - 1];

        if (!currentTail.isAdjacent(targetToFollow)) {
          currentTail.follow(targetToFollow);

          if (k === 8) {
            visitedPoints.add(currentTail.getCoordinates());
          }
        }
      }
    }
  }

  return visitedPoints.size;
}

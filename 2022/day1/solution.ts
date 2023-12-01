export function partOne(data: string[]): number {
  const elfCalories = data
    .map(line => line.split('\n'))
    .map(line => line.reduce((acc, calories) => acc + Number(calories), 0))
    .sort((first, second) => first < second ? 1 : -1);

  return elfCalories[0];
}

export function partTwo(data: string[]): number {
  const elfCalories = data
    .map(line => line.split('\n'))
    .map(line => line.reduce((acc, calories) => acc + Number(calories), 0))
    .sort((first, second) => first < second ? 1 : -1);

  return elfCalories[0] + elfCalories[1] + elfCalories[2];
}

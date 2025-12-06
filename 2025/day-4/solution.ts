function isRoll(str: string): boolean {
	return str === "@";
}

export function partOne(data: string[]): number {
	const grid = [data.length, data[0].length];
	let sum = 0;

	for (let y = 0; y < grid[0]; y++) {
		const row = data[y].split("");
		for (let x = 0; x < row.length; x++) {
			const item = data[y][x];

			if (!isRoll(item)) continue;

			let siblings = 0;

			const hasRowBefore = y - 1 >= 0;
			const hasRowAfter = y + 1 < grid[0];
			const hasColumnBefore = x - 1 >= 0;
			const hasColumnAfter = x + 1 <= grid[1];

			if (hasRowBefore) {
				if (isRoll(data[y - 1][x])) {
					siblings = siblings + 1;
				}
				if (hasColumnBefore && isRoll(data[y - 1][x - 1])) {
					siblings = siblings + 1;
				}
				if (hasColumnAfter && isRoll(data[y - 1][x + 1])) {
					siblings = siblings + 1;
				}
			}
			if (hasRowAfter) {
				if (isRoll(data[y + 1][x])) {
					siblings = siblings + 1;
				}
				if (hasColumnBefore && isRoll(data[y + 1][x - 1])) {
					siblings = siblings + 1;
				}
				if (hasColumnAfter && isRoll(data[y + 1][x + 1])) {
					siblings = siblings + 1;
				}
			}
			if (hasColumnBefore && isRoll(data[y][x - 1])) {
				siblings = siblings + 1;
			}
			if (hasColumnAfter && isRoll(data[y][x + 1])) {
				siblings = siblings + 1;
			}

			if (siblings < 4) {
				sum += 1;
			}
		}
	}

	return sum;
}

function generateNewGrid(
	grid: string[],
	pointsToRemove: { row: number; col: number }[],
) {
	const newGrid = grid.map((row) => row.split(""));

	pointsToRemove.forEach((point) => {
		const { row, col } = point;

		if (
			row >= 0 &&
			row < newGrid.length &&
			col >= 0 &&
			col < newGrid[row].length
		) {
			newGrid[row][col] = ".";
		}
	});

	return newGrid.map((row) => row.join(""));
}

export function partTwo(data: string[]): number {
	let sum = 0;

	let possible = true;
	let grid = data;

	while (possible) {
		let toRemove = [];

		for (let y = 0; y < grid.length; y++) {
			const row = grid[y].split("");
			for (let x = 0; x < row.length; x++) {
				const item = grid[y][x];

				if (!isRoll(item)) continue;

				let siblings = 0;

				const hasRowBefore = y - 1 >= 0;
				const hasRowAfter = y + 1 < grid.length;
				const hasColumnBefore = x - 1 >= 0;
				const hasColumnAfter = x + 1 <= grid[0].length;

				if (hasRowBefore) {
					if (isRoll(grid[y - 1][x])) {
						siblings = siblings + 1;
					}
					if (hasColumnBefore && isRoll(grid[y - 1][x - 1])) {
						siblings = siblings + 1;
					}
					if (hasColumnAfter && isRoll(grid[y - 1][x + 1])) {
						siblings = siblings + 1;
					}
				}
				if (hasRowAfter) {
					if (isRoll(grid[y + 1][x])) {
						siblings = siblings + 1;
					}
					if (hasColumnBefore && isRoll(grid[y + 1][x - 1])) {
						siblings = siblings + 1;
					}
					if (hasColumnAfter && isRoll(grid[y + 1][x + 1])) {
						siblings = siblings + 1;
					}
				}
				if (hasColumnBefore && isRoll(grid[y][x - 1])) {
					siblings = siblings + 1;
				}
				if (hasColumnAfter && isRoll(grid[y][x + 1])) {
					siblings = siblings + 1;
				}

				if (siblings < 4) {
					toRemove.push({
						row: y,
						col: x,
					});
					sum += 1;
				}
			}
		}

		if (toRemove.length > 0) {
			grid = generateNewGrid(grid, toRemove);
		} else {
			possible = false;
		}
	}

	return sum;
}

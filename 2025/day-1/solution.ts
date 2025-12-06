function rangeDial(value: number): number {
	let result = value % 100;
	if (result < 0) {
		result += 100;
	}
	return result;
}

const startingAt = 50;

export function partOne(data: string[]): number {
	let dial = startingAt;
	let sum = 0;

	for (let entry of data) {
		const [direction, value] = [entry.slice(0, 1), Number(entry.slice(1, 100))];

		dial = direction === "L" ? dial - value : dial + value;

		dial = rangeDial(dial);

		sum = dial === 0 ? sum + 1 : sum;
	}
	return sum;
}

function rangeDialWithClicks(value: number, turns: number): [number, number] {
	let crosses = turns;

	if (value > 99) {
		crosses += Math.floor(value / 100);
	} else if (value < 0) {
		crosses += Math.floor((Math.abs(value) - 1) / 100) + 1;
	}

	const finalPosition = rangeDial(value);
	return [finalPosition, crosses];
}

export function partTwo(data: string[]): number {
	let position = startingAt; // Track actual position, not wrapped
	let sum = 0;

	for (let entry of data) {
		const [direction, value] = [
			entry.slice(0, 1),
			Number(entry.slice(1, 1000)),
		];

		const oldPosition = position;
		const movement = direction === "L" ? -value : value;
		position += movement;

		// Count how many multiples of 100 we pass through or land on
		// We want the count in range (oldPosition, position] (excluding start, including end)
		let count;
		if (movement > 0) {
			// Moving right: count multiples in (oldPosition, position]
			const firstMultiple = Math.floor(oldPosition / 100) * 100 + 100;
			const lastMultiple = Math.floor(position / 100) * 100;

			if (lastMultiple >= firstMultiple) {
				count = (lastMultiple - firstMultiple) / 100 + 1;
			} else {
				count = 0;
			}
		} else {
			// Moving left: count multiples in [position, oldPosition)
			const firstMultiple = Math.ceil(position / 100) * 100;
			const lastMultiple = Math.ceil(oldPosition / 100) * 100 - 100;

			if (lastMultiple >= firstMultiple) {
				count = (lastMultiple - firstMultiple) / 100 + 1;
			} else {
				count = 0;
			}
		}

		sum += count;
	}

	return sum;
}

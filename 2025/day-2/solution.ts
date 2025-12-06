function findInvalidIds(start: string, end: string): string[] {
	const invalidIds: string[] = [];
	const startNum = parseInt(start, 10);
	const endNum = parseInt(end, 10);

	for (
		let patternLength = 1;
		patternLength <= end.length / 2;
		patternLength++
	) {
		const minPattern = Math.pow(10, patternLength - 1); // e.g., 10 for length 2
		const maxPattern = Math.pow(10, patternLength) - 1; // e.g., 99 for length 2

		for (let pattern = minPattern; pattern <= maxPattern; pattern++) {
			const patternStr = pattern.toString();
			const invalidId = patternStr + patternStr;
			const invalidIdNum = parseInt(invalidId, 10);

			if (invalidIdNum >= startNum && invalidIdNum <= endNum) {
				invalidIds.push(invalidId);
			}

			if (invalidIdNum > endNum) {
				break;
			}
		}

		if (parseInt(minPattern.toString() + minPattern.toString(), 10) > endNum) {
			break;
		}
	}

	return invalidIds;
}

function findInvalidIdsRepeated(start: string, end: string): string[] {
	const invalidIds: Set<string> = new Set();
	const startNum = parseInt(start, 10);
	const endNum = parseInt(end, 10);

	for (
		let patternLength = 1;
		patternLength <= end.length / 2;
		patternLength++
	) {
		const minPattern = Math.pow(10, patternLength - 1);
		const maxPattern = Math.pow(10, patternLength) - 1;

		for (let pattern = minPattern; pattern <= maxPattern; pattern++) {
			const patternStr = pattern.toString();

			for (let repetitions = 2; ; repetitions++) {
				const invalidId = patternStr.repeat(repetitions);
				const invalidIdNum = parseInt(invalidId, 10);

				if (invalidIdNum >= startNum && invalidIdNum <= endNum) {
					invalidIds.add(invalidId);
				}

				if (invalidIdNum > endNum) {
					break;
				}
			}

			if (parseInt(patternStr.repeat(2), 10) > endNum) {
				break;
			}
		}

		if (parseInt(minPattern.toString().repeat(2), 10) > endNum) {
			break;
		}
	}

	return Array.from(invalidIds).sort(
		(a, b) => parseInt(a, 10) - parseInt(b, 10),
	);
}

export function partOne(data: string[]): number {
	return data
		.flatMap((line) => {
			const [start, end] = line.split("-").map((s) => s.trim());
			return findInvalidIds(start, end);
		})
		.reduce((sum, id) => sum + Number(id), 0);
}

export function partTwo(data: string[]): number {
	return data
		.flatMap((line) => {
			const [start, end] = line.split("-").map((s) => s.trim());
			return findInvalidIdsRepeated(start, end);
		})
		.reduce((sum, id) => sum + Number(id), 0);
}

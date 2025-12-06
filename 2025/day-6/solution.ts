export function partOne(data: string[]): number {
	let result = 0;

	const lines = data.length;
	const operators = data[data.length - 1]
		.trim()
		.split(" ")
		.filter((n) => n.trim());
	const values = new Map<string, number[]>();

	for (let i = 0; i < lines - 1; i++) {
		const line = data[i]
			.trim()
			.split(" ")
			.filter((n) => n.trim())
			.map(Number);
		for (let idx in line) {
			const nums = values.get(idx) ?? [];
			values.set(idx, nums.concat([line[idx]]));
		}
	}

	for (let j = 0; j < values.size; j++) {
		const numbers = values.get(j.toString()) ?? [];

		if (operators[j] === "+") {
			result += numbers.reduce((acc, n) => acc + n, 0);
		}
		if (operators[j] === "*") {
			result += numbers.reduce((acc, n) => acc * n, 1);
		}
	}

	return result;
}

function getPaddedLine(line: string, separators: number[]) {
	const result: string[] = [];

	let i = 0;
	for (let s of separators) {
		result.push(line.slice(i, s));
		i = s + 1;
	}

	return result.map((r) => r.replace(/ /g, "0"));
}

export function partTwo(data: string[]): number {
	let result = 0;

	const lines = data.length;
	const operators = data[data.length - 1]
		.trim()
		.split(" ")
		.filter((n) => n.trim());

	const values = new Map<string, string[]>();

	const separators: number[] = [];

	for (let a = 0; a < data[0].length; a++) {
		if (
			data[0][a] === " " &&
			data[1][a] === " " &&
			data[2][a] === " " &&
			data[3][a] === " "
		) {
			separators.push(a);
		}
	}

	separators.push(Infinity);

	for (let i = 0; i < lines - 1; i++) {
		const paddedLine = getPaddedLine(data[i], separators);

		for (let idx in paddedLine) {
			const v = values.get(idx.toString()) ?? [];
			values.set(idx.toString(), v.concat([paddedLine[idx]]));
		}
	}

	const newValues = new Map<string, number[]>();

	for (let j = 0; j < values.size; j++) {
		const numbers = values.get(j.toString()) ?? [];
		const newNumbersMap = new Map<string, string[]>();

		for (let number of numbers) {
			const digits = number.split("");
			for (let k = 0; k < digits.length; k++) {
				const v = newNumbersMap.get(k.toString()) ?? [];
				newNumbersMap.set(k.toString(), v.concat(digits[k]));
			}
		}

		const newNumbers: number[] = [];

		for (let l = 0; l < newNumbersMap.size; l++) {
			const n = newNumbersMap
				.get(l.toString())
				?.filter((n) => n !== "0")
				.join("");
			newNumbers.push(Number(n));
		}

		newValues.set(j.toString(), newNumbers);
	}

	for (let j = 0; j < newValues.size; j++) {
		const numbers = newValues.get(j.toString()) ?? [];

		if (operators[j] === "+") {
			result += numbers.reduce((acc, n) => acc + n, 0);
		}
		if (operators[j] === "*") {
			result += numbers.reduce((acc, n) => acc * n, 1);
		}
	}

	return result;
}

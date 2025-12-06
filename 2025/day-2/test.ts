import { describe, expect, test } from "@jest/globals";
import { partOne, partTwo } from "./solution";

import { readFile } from "fs/promises";

describe("Day 2", () => {
	test("Gift Shop - Part one - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split(",");

		expect(partOne(data)).toBe(1227775554);
	});

	test("Gift Shop - Part one - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split(",");

		expect(partOne(data)).toBe(12586854255);
	});

	test("Gift Shop - Part two - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split(",");

		expect(partTwo(data)).toBe(4174379265);
	});

	test("Gift Shop - Part two - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split(",");

		expect(partTwo(data)).toBe(17298174201);
	});
});

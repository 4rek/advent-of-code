import { describe, expect, test } from "@jest/globals";
import { partOne, partTwo } from "./solution";

import { readFile } from "fs/promises";

describe("Day 5", () => {
	test("Cafeteria - Part one - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split("\n\n");

		expect(partOne(data)).toBe(3);
	});

	test("Cafeteria - Part one - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split("\n\n");

		expect(partOne(data)).toBe(577);
	});

	test("Cafeteria - Part two - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split("\n\n");

		expect(partTwo(data)).toBe(14);
	});

	test("Cafeteria - Part two - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split("\n\n");

		expect(partTwo(data)).toBe(350513176552950);
	});
});

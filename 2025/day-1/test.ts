import { describe, expect, test } from "@jest/globals";
import { partOne, partTwo } from "./solution";

import { readFile } from "fs/promises";

describe("Day 1", () => {
	test("Secret Entrance - Part one - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split("\n");

		expect(partOne(data)).toBe(3);
	});

	test("Secret Entrance - Part one - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split("\n");

		expect(partOne(data)).toBe(1007);
	});

	test("Secret Entrance - Part two - test data", async () => {
		const input: string = await readFile(__dirname + "/test-input.txt", "utf8");
		const data = input.split("\n");

		expect(partTwo(data)).toBe(6);
	});

	test("Secret Entrance - Part two - main data", async () => {
		const input: string = await readFile(__dirname + "/input.txt", "utf8");
		const data = input.split("\n");

		expect(partTwo(data)).toBe(5820);
	});
});

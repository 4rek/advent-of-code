import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

const challenge = 'Rope Bridge';

describe(`Day 9`, () => {

  test(`${challenge} - part one - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(13);
  });

  test(`${challenge} - part one`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(6284);
  });

  test(`${challenge} - part two - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input2.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(36);
  });

  test(`${challenge} - part two`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(2661);
  });
});
import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

const challenge = 'Cathode-Ray Tube';

describe(`Day 10`, () => {

  test(`${challenge} - part one - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(13140);
  });

  test(`${challenge} - part one`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(16020);
  });

  test(`${challenge} - part two - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    // expect(partTwo(data)).toBe(36);
  });

  test(`${challenge} - part two`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    // expect(partTwo(data)).toBe(2661);
  });
});
import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

const challenge = 'No Space Left On Device';

describe(`Day 7`, () => {

  test(`${challenge} - part one - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(95437);
  });

  test(`${challenge} - part one`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(1084134);
  });

  test(`${challenge} - part two - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(24933642);
  });

  test(`${challenge} - part two`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(6183184);
  });
});
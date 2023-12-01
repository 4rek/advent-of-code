import { describe, expect, test } from '@jest/globals';
import { partOne } from './solution';

import { readFile } from 'fs/promises';

const challenge = 'Tuning Trouble';

describe(`Day 6`, () => {

  test(`${challenge} - part one - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    const values = [7, 5, 6, 10, 11];

    data.forEach((item, k) => {
      expect(partOne(item, 4)).toBe(values[k]);
    });
  });

  test(`${challenge} - part one`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');

    expect(partOne(input, 4)).toBe(1480);
  });

  test(`${challenge} - part two - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    const values = [19, 23, 23, 29, 26];

    data.forEach((item, k) => {
      expect(partOne(item, 14)).toBe(values[k]);
    });
  });

  test(`${challenge} - part two`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');

    expect(partOne(input, 14)).toBe(2746);
  });
});
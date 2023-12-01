import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

describe('Day 2', () => {

  test('Rock Paper Scissors - part one - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(15);
  });

  test('Rock Paper Scissors - part one', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(9177);
  });

  test('Rock Paper Scissors - part two - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(12);
  });

  test('Rock Paper Scissors - part two', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(12111);
  });
});
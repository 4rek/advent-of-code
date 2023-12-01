import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

describe('Day 3', () => {

  test('Rucksack Reorganization - part one - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(157);
  });

  test('Rucksack Reorganization - part one', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(8123);
  });

  test('Rucksack Reorganization - part two - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(70);
  });

  test('Rucksack Reorganization - part two', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(2620);
  });
});
import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

describe('Day 6', () => {

  test('Trash Compactor - Part one - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(4277556);
  });

  test('Trash Compactor - Part one - main data', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partOne(data)).toBe(4878670269096);
  })

  test('Trash Compactor - Part two - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(3263827);
  })

  test('Trash Compactor - Part two - main data', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    expect(partTwo(data)).toBe(8674740488592);
  })
});
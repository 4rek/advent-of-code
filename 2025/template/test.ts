import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

describe.skip('Template', () => {

  test('Part one - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partOne(data)).toBe(1);
  });

  test('Part one - main data', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partOne(data)).toBe(1);
  })

  test('Part two - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partTwo(data)).toBe(2);
  })

  test('Part two - main data', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partTwo(data)).toBe(2);
  })
});
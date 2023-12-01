import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

describe('Day 1', () => {

  test('Calorie Counting - part one - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partOne(data)).toBe(24000);
  });

  test('Calorie Counting - part one', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partOne(data)).toBe(70698);
  })

  test('Calorie Counting - part two - test data', async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partTwo(data)).toBe(45000);
  })

  test('Calorie Counting - part two', async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n\n');

    expect(partTwo(data)).toBe(206643);
  })
});
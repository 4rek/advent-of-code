import { describe, expect, test } from '@jest/globals';
import { partOne, partTwo } from './solution';

import { readFile } from 'fs/promises';

const challenge = 'Supply Stacks';

describe(`Day 5`, () => {

  test(`${challenge} - part one - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    const initialStack = [
      'ZN',
      'MCD',
      'P'
    ]

    expect(partOne(data, initialStack)).toBe('CMZ');
  });

  test(`${challenge} - part one`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    const initialStack = [
      'BQC',
      'RQWZ',
      'BMRLV',
      'CZHVTW',
      'DZHBNVG',
      'HNPCJFVQ',
      'DGTRWZS',
      'CGMNBWZP',
      'NJBMWQFP'
    ]

    expect(partOne(data, initialStack)).toBe('BWNCQRMDB');
  });

  test(`${challenge} - part two - test data`, async () => {
    const input: string = await readFile(__dirname + '/test-input.txt', 'utf8');
    const data = input.split('\n');

    const initialStack = [
      'ZN',
      'MCD',
      'P'
    ]

    expect(partTwo(data, initialStack)).toBe('MCD');
  });

  test(`${challenge} - part two`, async () => {
    const input: string = await readFile(__dirname + '/input.txt', 'utf8');
    const data = input.split('\n');

    const initialStack = [
      'BQC',
      'RQWZ',
      'BMRLV',
      'CZHVTW',
      'DZHBNVG',
      'HNPCJFVQ',
      'DGTRWZS',
      'CGMNBWZP',
      'NJBMWQFP'
    ]

    expect(partTwo(data, initialStack)).toBe('NHWZCBNBF');
  });
});
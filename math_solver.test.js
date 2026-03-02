/**
 * Tests for the 1+1=x equation solver.
 * The correct answer to 1+1 is 2.
 */

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { solveOnePlusOne } = require('./math_solver');

// RED: this test should fail until implementation is correct
test('1 + 1 equals 2', () => {
  const result = solveOnePlusOne();
  assert.strictEqual(result, 2);
});

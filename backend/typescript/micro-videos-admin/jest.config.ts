/**
 * For a detailed explanation regarding each configuration property, visit:
 * https://jestjs.io/docs/configuration
 */

import type {Config} from 'jest';

const config: Config = {
  clearMocks: true,
  coverageProvider: "v8",
  "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "collectCoverageFrom": [
      "**/*.(t|j)s"
    ],
    "coverageDirectory": "../coverage",
    "testEnvironment": "node",
    setupFilesAfterEnv: ["./core/shared/infra/testing/expect-helpers.ts"],
    transform: {
      '^.+\\.(t|j)s?$': '@swc/jest',
    },
    moduleNameMapper: {
      '@core/(.*)': '<rootDir>/$1',
    },
    rootDir: './src',
    testRegex: '.*\\..*spec\\.ts$',
};

export default config;

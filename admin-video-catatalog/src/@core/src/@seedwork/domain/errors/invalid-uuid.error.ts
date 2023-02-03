export class InvalidUuidError extends Error {
  constructor(message?: 'Id must be a validd UUID') {
    super(message);

    this.name = 'InvalidUuidError';
  }
}

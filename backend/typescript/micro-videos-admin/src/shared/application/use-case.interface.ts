export interface IUseCase<Params, Result> {
  execute(params: Params): Promise<Result>;
}

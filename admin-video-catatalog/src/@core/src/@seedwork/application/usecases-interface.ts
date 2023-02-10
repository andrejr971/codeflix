export interface UseCase<Params, Response> {
  execute(data: Params): Response | Promise<Response>;
}

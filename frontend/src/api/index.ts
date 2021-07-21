import { Phrases, PhrasesResource } from './resources/phrases';

export interface ApiMiddleware {
  phrases: Phrases;
}

export class Api implements ApiMiddleware {
  private static instance: ApiMiddleware;
  public phrases = new PhrasesResource();

  private constructor() {}

  public static getInstance(): ApiMiddleware {
    if (!Api.instance) {
      Api.instance = new Api();
    }

    return Api.instance;
  }
}

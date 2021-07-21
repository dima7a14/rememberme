import { BaseResource } from "../../common";
import { Phrases } from "./types";

export interface Phrases {
  list(): Promise<Phrases.Phrase[]>;
  create(data: Omit<Phrases.Phrase, "id">): Promise<Phrases.Phrase>;
  retrieve(id: number): Promise<Phrases.Phrase>;
  partialUpdate(
    id: number,
    data: Phrases.PatchedPhrase,
  ): Promise<Phrases.Phrase>;
  destroy(id: number): Promise<void>;
}

type PathsParams =
  | Record<string, never>
  | { phrasePk: number }
  | { phrasePk: number; mentionPk: number }
  | { phrasePk: number; translationPk: number };

export class PhrasesResource extends BaseResource implements Phrases {
  private readonly rootPath = "/api/phrases/";

  private getPath(params: PathsParams): string {
    let path = this.rootPath;

    if ("phrasePk" in params) {
      path = `${path}${params.phrasePk}/`;

      if ("mentionPk" in params) {
        path = `${path}mentions/${params.mentionPk}/`;
      } else if ("translationPk" in params) {
        path = `${path}translations/${params.translationPk}/`;
      }
    }

    return path;
  }

  list(): Promise<Phrases.Phrase[]> {
    return this.get<Phrases.Phrase[]>(this.rootPath);
  }

  create(data: Omit<Phrases.Phrase, "id">): Promise<Phrases.Phrase> {
    return this.post<Phrases.Phrase, Omit<Phrases.Phrase, "id">>(
      this.rootPath,
      data,
    );
  }

  retrieve(id: number): Promise<Phrases.Phrase> {
    return this.get<Phrases.Phrase>(this.getPath({ phrasePk: id }));
  }

  partialUpdate(
    id: number,
    data: Phrases.PatchedPhrase,
  ): Promise<Phrases.Phrase> {
    return this.patch<Phrases.Phrase, Phrases.PatchedPhrase>(
      this.getPath({ phrasePk: id }),
      data,
    );
  }

  async destroy(id: number): Promise<void> {
    await this.delete(this.getPath({ phrasePk: id }));
  }
}

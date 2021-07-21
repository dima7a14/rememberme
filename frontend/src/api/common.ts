export class BaseResource {
  protected readonly defaultOptions = {
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  } as const;

  protected async get<
    R,
    P extends Record<string, unknown> = Record<string, unknown>,
  >(path: string, params?: P): Promise<R> {
    const response = await fetch(path, {
      ...this.defaultOptions,
      ...params,
      method: "GET",
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return response.json();
  }

  protected async post<
    R,
    D extends Record<string, unknown> = Record<string, unknown>,
    P extends Record<string, unknown> = Record<string, unknown>,
  >(path: string, data: D, params?: P): Promise<R> {
    const response = await fetch(path, {
      ...this.defaultOptions,
      ...params,
      method: "POST",
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return response.json();
  }

  protected async put<
    R,
    D extends Record<string, unknown> = Record<string, unknown>,
    P extends Record<string, unknown> = Record<string, unknown>,
  >(path: string, data: D, params?: P): Promise<R> {
    const response = await fetch(path, {
      ...this.defaultOptions,
      ...params,
      method: "PUT",
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return response.json();
  }

  protected async patch<
    R,
    D extends Record<string, unknown> = Record<string, unknown>,
    P extends Record<string, unknown> = Record<string, unknown>,
  >(path: string, data: D, params?: P): Promise<R> {
    const response = await fetch(path, {
      ...this.defaultOptions,
      ...params,
      method: "PATCH",
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return response.json();
  }

  protected async delete<
    R,
    P extends Record<string, unknown> = Record<string, unknown>,
  >(path: string, params?: P): Promise<R> {
    const response = await fetch(path, {
      ...this.defaultOptions,
      ...params,
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return response.json();
  }
}

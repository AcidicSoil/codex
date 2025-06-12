import type { AnyZodObject } from "zod";

import { getWeather, WeatherArgsSchema } from "./weather";

const registry: Record<string, { schema: AnyZodObject; run: (args: unknown) => Promise<string> }> = {
  get_weather: {
    schema: WeatherArgsSchema,
    run: getWeather,
  },
};

export async function dispatchToolCall(name: string, argsJson: string): Promise<string> {
  const tool = registry[name];
  if (!tool) {
    throw new Error(`Unknown tool: ${name}`);
  }
  let args;
  try {
    args = JSON.parse(argsJson);
  } catch {
    throw new Error("Arguments must be valid JSON");
  }
  const parsed = tool.schema.safeParse(args);
  if (!parsed.success) {
    throw new Error("Tool argument validation failed");
  }
  return tool.run(parsed.data);
}

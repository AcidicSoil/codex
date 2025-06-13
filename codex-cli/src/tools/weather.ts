import { z } from "zod";

export const WeatherArgsSchema = z.object({
  location: z.string(),
  unit: z.enum(["celsius", "fahrenheit"]).default("celsius"),
});

export async function getWeather(args: unknown): Promise<string> {
  const parsed = WeatherArgsSchema.safeParse(args);
  if (!parsed.success) {
    throw new Error("Invalid arguments for get_weather");
  }
  const { location, unit } = parsed.data;
  // Placeholder implementation to avoid external requests
  return `The weather in ${location} is 23\u00b0 ${unit}`;
}

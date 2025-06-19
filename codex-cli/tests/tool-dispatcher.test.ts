import { describe, it, expect } from "vitest";
import { dispatchToolCall } from "../src/tools/dispatcher";

describe("dispatchToolCall", () => {
  it("runs registered tool", async () => {
    const result = await dispatchToolCall(
      "get_weather",
      JSON.stringify({ location: "Tokyo", unit: "celsius" }),
    );
    expect(result).toMatch("Tokyo");
  });

  it("throws on unknown tool", async () => {
    await expect(
      dispatchToolCall("unknown", "{}"),
    ).rejects.toThrow("Unknown tool");
  });
});

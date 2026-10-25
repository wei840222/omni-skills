/** Decode UTF8 across input chunks; never echo invalid JSON or credentials. */
export async function readJsonStdin(input = process.stdin) {
  const decoder = new TextDecoder("utf-8", { fatal: true });
  let text = "";
  try {
    for await (const chunk of input) {
      text += decoder.decode(typeof chunk === "string" ? Buffer.from(chunk) : chunk, { stream: true });
    }
    text += decoder.decode();
    return JSON.parse(text);
  } catch {
    throw new Error("Invalid JSON stdin");
  }
}

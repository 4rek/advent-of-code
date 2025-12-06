import { open, constants } from "fs/promises";

async function writeLogs(input: string[], file: string = "/log.txt") {
	const joinedInput = input.join("\n");
	const fs = await open(__dirname + file, constants.O_RDWR, constants.O_APPEND);
	await fs.writeFile(joinedInput);
	await fs.close();
}

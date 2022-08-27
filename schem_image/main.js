#!/usr/bin/env -S node --no-warnings

import fs from "fs";
import { Schematic } from "mindustry-schematic-parser";
import { ArgumentParser } from "argparse";
import clipboard from "clipboardy";

const parser = new ArgumentParser();

parser.add_argument("--base64", "-b", {
  nargs: 1,
  type: "string",
});
parser.add_argument("-c", "--clipboard", {
  action: "store_true",
});
parser.add_argument("--file", {
  nargs: 1,
  type: "string",
  action: "store",
});
parser.add_argument("--image", "-i", {
  nargs: 1,
  type: "string",
  help: "where to output the image",
});
parser.add_argument("--rename", "-r", {
  nargs: "+",
  type: "string",
  help: "to rename the schematic, and copy the new schematic",
});
parser.add_argument("--format", "-f", {
  action: "store_true",
});

let base64;
let file;

const args = parser.parse_args();

base64 = args.base64 ? args.base64[0] : "";
file = args.file ? args.file[0] : "";

if (args.clipboard) {
  const clip = clipboard.readSync();
  if (!clip) throw new Error("clipboard empty");
  base64 = clip;
}

if (!file && !base64) {
  throw new Error("file/base64 not specified");
}

let schematic;
if (base64) {
  schematic = Schematic.decode(base64);
} else if (file) {
  const buffer = fs.readFileSync(file);
  schematic = Schematic.decode(buffer);
}

if (args.image) {
  const opacity = 0.25;
  // save a preview of the schematic
  schematic
    .render({
      background: false, // disable background
      bridges: {
        opacity: opacity,
      },
      phaseBridges: {
        opacity: opacity,
      },
    })
    .then((nodeCanvas) => nodeCanvas.toBuffer())
    .then((buffer) => fs.writeFileSync(args.image[0], buffer));
}

if (args.rename) {
  schematic.name = args.rename.join(" ");
  if (args.format) clipboard.write(`\`\`\`${schematic.encode()}\`\`\``);
  else clipboard.write(schematic.encode());
} else if (args.format) clipboard.write(`\`\`\`${schematic.encode()}\`\`\``);

console.log(schematic.name);

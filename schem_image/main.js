#!/usr/bin/env node

import fs from "fs";
import { Schematic } from "mindustry-schematic-parser";
import { ArgumentParser } from "argparse";

const parser = new ArgumentParser();

parser.add_argument("--base64", "-b", {
  nargs: 1,
  type: "string",
});
parser.add_argument("--file", "-f", {
  nargs: 1,
  type: "string",
  action: "store",
});
parser.add_argument("--image", "-i", {
  nargs: 1,
  type: "string",
  help: "where to output the image",
});

const args = parser.parse_args();
if (!args.file && !args.base64) {
  throw new Error("You must specify either a file or base64");
}

let schematic;
if (args.base64) {
  schematic = Schematic.decode(args.base64[0]);
} else {
  const buffer = fs.readFileSync(args.file[0]);
  schematic = Schematic.decode(buffer);
}
console.log(schematic.name);

if (args.image) {
  // save a preview of the schematic
  schematic
    .render({
      background: false, // disable background
    })
    .then((nodeCanvas) => nodeCanvas.toBuffer())
    .then((buffer) => fs.writeFileSync(args.image[0], buffer));
}

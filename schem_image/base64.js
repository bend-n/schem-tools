import * as fs from 'fs'
import {
  Schematic
} from 'mindustry-schematic-parser'

const base64 = process.argv.slice(2)[0]
const schematic = Schematic.decode(base64)
console.log(schematic.name)

// save a preview of the schematic
schematic
  .render({
    background: false // disable background
  })
  .then(nodeCanvas => nodeCanvas.toBuffer())
  .then(buffer => fs.writeFileSync('/tmp/mindustry_schematics/image.png', buffer))
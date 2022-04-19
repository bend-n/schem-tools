import * as fs from 'fs'
import {
    Schematic
} from 'mindustry-schematic-parser'

const file = process.argv.slice(2)[0]
const buffer = fs.readFileSync(file)
const schematic = Schematic.decode(buffer)

console.log(schematic.name)

// save a preview of the schematic
schematic
    .render({
        background: false // disable background
    })
    .then(nodeCanvas => nodeCanvas.toBuffer())
    .then(buffer => fs.writeFileSync('/tmp/mindustry_schematics/image.png', buffer))
#!/bin/python
"""purpose: convert specific image colors to json"""


from PIL import Image
import json
from argparse import ArgumentParser
from rich.console import Console
console = Console()

colors = {
    (0, 0, 255): "water",
    (178, 34, 34): "slag",
    (110, 112, 128): "additive-reconstructor",
    (110, 112, 128): "air-factory",
    (154, 149, 128): "alloy-smelter",
    (138, 144, 178): "arc",
    (78, 79, 88): "armored-conveyor",
    (176, 154, 143): "battery-large",
    (176, 185, 128): "battery",
    (152, 154, 128): "blast-drill",
    (161, 154, 159): "blast-mixer",
    (82, 82, 92): "basalt-boulder",
    (152, 154, 164): "bridge-conduit",
    (110, 112, 128): "bridge-conveyor",
    (156, 182, 164): "coal-centrifuge",
    (176, 165, 128): "combustion-generator",
    (152, 154, 164): "command-center",
    (110, 112, 128): "conduit",
    (143, 112, 128): "constructor",
    (154, 154, 164): "container",
    (78, 79, 88): "conveyor",
    (177, 135, 104): "copper-wall-large",
    (177, 135, 104): "copper-wall",
    (176, 178, 128): "core-foundation",
    (176, 182, 128): "core-nucleus",
    (176, 182, 159): "core-shard",
    (152, 154, 164): "cryofluid-mixer",
    (110, 112, 156): "cultivator",
    (123, 123, 123): "cyclone",
    (128, 112, 128): "deconstructor",
    (176, 154, 143): "differential-generator",
    (152, 154, 128): "diode",
    (168, 136, 128): "disassembler",
    (110, 112, 128): "distributor",
    (154, 159, 180): "door-large",
    (154, 159, 180): "door",
    (110, 112, 128): "duct-bridge",
    (110, 112, 128): "duct-router",
    (82, 83, 93): "duct",
    (143, 102, 91): "duo",
    (110, 112, 128): "exponential-reconstructor",
    (152, 154, 163): "force-projector",
    (123, 123, 121): "foreshadow",
    (110, 116, 128): "fuse",
    (142, 144, 154): "graphite-press",
    (110, 112, 128): "ground-factory",
    (143, 112, 128): "hail",
    (152, 146, 164): "hyper-processor",
    (169, 173, 183): "illuminator",
    (176, 136, 128): "impact-reactor",
    (110, 84, 83): "incinerator",
    (152, 154, 164): "interplanetary-accelerator",
    (110, 112, 107): "inverted-sorter",
    (110, 112, 107): "item-source",
    (110, 112, 107): "item-void",
    (110, 112, 128): "junction",
    (152, 154, 143): "kiln",
    (138, 154, 192): "lancer",
    (143, 112, 128): "large-constructor",
    (86, 86, 102): "large-logic-display",
    (152, 146, 164): "laser-drill",
    (152, 154, 128): "launch-pad",
    (136, 154, 188): "liquid-container-full.png",
    (136, 154, 188): "liquid-container",
    (176, 185, 192): "liquid-junction",
    (110, 112, 128): "liquid-router-full.png",
    (110, 112, 128): "liquid-router",
    (176, 154, 126): "liquid-source",
    (136, 154, 192): "liquid-tank-full.png",
    (136, 154, 192): "liquid-tank",
    (176, 154, 159): "liquid-void",
    (86, 86, 102): "logic-display",
    (152, 146, 164): "logic-processor",
    (152, 154, 164): "mass-driver",
    (152, 135, 108): "mechanical-drill",
    (152, 154, 143): "mechanical-pump",
    (123, 116, 119): "meltdown",
    (176, 149, 128): "melter",
    (110, 112, 128): "memory-bank",
    (110, 112, 128): "memory-cell",
    (132, 174, 144): "mender",
    (132, 174, 144): "mend-projector",
    (110, 112, 128): "message",
    (152, 146, 164): "micro-processor",
    (110, 112, 128): "multiplicative-reconstructor",
    (110, 112, 128): "multi-press",
    (110, 112, 128): "naval-factory",
    (152, 154, 164): "oil-extractor",
    (53, 53, 53): "ore-coal",
    (174, 124, 91): "ore-copper",
    (142, 133, 162): "ore-lead",
    (155, 146, 139): "ore-scrap",
    (205, 159, 207): "ore-thorium",
    (96, 107, 184): "ore-titanium",
    (176, 154, 128): "overdrive-dome",
    (176, 154, 128): "overdrive-projector",
    (110, 112, 129): "overflow-gate",
    (152, 154, 164): "parallax",
    (74, 75, 83): "payload-conveyor",
    (106, 107, 128): "payload-loader",
    (152, 141, 128): "payload-propulsion-tower",
    (110, 112, 128): "payload-router",
    (110, 112, 126): "payload-source",
    (110, 112, 123): "payload-unloader",
    (110, 112, 128): "payload-void",
    (136, 154, 192): "phase-conduit",
    (176, 154, 128): "phase-conveyor",
    (239, 201, 152): "phase-wall-large",
    (239, 201, 152): "phase-wall",
    (176, 178, 128): "phase-weaver",
    (152, 161, 164): "plastanium-compressor",
    (74, 75, 83): "plastanium-conveyor",
    (203, 216, 126): "plastanium-wall-large",
    (203, 216, 126): "plastanium-wall",
    (110, 112, 155): "plated-conduit",
    (152, 154, 164): "pneumatic-drill",
    (176, 185, 128): "power-node-large",
    (176, 185, 128): "power-node",
    (176, 154, 128): "power-source",
    (173, 149, 103): "power-void",
    (111, 128, 205): "pulse-conduit",
    (110, 112, 128): "pulverizer",
    (152, 154, 163): "pyratite-mixer",
    (110, 112, 128): "repair-point",
    (110, 154, 128): "repair-turret",
    (123, 123, 123): "ripple",
    (136, 154, 192): "rotary-pump",
    (110, 112, 128): "router",
    (110, 112, 159): "rtg-generator",
    (149, 154, 143): "salvo",
    (123, 123, 123): "scatter",
    (138, 112, 128): "scorch",
    (154, 159, 180): "scrap-wall-gigantic",
    (154, 159, 180): "scrap-wall-huge",
    (154, 159, 180): "scrap-wall-large",
    (154, 159, 180): "scrap-wall",
    (152, 154, 164): "segment",
    (152, 154, 128): "separator",
    (74, 75, 83): "shock-mine",
    (111, 112, 126): "silicon-crucible",
    (144, 145, 156): "silicon-smelter",
    # (110, 112, 128): "solar-panel-large",
    # (110, 112, 128): "solar-panel",
    # (110, 112, 128): "sorter",
    (179, 48, 48): "spawn",
    (123, 116, 123): "spectre",
    (152, 149, 164): "spore-press",
    (152, 154, 164): "steam-generator",
    (176, 178, 136): "surge-tower",
    (232, 208, 116): "surge-wall-large",
    (232, 208, 116): "surge-wall",
    (110, 112, 120): "swarmer",
    # (110, 112, 128): "switch",
    # (110, 112, 128): "tetrative-reconstructor",
    (176, 154, 128): "thermal-generator",
    (176, 146, 128): "thermal-pump",
    (110, 112, 132): "thorium-reactor",
    (128, 117, 165): "thorium-wall-large",
    (128, 117, 165): "thorium-wall",
    (154, 159, 180): "thruster",
    (78, 79, 88): "titanium-conveyor",
    (104, 116, 196): "titanium-wall-large",
    (104, 116, 196): "titanium-wall",
    (110, 116, 128): "tsunami",
    (110, 112, 126): "underflow-gate",
    (152, 154, 159): "unloader",
    (173, 157, 164): "vault",
    (136, 154, 164): "water-extractor",
    (143, 152, 143): "wave",
}


def rgb_to_hex(rgb):
    """converts rgb to hex"""
    return "#%02x%02x%02x" % tuple(rgb)


def escape(color, text):
    r, g, b = color
    return f"\u001b[1m\u001b[38;2;{r};{g};{b}m{text}"


if __name__ == "__main__":
    parser = ArgumentParser(
        "objective(c): convert specific image colors to msch")
    parser.add_argument("-i", "--image", dest="image",
                        help="image(s) to convert, when using multiple images will layer them", nargs="+")
    parser.add_argument("-o", "--output", dest="output",
                        help="output file(s)", type=str)
    parser.add_argument("-l", "--list", dest="list",
                        action="store_true", help="list all colors, and exit")
    parser.add_argument("-n", "--name", dest="name",
                        help="name to use", default="test", nargs="*")
    parser.add_argument("-d", "--description",
                        dest="description", help="description", default="testonks", nargs="*")

    args = parser.parse_args()
    args.name = " ".join(args.name)
    args.description = " ".join(args.description)

    if args.list:
        for key, item in colors.items():
            print(escape(key, f"{item}: {rgb_to_hex(key)}"))
        exit(0)
    if args.image is None:
        raise IOError("image not specified")
    if args.output is None:
        raise IOError("output not specified")

    out = {
        "name": args.name,
        "description": args.description,
        "tags": ["u"],
        "width": 0,
        "height": 0,
        "blocks": []
    }

    for i, img in enumerate(args.image):
        parsedimg = Image.open(img)
        pix = parsedimg.load()
        width, height = parsedimg.size
        if i != 0:
            if width != out["width"] or height != out["height"]:
                raise IOError("all images must be the same size!")
        out["width"] = width
        out["height"] = height
        console.log(f"working on image {i+1}: img")
        for x in range(width):
            for y in range(height):
                pixcolor = pix[x, y][:3]  # :3
                r, g, b = pixcolor
                if pixcolor in colors:
                    name = colors[pixcolor]
                    console.log(f"{name} found at {x}, {y}")
                    out["blocks"].append(
                        {
                            "type": name,
                            "x": x,
                            "y": y,
                            "rotation": 0,
                            "config": 0
                        }
                    )

    console.log(out)
    with open(args.output, "w") as f:
        json.dump(out, f)

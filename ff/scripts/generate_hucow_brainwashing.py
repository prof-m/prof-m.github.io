"""Generator for hucow_brainwashing.txt — produces a FlipFlip caption script
with randomly positioned blink/cap/bigcap commands. Re-run to regenerate with
a fresh random layout."""

import os
import random

HEADER = """setBlinkDuration 400
setBlinkDelay 150
setBlinkGroupDelay 300

setCaptionDuration 600
setCaptionDelay 200

setCountDuration 500
setCountDelay 100
setCountGroupDelay 500

storePhrase $1 MOO
storePhrase $1 moo
storePhrase $1 Moo
storePhrase $1 MOOO
storePhrase $1 mooo
storePhrase $1 MOOOO
storePhrase $1 moooo
storePhrase $1 MOOOOO
storePhrase $1 mooooo
storePhrase $1 MOOOOOO
storePhrase $1 moooooo
storePhrase $1 MOOOOOOO
storePhrase $1 moooooooo
storePhrase $1 moooooooooooo
storePhrase $1 MoO
storePhrase $1 mOo
storePhrase $1 MoOoO
storePhrase $1 mOoOo
storePhrase $1 MOo
storePhrase $1 moO
storePhrase $1 MoOo
storePhrase $1 MOOoo
storePhrase $1 mooOO
storePhrase $1 mOOoo

storePhrase $2 cow
storePhrase $2 milky
storePhrase $2 udders
storePhrase $2 docile
storePhrase $2 peaceful
storePhrase $2 happy
storePhrase $2 milked
storePhrase $2 simple
storePhrase $2 purpose
storePhrase $2 graze
storePhrase $2 chew
storePhrase $2 herd
storePhrase $2 pasture
storePhrase $2 heavy
storePhrase $2 full
storePhrase $2 empty mind
storePhrase $2 obey

"""

# 48 groups of 4 statements = 192 total (144 blink, 24 cap, 24 bigcap)
# maintains the ~3:1 blink-to-non-blink ratio.
NUM_GROUPS = 48
POS_MIN = -90
POS_MAX = 90


def rand_pos():
    return random.randint(POS_MIN, POS_MAX), random.randint(POS_MIN, POS_MAX)


def blink_block():
    x, y = rand_pos()
    return f"setBlinkX {x}\nsetBlinkY {y}\nblink $2\n"


def cap_block():
    x, y = rand_pos()
    return f"setCaptionX {x}\nsetCaptionY {y}\ncap $1\n"


def bigcap_block():
    x, y = rand_pos()
    return f"setBigCaptionX {x}\nsetBigCaptionY {y}\nbigcap $1\n"


def main():
    out = [HEADER]
    for i in range(NUM_GROUPS):
        out.append("\n")  # blank line before group
        out.append(blink_block())
        out.append("\n")
        out.append(blink_block())
        out.append("\n")
        out.append(blink_block())
        out.append("\n")
        # alternate cap / bigcap for the 4th statement in each group
        out.append(cap_block() if i % 2 == 0 else bigcap_block())

    target = os.path.join(os.path.dirname(__file__), "hucow_brainwashing.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(out))
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()

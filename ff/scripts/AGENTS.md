# FlipFlip Caption Scripts: Agent Instruction Guide

This document is designed to give you (an AI agent) the necessary context and rules to write, modify, and understand FlipFlip caption scripts. When the user asks you to create or edit a script, follow these exact syntax rules and refer to the examples in this `ff/scripts/` directory if needed.

## 1. What are FlipFlip Caption Scripts?
FlipFlip is an application where users watch slideshows. "Caption scripts" are text files that dictate what text flashes on the screen, when it flashes, for how long, and where. 

Scripts are read line by line. Blank lines are ignored. Lines consist of a command followed by arguments separated by spaces.
**All times are represented in milliseconds (ms).**

## 2. Core Commands (Displaying Text)
You can insert a newline in the text by adding `\n`.

- `cap <TEXT>`: Shows medium-sized text for `captionDuration` ms, then waits `captionDelay` ms.
- `bigcap <TEXT>`: Shows big text for `captionDuration` ms, then waits `captionDelay` ms.
- `blink <TEXT> / <TEXT> / <TEXT>`: Shows each text segment sequentially. Each flashes for `blinkDuration` ms, delaying `blinkDelay` ms between each. After all are shown, waits `blinkGroupDelay` ms. Note the spaces around the slashes.
- `count <START> <END>`: Counts from START number to END number. Shows each number for `countDuration`, waits `countDelay`, and waits `countGroupDelay` afterward.
  You can also show a circular progress bar around the count by using these commands:
  - `setShowCountProgress true`: Enables progress bar (default false)
  - `setCountProgressScale <SCALE_NUM>`: Sets progress bar scale (default 500)
  - `setCountProgressColor <NUM> <COLOR_HEX>`: Sets the color of progress bar at the designated number (e.g. `setCountProgressColor 5 #ffeb3b`)
  - `setCountProgressOffset true`: Setting this as true will offset the total, so that your end number operates as 0.
  - `setCountColorMatch true`: Setting this to true will make the count color match the progress color.
- `wait <MILLISECONDS>`: Pauses execution for the specified milliseconds.
- `advance`: Advances the background scene 1 image forward.

## 3. Setters (Configuring Behavior)
By default, commands need to be configured. Usually, scripts start with a standard group of setters to configure durations and delays. 

**Format:** `set<CommandPrefix><Attribute> <MIN_MS> [<MAX_MS>]`
If only one number is provided, it sets an absolute constant duration. If two are provided, the value will be randomized or oscillate between `MIN` and `MAX`.

### Common Setters
```text
setBlinkDuration 300
setBlinkDelay 100
setBlinkGroupDelay 500

setCaptionDuration 1000
setCaptionDelay 1000

setCountDuration 500
setCountDelay 100
setCountGroupDelay 1000
```

## 4. Advanced Timing Functions
You can change *how* delays or durations are processed (default is `constant`).
**Timing Functions (`constant`, `random`, `wave`, `bpm`, `scene`)**

Set timing functions by appending `TF`, `DelayTF`, or `GroupDelayTF` to the command prefix:
- `setBlinkDelayTF random`
- `setCaptionTF wave`
- `setCountGroupDelayTF bpm`

**Timing Function Modifiers:**
You can further control `wave` timings (wave rate, 0-100) or `bpm` timings (bpm multiplier, 0-5.0):
- `setBlinkWaveRate 75` or `setBlinkDelayWaveRate 75`
- `setCaptionBPMMulti 2` or `setCaptionDelayBPMMulti 2`
- `setCountGroupDelayWaveRate 50`

## 5. Screen Positioning and Opacity
Commands are centered by default. You can offset them on the X and Y axis using numbers (typically from `-100` to `100`).
- `setBlinkX -75` / `setBlinkY 50`
- `setCaptionX <POS>` / `setCaptionY <POS>`
- `setBigCaptionX <POS>` / `setBigCaptionY <POS>`
- `setCountX <POS>` / `setCountY <POS>`

**Opacity**
You can set the opacity within a script on a per-command basis using values between 0 and 100 (default 100).
- `setBlinkOpacity <OPACITY>`
- `setCaptionOpacity <OPACITY>`
- `setBigCaptionOpacity <OPACITY>`
- `setCountOpacity <OPACITY>`

## 6. Variables and Random Phrases
You can store lists of phrases and pull randomly from them using `$RANDOM_PHRASE`.

```text
storePhrase GOOD GIRL
storePhrase OBEY
storePhrase SERVE

cap $RANDOM_PHRASE
blink $RANDOM_PHRASE / $RANDOM_PHRASE
```

**Phrase Groups (1-9):**
```text
storePhrase $1 Good
storePhrase $1 Bad
storePhrase $2 Girl
storePhrase $2 Boy

cap $1 $2
```
**Tag Phrases:** Use `$TAG_PHRASE` to fetch a phrase dynamically based on the current media's tag.

## 7. Audio playback
You can load `.wav` or `.mp3` files and play them during scripts:
```text
storeAudio "C:\path\to\snap.wav" snap
playAudio snap 100
```
(100 is the volume).

## 8. Timestamp Scripts
If exact synchronization with audio/video is required, use timestamps. 
**Crucial Rule:** Timestamp scripts do NOT loop. Also, all setters in a timestamp script MUST be prefixed with a timestamp (often `0`).

Valid formats: `HH:MM:SS.mmm`, `MM:SS`, `SS.mmm`, etc.

```text
0 setBlinkDuration 300
0 setCaptionDuration 2000

00:00 bigcap YOU ARE READY
00:03.2 blink TO / OBEY / ME
```

## AI Agent Directives (How to assist the User)
1. **Analyze existing files:** This directory (`ff/scripts/`) has multiple `.txt` examples. Look to them for tone, pacing, and usage of setters.
2. **Setup your environment:** Begin your scripts by defining your set variables (`setBlinkDuration`, etc.) so the user doesn't have a rapid flashing mess, unless specified.
3. **Be creative with positioning and groups:** Use position randomness or groups for dynamic effects (e.g., spirals, random placement on screen).
4. **Follow instructions completely:** The user might ask for "Spirals" or "Random blinks". Use `setBlinkX` and `setBlinkY` repeatedly between commands to change position manually if no automated system is viable.
5. **Format exactly:** FlipFlip parser relies heavily on accurate spacing, particularly around the ` / ` in `blink`.

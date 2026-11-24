# Funniest Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/cryptokom-tech/funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/cryptokom-tech/funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for the [make.fun bounty "Funniest Time Machine Warning Label"](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151):
one line, at most 120 characters — the funniest warning label for a
time machine.

## The entry

> WARNING: Do not press the red button. You pressed it. That is why you are reading this.

The label warns you not to press the red button, then tells you that
you already pressed it — which is the only reason you are reading the
label at all. A closed causal loop, delivered with a straight face,
like a genuine safety notice. No "do not meet yourself", no
grandfather, no butterfly: the field is full of all three.

## How it works

`main.py` (Python 3, standard library only, no network) writes the
single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
then reads it back and asserts it matches, inside the 1–120
character gate.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

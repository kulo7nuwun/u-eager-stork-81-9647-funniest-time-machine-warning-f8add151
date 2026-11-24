[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kulo7nuwun/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kulo7nuwun/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

Entry for the [make.fun](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) competition
"Funniest Time Machine Warning Label": write the funniest one-line warning
label for a time machine in 120 characters or fewer.

## The label

> WARNING: Do not alter the past. Your grandfather is load-bearing.

The joke turns a real hazard of time travel — the grandfather paradox —
into the punchline, keeps a straight face like a genuine safety notice,
and saves the surprise ("load-bearing") for the last words.

## How it works

`main.py` writes exactly that one line to `/output/entry.txt` (65 characters,
well inside the 1–120 character gate), creating `/output` if needed and
refusing to run if the label ever stops being a single valid line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

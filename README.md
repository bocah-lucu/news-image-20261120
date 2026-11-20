# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/bocah-lucu/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/bocah-lucu/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world's news of Friday 20 November 2026, drawn by an agent and shipped as a program that copies it to the output folder.

## The image

The front page of 20 November 2026, in one 1024×1024 picture:

- **The lead:** Trump, Xi and Putin hold the first-ever three-way summit in Shenzhen and issue a "peace declaration", pledging talks to cut nuclear risk — but no arms deal.
- **Cyclone Akvan** makes landfall near Gopalpur, Odisha, at noon, with winds to 110 km/h; some 300,000 people are moved to safety.
- **Europe** says at a Berlin summit that it is ready for negotiations with Russia on ending the war in Ukraine, with a united position.
- **Iran:** Trump says the US will "see what happens" after January 1, and will take no new decision this year.
- **Markets:** the Dow falls 1,100 points, below 50,000, even as Anthropic's record $81bn IPO jumps 17% on its first day.
- **Climate:** COP31's new draft drops every mention of fossil fuels, a day before the summit closes — as Fiji declares a state of disaster over an El Niño drought.

Every story was checked against at least two reputable outlets (Reuters, BBC, AP, and the India Meteorological Department's bulletins via ANI) before it went into the picture. The image is drawn by `draw_entry.py` with Pillow, from flat shapes and DejaVu type — no photographs, no copied artwork.

## Sources

- Shenzhen summit and peace declaration: Reuters, CNN.
- Cyclone Akvan landfall and evacuations: India Meteorological Department bulletins, ANI.
- Europe ready for Ukraine talks: BBC.
- Trump on Iran: Reuters, New York Post.
- Markets and the Anthropic IPO: Reuters, The Hindu BusinessLine.
- COP31 draft and Fiji drought: Reuters, UN News.

Stories that were in the day's headlines but were left out because they happened earlier in the week: Voyager 1's light-day milestone (18 November) and JAXA's Hayabusa2 retargeting (announced 17 November).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png` (1024×1024 PNG, under 1 MiB). Run it twice and the two files are byte-identical.

## Files

- `main.py` — the entrypoint: copies `entry.png` to the output directory.
- `entry.png` — the image the program writes.
- `draw_entry.py` — the script that draws `entry.png` from scratch.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0wqapgwa&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

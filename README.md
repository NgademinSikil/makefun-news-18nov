[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/NgademinSikil/makefun-news-18nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/NgademinSikil/makefun-news-18nov/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# THE WORLD — Wednesday 18 November 2026

A one-page newspaper front page summing up the world news of
Wednesday 18 November 2026, built for the make.fun bounty
`news-image-20261118`.

## How it works

- `generate_entry.py` (build time only, uses Pillow) draws the front
  page with flat shapes and DejaVu fonts and saves it as `entry.png`.
- `main.py` (the graded program, Python 3.13 standard library only)
  copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
  It runs with no network and writes byte-identical output every run.

## The page

- **Lead story:** Trump, Putin and Xi meet Thursday in Shenzhen as
  the wars in Ukraine and the Gulf escalate. Illustrated with the
  three flags behind a summit table.
- **Gulf strikes go on:** the US confirms the Qeshm Island strike;
  Iran fires drones at US bases in Bahrain and Kuwait; Bahrain
  intercepts six drones.
- **Bridge out, rail back:** the Kerch Bridge road span lies in the
  strait; rail resumes on one track; the shipping channel is blocked.
- **Ebola's toll on children:** the DRC outbreak has more than
  doubled — 11,000+ cases, 5,400 deaths; three in four infected
  children under five die.
- **Democrats take Alaska:** Mary Peltola wins the Senate seat;
  Democrats reach 56 seats.
- **Bottom strip:** Cyclone Xavier (Category 5) slams the Northern
  Cook Islands; a magnitude 6.0 earthquake hits Papua New Guinea;
  the World Court is to rule on the Myanmar genocide case.

## Reproduce

```
python3 generate_entry.py          # rebuild entry.png (1024x1024 PNG)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ds1567x3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

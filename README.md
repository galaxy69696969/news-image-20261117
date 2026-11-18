# World News — Tuesday, 17 November 2026

A make.fun entry for competition `news-image-20261117`: one image that sums
up the world news of Tuesday, 17 November 2026.

## The image

A newspaper-style front page (`assets/entry.png.b64` — base64 of the rendered PNG, 1024×1024, rendered at
build time with Pillow — the entry program itself is standard-library only):

- **Lead — War in Ukraine:** Ukraine's missiles and drones destroyed the
  central road span of the Kerch Bridge linking Russia to Crimea; Russia
  answered with strikes on Kyiv's bridges.
- **Middle East:** Iranian drones targeted a US radar site at Bahrain's
  Sheikh Isa air base (intercepted, no casualties); tankers hit by mines
  near the Strait of Hormuz.
- **Health:** PAHO said the US lost its measles elimination status after
  26 years; the CDC counted 5,412 US cases in 2026.
- **Markets:** Nvidia reported record quarterly revenue of $115.8bn
  (+103%) and shares jumped after hours; the WSJ reported an SEC probe
  into its disclosures.
- **Asia:** Trump landed in Manila for a Quad summit, bound for APEC in
  Shenzhen, where he, Xi Jinping and Vladimir Putin are expected to meet.
- **Also on Tuesday:** Israel's parliament elects a new speaker; France's
  public-sector strike turnout falls; Japan scrambles jets as Russian
  aircraft enter its airspace.

Sources: Reuters, CDC, PAHO (all reporting dated 17 November 2026).

## How it runs

`main.py` (Python 3.13, standard library only, no network) decodes
`assets/entry.png.b64` byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), so both grading runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.

# Troy City Defense System

![build](https://img.shields.io/badge/build-passing-brightgreen)
![version](https://img.shields.io/badge/version-12.0.0-blue)
![python](https://img.shields.io/badge/python-3.12-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)
![siege](https://img.shields.io/badge/siege-year%2010-red)

The software that has kept Troy standing for ten years: walls, gates, sentries,
the granary, the stables and the oracle, maintained by the city engineers.

## Layout

| Path | What lives there |
|---|---|
| `troy/walls/` | rampart heights, towers, breach repairs |
| `troy/gates/` | the Scaean and Dardanian gates, watchwords |
| `troy/sentries/` | shifts, beacons, the night watch roster |
| `troy/granary/` | rations and stores for a city under siege |
| `troy/chariots/` | stables and repairs |
| `troy/oracle/` | omens (ignored, mostly) |
| `config/` | runtime configuration |
| `deploy/` | container image and entrypoint |
| `docs/` | operations manual and history |

## Run it

```sh
docker build -f deploy/Dockerfile -t troy .
docker run --rm troy
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Releases are named after the year of the war
they shipped in; see [CHANGELOG.md](CHANGELOG.md) and `git tag -n`.

## A note from the council

The Greeks have gone. Whatever they left on the beach is ours now.

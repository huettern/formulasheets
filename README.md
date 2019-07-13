# Formulasheets [![Build Status](https://travis-ci.org/noah95/formulasheets.svg?branch=master)](https://travis-ci.org/noah95/formulasheets)

## Downloads
Most recent builds from `v0.0` tag. Statistics are reset after each push to `v0.0`.

### Completed
| Name          | Status | Download      | Statistics |
| ------------- |--------|---------------|------------|
| Leistungselektronik | Finished | [link][le] | ![][le-badge] |
| Analysis III - PDE | Finished | [link][an3] | ![][an3-badge] |
| Communication Networks | Finished | [link][comnet] | ![][comnet-badge] |
| Semiconductor Devices | Finished | [short][semi] [extended][semi-ex] | ![][semi-badge] ![][semi-ex-badge] |

[le]: https://github.com/noah95/formulasheets/releases/download/v1.0/leistungselektronik.pdf
[le-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v1.0/leistungselektronik.pdf.svg
[an3]: https://github.com/noah95/formulasheets/releases/download/v1.0/analysis3pde.pdf
[an3-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v1.0/analysis3pde.pdf.svg
[comnet]: https://github.com/noah95/formulasheets/releases/download/v2.0.1/ComNet_summary.pdf
[comnet-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.0.1/ComNet_summary.pdf.svg

[semi]: https://github.com/noah95/formulasheets/releases/download/v2.1/semiconductordevices.pdf
[semi-ex]: https://github.com/noah95/formulasheets/releases/download/v2.1/semiconductordevices-extended.pdf
[semi-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1/semiconductordevices.pdf.svg
[semi-ex-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1/semiconductordevices-extended.pdf.svg

### Working
| Name          | Status | Download      | Statistics |
| ------------- |--------|---------------|------------|
| Electrodynamics | stall | [link](https://github.com/noah95/formulasheets/releases/download/v0.0/electrodynamics.pdf) | ![](https://img.shields.io/github/downloads/noah95/formulasheets/v0.0/electrodynamics.pdf.svg) |
| Introduction to Machine Learning | stall | [link](https://github.com/noah95/formulasheets/releases/download/v0.0/IntroToML_summary.pdf) | ![](https://img.shields.io/github/downloads/noah95/formulasheets/v0.0/IntroToML_summary.pdf.svg) |
| Numerische Methoden | stall | [link](https://github.com/noah95/formulasheets/releases/download/v0.0/Numerik_summary.pdf) | ![](https://img.shields.io/github/downloads/noah95/formulasheets/v0.0/Numerik_summary.pdf.svg) |

## Build documentation

### Re-Tag
To update the download links above, the `v0.0` tag has to be overwritten by running:

```bash
git tag -f v0.0
git push -f origin v0.0
```
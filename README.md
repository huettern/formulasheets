# Formulasheets [![Build Status](https://travis-ci.org/noah95/formulasheets.svg?branch=master)](https://travis-ci.org/noah95/formulasheets)

## Downloads
Most recent builds from `v0.0` tag. Statistics are reset after each push to `v0.0`.

### Completed
| Name          | Status | Download      | Statistics |
| ------------- |--------|---------------|------------|
| Leistungselektronik | Finished | [link][le] | ![][le-badge] |
| Analysis III - PDE | Finished | [link][an3] | ![][an3-badge] |
| Communication Networks | Finished | [link][comnet] | ![][comnet-badge] |
| Semiconductor Devices | Finished | [link][semi] | ![][semi-badge] |
| Electrodynamics (handwritten) | Finished | [link][em] | ![][em-badge] |
| Numerische Methoden (handwritten) | Finished | [link][num] | ![][num-badge] |
| Wahrscheinlichkeitstheorie und Statistik (handwritten) | Finished | [link][wus] | ![][wus-badge] |
| VLSI1 (handwritten) | Finished | [link][vlsi1] | ![][vlsi1-badge] |

[le]: https://github.com/noah95/formulasheets/releases/download/v1.0/leistungselektronik.pdf
[le-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v1.0/leistungselektronik.pdf.svg
[an3]: https://github.com/noah95/formulasheets/releases/download/v1.0/analysis3pde.pdf
[an3-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v1.0/analysis3pde.pdf.svg
[comnet]: https://github.com/noah95/formulasheets/releases/download/v2.0.1/ComNet_summary.pdf
[comnet-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.0.1/ComNet_summary.pdf.svg

[semi]: https://github.com/noah95/formulasheets/releases/download/v2.1.1/semiconductordevices.pdf
[semi-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1.1/semiconductordevices.pdf.svg

[em]: https://github.com/noah95/formulasheets/releases/download/v2.1.2/em_fosa_huetter.pdf
[em-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1.2/em_fosa_huetter.pdf.svg

[num]: https://github.com/noah95/formulasheets/releases/download/v2.1.2/num_fosa_huetter.pdf
[num-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1.2/num_fosa_huetter.pdf.svg

[wus]: https://github.com/noah95/formulasheets/releases/download/v2.1.2/wus_fosa_huetter.pdf
[wus-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v2.1.2/wus_fosa_huetter.pdf.svg

[vlsi1]: https://github.com/noah95/formulasheets/releases/download/v3.0.0/vlsi1_fosa_huetter.pdf
[vlsi1-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v3.0.0/vlsi1_fosa_huetter.pdf.svg

### Work in Progress
| Name          | Status | Download      |
| ------------- |--------|---------------|
| Communication Systems | WIP | [link][comsys] |

[comsys]: https://github.com/noah95/formulasheets/raw/build/Communication%20Systems/communication_systems.pdf

## Build documentation

### Re-Tag
To update the download links above, the `v0.0` tag has to be overwritten by running:

```bash
git tag -f v0.0
git push -f origin v0.0
```

## Build
```bash
brew cask install mactex-no-gui
make
```
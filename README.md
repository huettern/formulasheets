# Formulasheets [![Build Status](https://travis-ci.org/noah95/formulasheets.svg?branch=master)](https://travis-ci.org/noah95/formulasheets)

## Downloads
Most recent builds from `v0.0` tag. Statistics are reset after each push to `v0.0`.

### Completed

| Name                                                    | Type                 | Status   | Download                    |
|:--------------------------------------------------------|:---------------------|:---------|:----------------------------|
| Leistungselektronik                                     | Fosa                 | Finished | [![][le-badge]][le]         |
| Analysis III - PDE                                      | Fosa                 | Finished | [![][an3-badge]][an3]       |
| Communication Networks                                  | Fosa                 | Finished | [![][comnet-badge]][comnet] |
| Semiconductor Devices                                   | Fosa                 | Finished | [![][semi-badge]][semi]     |
| Electrodynamics                                         | Fosa, Handwritten    | Finished | [![][em-badge]][em]         |
| Numerische Methoden                                     | Fosa, Handwritten    | Finished | [![][num-badge]][num]       |
| Wahrscheinlichkeitstheorie und Statistik                | Fosa, Handwritten    | Finished | [![][wus-badge]][wus]       |
| VLSI1                                                   | Summary, Handwritten | Finished | [![][vlsi1-badge]][vlsi1]   |
| Communication Systems                                   | Fosa                 | Finished | [![][comsys-badge]][comsys] |
| Advanced Communication Networks                         | Summary              | Finished | [![][advnet-badge]][advnet] |
| Signal Analysis, Models and Machine Learning            | Summary, Handwritten | Finished | [![][sml-badge]][sml]       |
| Systems-on-Chip for Data Analytics and Machine Learning | Summary, Handwritten | Finished | [![][soc-badge]][soc]       |
| VLSI2                                                   | Summary, Handwritten | Finished | [![][vlsi2-badge]][vlsi2]   |

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

[comsys]: https://github.com/noah95/formulasheets/releases/download/v3.0.0/comsys_fosa_huetter.pdf
[comsys-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v3.0.0/comsys_fosa_huetter.pdf.svg

[advnet]: https://github.com/noah95/formulasheets/releases/download/v3.1.0/advnet_fosa_huetter.pdf
[advnet-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v3.1.0/advnet_fosa_huetter.pdf.svg

[sml]: https://github.com/noah95/formulasheets/releases/download/v3.1.1/sml_summary_huetter.pdf
[sml-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v3.1.1/sml_summary_huetter.pdf.svg

[soc]: https://github.com/noah95/formulasheets/releases/download/v4.0.0/soc_summary_huetter.pdf
[soc-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v4.0.0/soc_summary_huetter.pdf.svg

[vlsi2]: https://github.com/noah95/formulasheets/releases/download/v4.0.0/vlsi2_summary_huetter.pdf
[vlsi2-badge]: https://img.shields.io/github/downloads/noah95/formulasheets/v4.0.0/vlsi2_summary_huetter.pdf.svg


### Work in Progress
| Name          | Status | Download      |
| ------------- |--------|---------------|
| SoC for Data Analytics | WIP  | [link][socdaml] |

[socdaml]: https://github.com/noah95/formulasheets/raw/build/SoC%20for%20Data%20Analytics%20and%20Machine%20Learning/soc_for_da_ml_huetter.pdf

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
# India Solar Benchmark Dataset Generation Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Years](https://img.shields.io/badge/Years-2016--2025-blueviolet)
![Cities](https://img.shields.io/badge/Cities-50-green)
![Rows](https://img.shields.io/badge/Rows-4.38M-orange)
![Features](https://img.shields.io/badge/Features-60-red)
![Version](https://img.shields.io/badge/version-v1.0-success)
![License](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/narendersingh007/india-solar-benchmark-dataset)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/datasets/Narendersingh007/india-solar-benchmark-dataset)
[![GitHub Release](https://img.shields.io/github/v/release/Narendersingh007/india-solar-benchmark-dataset)](https://github.com/Narendersingh007/india-solar-benchmark-dataset/releases)

A reproducible large-scale data engineering, feature engineering, and benchmark dataset generation pipeline for solar irradiance forecasting research.
The pipeline automatically collects meteorological observations from NASA POWER across multiple Indian cities, performs validation and preprocessing, generates temporal, geographical, solar-geometry, physics-informed, lag, and rolling statistical features, and exports machine-learning-ready benchmark datasets with standardized train, validation, and test splits.

The first public release generated the India Solar Benchmark Dataset v1.0 — one of the largest publicly available solar forecasting datasets for India, containing 4.38 million hourly observations spanning 50 cities over 10 years.
  
## Generated Benchmark Dataset
The pipeline currently produces two benchmark datasets:

| Dataset | Description |
|----------|-------------|
| **india_multicity_raw.parquet** | Cleaned and standardized meteorological observations directly after preprocessing, before feature engineering. Suitable for custom feature engineering and research. |
| **india_multicity_ml_ready.parquet** | Fully engineered machine-learning-ready benchmark dataset containing temporal, solar geometry, physics-informed, lag, and rolling statistical features. |
### Dataset Statistics

| Metric | Value |
|----------|----------|
| Cities | 50 |
| Years | 2016–2025 |
| Rows | 4,383,600 |
| Features | 60 |
| Target | ALLSKY_SFC_SW_DWN |
| Storage | Parquet |

## Dataset Availability

| Platform | Access |
|-----------|-----------|
| GitHub Repository | https://github.com/Narendersingh007/india-solar-benchmark-dataset |
| GitHub Release (v1.0) | https://github.com/Narendersingh007/india-solar-benchmark-dataset/releases |
| Kaggle Dataset | https://www.kaggle.com/datasets/narendersingh007/india-solar-benchmark-dataset |
| Hugging Face Dataset | https://huggingface.co/datasets/Narendersingh007/india-solar-benchmark-dataset |

## Table of Contents

- [Dataset Overview](#dataset-overview)
- [Engineering Highlights](#engineering-highlights)
- [Intended Use Cases](#intended-use-cases)
- [Pipeline Architecture](#pipeline-architecture)
- [Dataset Generation Pipeline](#dataset-generation-pipeline)
- [Feature Groups](#feature-groups)
- [Train / Validation / Test Split](#train--validation--test-split)
- [Geographic Coverage](#geographic-coverage)
- [Dataset Files](#dataset-files)
- [File Sizes](#file-sizes)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Data Quality & Validation](#data-quality--validation)
- [Reproducibility](#reproducibility)
- [Citation](#citation)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Dataset Overview

| Metric | Value |
|----------|----------|
| Cities | 50 |
| Years Covered | 2016–2025 |
| Rows | 4,383,600 |
| Raw Files | 500 |
| Features | 60 |
| Frequency | Hourly |
| Target | ALLSKY_SFC_SW_DWN |
| Benchmark Files | Raw + ML-Ready Parquet |

The primary prediction target is `ALLSKY_SFC_SW_DWN` — the hourly all-sky surface shortwave downward irradiance (Global Horizontal Irradiance, GHI), measured in W/m².

## Engineering Highlights

- Automated collection of 500 NASA POWER city-year files
- Configuration-driven pipeline using YAML
- Modular ETL architecture
- Deterministic feature engineering workflow
- Automated metadata and validation generation
- Reproducible benchmark creation process
- Parquet-based storage optimization
- Chronological leakage-safe dataset splitting
- Automatic benchmark dataset generation
- Raw and ML-ready dataset export
  
## Intended Use Cases

- Solar irradiance forecasting
- Renewable energy generation prediction
- Time-series forecasting research (Transformer, LSTM, GRU)
- XGBoost, LightGBM, and other tree-based forecasting models
- Physics-informed machine learning
- Feature engineering studies and energy systems research

## Pipeline Architecture

The repository follows a modular ETL architecture:

| Layer | Responsibility |
|--------|----------------|
| Data Acquisition | NASA POWER download service |
| Data Processing | Cleaning, merging, preprocessing |
| Feature Engineering | Temporal, cyclical, solar, lag and rolling features |
| Validation | Dataset integrity checks |
| Metadata | Schema and statistical report generation |
| Benchmark Packaging | Raw dataset, ML-ready dataset and train/validation/test splits |

Each stage is independently configurable and reproducible, enabling benchmark dataset generation for new cities, regions, and forecasting tasks with minimal changes.
## Dataset Generation Pipeline
<img width="912" height="722" alt="Screenshot 2026-06-23 at 4 49 37 PM" src="https://github.com/user-attachments/assets/3373e4ff-b5b3-485a-a508-506ad6da430e" />

## Feature Groups

| Group | Examples |
|---------|---------|
| Weather Variables | T2M, RH2M, WS10M, PRECTOTCORR, PS, WS2M, WD10M |
| Temporal Features | year, month, day, hour, weekday, week, quarter, is_weekend |
| Cyclical Features | hour_sin, hour_cos, month_sin, month_cos, dayofyear_sin/cos |
| Geographic Features | CITY, LATITUDE, LONGITUDE |
| Solar Geometry Features | SOLAR_ZENITH, SOLAR_ELEVATION, SOLAR_AZIMUTH, CLEARSKY_GHI/DNI/DHI |
| Physics-Informed Features | TEMP_HUMIDITY, DEWPOINT_SPREAD, WIND_POWER, PRESSURE_TEMP |
| Lag Features | lag_1, lag_3, lag_6, lag_12, lag_24, lag_168 |
| Rolling Features | rolling_mean_24, rolling_std_24, rolling_mean_168, rolling_max_24, rolling_min_24 |

Full schema and column definitions are available in `data/metadata/schema.csv`.

## Train / Validation / Test Split

| Split | Years | Purpose |
|----------|----------|----------|
| Train | 2016–2022 | Model training |
| Validation | 2023 | Hyperparameter tuning |
| Test | 2024–2025 | Final evaluation |

The dataset uses chronological splitting to prevent temporal leakage and mimic real-world forecasting scenarios, where models must predict future observations using only historical information.
**Leakage prevention:** avoid random shuffling across years, using future lag values, computing rolling statistics with future timestamps, or training on validation/test periods.

## Geographic Coverage

The dataset spans 50 major Indian cities across North, South, East, West, Central, and Northeast India.
Coverage includes:
- Coastal and inland regions
- Plains, deserts, and mountainous terrain
- Tropical, subtropical, temperate, and semi-arid climates

This diversity enables evaluation of both city-specific and generalized solar forecasting models.

## Dataset Files

| Path | Description |
|------|-------------|
| data/raw/ | Original NASA POWER downloads |
| data/processed/ | Intermediate cleaned city datasets |
| data/benchmark/india_multicity_raw.parquet | Cleaned benchmark dataset before feature engineering |
| data/benchmark/india_multicity_ml_ready.parquet | Final ML-ready benchmark dataset |
| data/splits/ | Train / Validation / Test splits |
| data/metadata/ | Schema, statistics and validation reports |

## Repository Structure

```text
src/
├── clients/              # NASA POWER API clients
├── downloader/           # Data acquisition
├── processing/           # Cleaning & merging
├── features/             # Feature engineering
├── validation/           # Data validation
├── metadata/             # Reports & schema generation
├── pipeline/             # End-to-end orchestration
├── storage/              # File management
├── utils/                # Logging & configuration
└── main.py

configs/                  # YAML configurations
data/                     # Raw, processed & benchmark datasets
docs/                     # Documentation
tests/                    # Unit tests

README.md
requirements.txt
LICENSE
```
### File Sizes

| File | Size |
|--------|--------|
| `india_multicity_raw.parquet` | 71 MB |
| `india_multicity_ml_ready.parquet` | 412 MB |
| `train.parquet` | 286 MB |
| `val.parquet` | 42 MB |
| `test.parquet` | 82 MB |


## Installation

Clone the repository:

```bash
git clone https://github.com/Narendersingh007/india-solar-benchmark-dataset.git
cd solar-benchmark-dataset
```

Create a virtual environment:

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The dataset generation pipeline is fully configurable through YAML files in `configs/`:

- `configs/cities.yaml` — geographic coverage (city names, latitude, longitude)
- `configs/api.yaml` — NASA POWER API parameters and download settings
- `configs/pipeline.yaml` — download years, output locations, processing and feature engineering options

Example `cities.yaml` entry:

```yaml
cities:
  - name: New_Delhi
    latitude: 28.6139
    longitude: 77.2090

  - name: Mumbai
    latitude: 19.0760
    longitude: 72.8777
```

Changes to configuration files are automatically reflected during dataset generation.

## Usage

Generate the complete dataset:

```bash
python src/main.py
```

The pipeline automatically performs NASA POWER data collection, raw storage, cleaning and validation, feature engineering, metadata generation, ML-ready dataset creation, and train/validation/test splitting — producing:

```text
data/
├── raw/
├── processed/
├── metadata/
├── ml_ready/
└── splits/
```

## Data Quality & Validation

Automated validation and metadata generation ensure dataset integrity and reproducibility, including:

- Dataset schema (`schema.csv`)
- Statistical summaries (`statistics.csv`)
- Missing value reports (`missing_values.csv`)
- Geographic metadata (`city_metadata.csv`)

Validation checks cover missing values, datetime consistency, column validation, city metadata integrity, and overall dataset completeness. All reports are stored in `data/metadata/`.

## Reproducibility

Given the same configuration files and NASA POWER API responses, the dataset can be reproduced from scratch via:

- YAML-based configuration management
- Automated download orchestration
- Deterministic feature engineering
- Standardized train/validation/test splits
- Metadata and validation reports
- Version-controlled source code

## Citation

If you use this dataset in your research, publication, or project, please cite:

```bibtex
@software{india_solar_pipeline,
  author = {Narender Singh},
  title = {India Solar Benchmark Dataset Generation Pipeline},
  year = {2026},
  url = {https://github.com/Narendersingh007/india-solar-benchmark-dataset}
}
```

## License

- **Dataset:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — you may share and adapt the data for any purpose, including commercially, as long as you give appropriate credit.
- **Code:** [MIT License](https://opensource.org/licenses/MIT) — permissive use, modification, and distribution of the pipeline source code.

NASA POWER data is provided under NASA's open data policy; see the [NASA POWER data use guidelines](https://power.larc.nasa.gov/docs/services/api/) for details.

## Acknowledgements

This dataset is built using meteorological and solar radiation data from the [NASA POWER](https://power.larc.nasa.gov/) project, with solar geometry features computed via [PVLIB](https://pvlib-python.readthedocs.io/).

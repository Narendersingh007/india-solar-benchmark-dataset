# India Solar Benchmark Dataset

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Years](https://img.shields.io/badge/Years-2016--2025-blueviolet)
![Cities](https://img.shields.io/badge/Cities-50-green)
![Rows](https://img.shields.io/badge/Rows-4.38M-orange)
![Features](https://img.shields.io/badge/Features-60-red)
![Version](https://img.shields.io/badge/version-v1.0-success)
![License](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)

**Dataset Size:** 4.38M rows • 60 features • 50 cities • 10 years of hourly observations
A large-scale, multi-city solar irradiance forecasting dataset for India built from NASA POWER meteorological observations and enhanced with temporal, geographical, solar-geometry, physics-informed, lag, and rolling statistical features.
The dataset contains hourly weather and solar measurements collected across 50 major Indian cities from 2016 to 2025, providing a unified dataset for solar energy forecasting, renewable energy research, time-series modeling, and machine learning applications.

## Dataset Availability

| Platform | Link |
|----------|----------|
| GitHub Repository | https://github.com/Narendersingh007/india-solar-benchmark-dataset |
| Kaggle Dataset | https://www.kaggle.com/datasets/narendersingh007/india-solar-benchmark-dataset |
| Hugging Face Dataset | https://huggingface.co/datasets/Narendersingh007/india-solar-benchmark-dataset |
| GitHub Release | v1.0 |

## Table of Contents

- [Dataset Overview](#dataset-overview)
- [Key Highlights](#key-highlights)
- [Intended Use Cases](#intended-use-cases)
- [Dataset Generation Pipeline](#dataset-generation-pipeline)
- [Feature Groups](#feature-groups)
- [Train / Validation / Test Split](#train--validation--test-split)
- [Geographic Coverage](#geographic-coverage)
- [Dataset Files](#dataset-files)
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
| Source | NASA POWER API |
| Storage Format | CSV, Parquet |

The primary prediction target is `ALLSKY_SFC_SW_DWN` — the hourly all-sky surface shortwave downward irradiance (Global Horizontal Irradiance, GHI), measured in W/m².


## Key Highlights

- 50 Indian cities covering diverse climatic zones
- 10 years of hourly observations (2016–2025)
- 4.38 million records, 60 engineered features
- NASA POWER weather and solar variables
- Solar geometry features generated using PVLIB
- Physics-informed feature engineering
- Time-series lag and rolling window features
- Chronological train, validation, and test splits

## Intended Use Cases

- Solar irradiance forecasting
- Renewable energy generation prediction
- Time-series forecasting research (Transformer, LSTM, GRU)
- XGBoost, LightGBM, and other tree-based forecasting models
- Physics-informed machine learning
- Feature engineering studies and energy systems research

## Dataset Generation Pipeline

```text
NASA POWER API
      ↓
50 Cities × 10 Years
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Solar & Physics Features
      ↓
Lag & Rolling Features
      ↓
ML-Ready Dataset
      ↓
Train / Validation / Test Splits
```

Generated automatically through a reproducible Python pipeline: raw data is collected from NASA POWER for each city/year, merged and cleaned, then enriched with temporal, solar-geometry (PVLIB), physics-informed, lag, and rolling-window features before being exported to Parquet and split chronologically.

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
|--------|--------|
| `data/raw/` | Original NASA POWER API downloads |
| `data/processed/` | Cleaned city-level datasets and merged multicity dataset |
| `data/metadata/` | Schema, statistics, validation reports, and city metadata |
| `data/ml_ready/india_multicity_ml_ready.parquet` | Final machine-learning-ready  dataset (4,383,600 rows × 60 features) |
| `data/splits/` | Chronological train, validation, and test splits |

## Repository Structure

```text
configs/      Configuration files
data/         Raw, processed, metadata, and split datasets
src/          Dataset generation pipeline
notebooks/    Exploration and experiments
tests/        Unit tests
docs/         Additional documentation
```

### File Sizes

| File | Size |
|--------|--------|
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
source .venv/bin/activate
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
@dataset{india_solar_benchmark_dataset,
  title={India Solar Benchmark Dataset},
  author={Narender Singh},
  year={2026},
  publisher={GitHub},
  url={https://github.com/Narendersingh007/india-solar-benchmark-dataset}
}
```

## License

- **Dataset:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — you may share and adapt the data for any purpose, including commercially, as long as you give appropriate credit.
- **Code:** [MIT License](https://opensource.org/licenses/MIT) — permissive use, modification, and distribution of the pipeline source code.

NASA POWER data is provided under NASA's open data policy; see the [NASA POWER data use guidelines](https://power.larc.nasa.gov/docs/services/api/) for details.

## Acknowledgements

This dataset is built using meteorological and solar radiation data from the [NASA POWER](https://power.larc.nasa.gov/) project, with solar geometry features computed via [PVLIB](https://pvlib-python.readthedocs.io/).

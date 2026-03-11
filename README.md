# Data Migration Glue (In Progress)

## Project Goal
Build an AWS Glue-centered data migration pipeline from scratch (bronze → silver → gold) for synthetic datasets, with catalog discovery and transformation logic. This repository is currently in development; existing artifacts show the initial scaffolding and migration approach.

## What’s Included
- `Scripts/`:
  - `synthetic_csv_genrator.py` - generate synthetic CSV data for CRM, Insurance, Retail domains.
  - `data_mapping_sheet.py` - generate/inspect field mappings and mapping sheets.
  - `bronze_to_silver.py` - simple ETL transformation from bronze to silver stage.
- `synthetic_data/`:
  - `bronze/`, `silver/`, `gold/` layers with domain-specific CSV files.
- `data_mapping/`:
  - data mapping definitions and output conversion support.
- `cf_templates/`:
  - `glue-crawler.yaml` - AWS Glue crawler resources to scan S3 and create catalog tables.
  - `s3_datalakes.yml` - S3 bucket structure for data lake layers (if present).

## Primary Use Case
1. Generate synthetic domain data in the bronze layer.
2. Use AWS Glue crawler to discover and catalog data.
3. Run ETL to transform bronze data into silver business-ready datasets (\`bronze_to_silver.py\` currently).
4. (Future) Build gold layer aggregations and analytics outputs.

## Setup Instructions
### Prerequisites
- Python 3.9+ (latest stable preferred)
- AWS account with IAM permission to create S3/Glue resources
- AWS CLI configured (`aws configure`)
- Optional: `virtualenv`

### Install
```bash
cd d:/Backup_downloads/My_Projects/data-migration-glue
python -m venv .venv
.\.venv\Scripts\activate
pip install pandas pyyaml boto3
```

### Validate CloudFormation templates
```bash
aws cloudformation validate-template --template-body file://cf_templates/glue-crawler.yaml
aws cloudformation validate-template --template-body file://cf_templates/s3_datalakes.yml
```

## Quick Start (Current State)
1. Generate sample data:
   ```bash
   python Scripts/synthetic_csv_genrator.py
   ```
2. Inspect data mapping outputs:
   ```bash
   python Scripts/data_mapping_sheet.py
   ```
3. Run bronze→silver transform locally:
   ```bash
   python Scripts/bronze_to_silver.py
   ```
4. Review output CSVs in `synthetic_data/silver/` and `synthetic_data/gold/`.

## Data Lake Conventions
- `synthetic_data/bronze/<domain>/` raw source data
- `synthetic_data/silver/<domain>/` clean/intermediate data
- `synthetic_data/gold/<domain>/` curated analytics data

## Architecture Diagram
Below is the current architecture intended for this migration pipeline. Save or place your diagram image in the repo and update the path as needed.

![Glue Data Migration Architecture](./docs/architecture.png)

- Bronze layer raw CSVs are stored in S3 and/or local `synthetic_data/bronze`.
- Glue Crawler discovers schema and writes tables into Glue Data Catalog (`migration_catalog_db`).
- ETL processing is performed via `bronze_to_silver.py` (local prototype) or AWS Glue job conduit.
- Silver and Gold datasets land in S3 directories, enabling Athena query validation and downstream analytics.
- Monitoring and logging are expected via CloudWatch (future integration).

## Project Status
- [x] Synthetic data generation script exists
- [x] Bronze→Silver script exists
- [x] Glue crawler template exists (with resource fix applied)
- [ ] Glue jobs and IAM role policies need completion
- [ ] s3_datalakes template and actual deploy script needs validation
- [ ] Automated unit tests and data quality checks

## Next Actions (recommended)
1. Add `requirements.txt` and `pyproject.toml`.
2. Add `README` sections for verifying Glue role and S3 bucket naming.
3. Implement Glue ETL Job script (or Glue Python shell job) to read Bronze and write Silver/Gold.
4. Add `Makefile`/`cli` wrapper to manage all stages.
5. Add fully automated tests using `pytest` for output row counts, schema consistency, and null handling.

## Notes
- Paths in scripts may be relative; adjust for your workspace and deployment bucket.
- Consider adding a `ci` pipeline (GitHub Actions) for smoke tests.

## License
MIT

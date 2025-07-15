# My dbt Project Overview

This `README.md` provides a summary of the dbt (data build tool) project, focusing on the `dbt build` process and the generated `dbt docs`.

---

## 1. `dbt build` Process

The `dbt build` command is a crucial step in the data transformation workflow. It orchestrates the execution of data models, tests, and other operations defined in the dbt project.

### Execution Summary (Based on Screenshot 2025-07-11 183043.png)

**Note:** The image below is linked from Google Drive using a direct image URL format. Ensure the file is publicly shared. If the image still doesn’t display, click [here to view it](https://drive.google.com/file/d/1M9drJ9eJ9snjfAtQ9V0aW-LHcDDhb-JF/view?usp=sharing).

![dbt build execution log](https://drive.google.com/uc?export=view&id=1M9drJ9eJ9snjfAtQ9V0aW-LHcDDhb-JF)

The screenshot demonstrates a successful `dbt build` run with the following key outcomes:

* **Models Built:**
    * `analytics.stg_telegram_messages` (created as a SQL view)
    * `analytics.dim_channels` (created as a SQL view)
    * `analytics.dim_dates` (created as a SQL view)
    * `analytics.fct_messages` (created as a SQL view)
* **Data Tests Executed & Passed:** 14 out of 14 data tests completed successfully, ensuring data quality and integrity. These included:
    * `not_null` tests (e.g., `source_not_null_raw_telegram_messages_id`, `not_null_stg_telegram_messages_date`)
    * `unique` tests (e.g., `source_unique_raw_telegram_messages_id`)
    * `relationships` tests (e.g., `relationships_fct_messages_channel_id__channel_id__ref_dim_channels`)
* **Performance:** The entire build process, including compiling, running models, and executing tests, completed in **4.03 seconds** with a concurrency of 1 thread.
* **Resources Processed:** The build involved 4 models, 14 data tests, and 1 source.
* **Database Connection:** The build was executed against a `postgres-1.9.0` database instance within the `telegram-warehouse`.

---

## 2. `dbt docs generate` - Project Documentation

The `dbt docs generate` command creates a comprehensive and interactive web-based documentation for your dbt project. This documentation is invaluable for understanding the data lineage, model definitions, and data quality checks.

### Example: `raw.telegram_messages` Source (Based on Screenshot 2025-07-12 125104.png)

**Note:** The image below is linked from Google Drive using a direct image URL format. If it doesn't display, click [here to view it](https://drive.google.com/file/d/1GjBJ-oiuUkt_e-0nbSsDzATog6Xpjjyi/view?usp=sharing).

![dbt docs raw telegram messages](https://drive.google.com/uc?export=view&id=1GjBJ-oiuUkt_e-0nbSsDzATog6Xpjjyi)

The screenshot illustrates a view from the generated dbt documentation, specifically detailing the `raw.telegram_messages` source table:

* **Table Type:** Identified as a `source table`
* **Description:** "Raw data imported from Telegram messages."
* **Key Details:**
    * **Tags:** `untagged`
    * **Owner:** `postgres`
    * **Package:** `telegram_warehouse`
    * **Relation:** `telegram_db.raw.telegram_messages`
    * **Contract:** `Not Enforced`
    * **Loader:** `raw`
* **Columns:**
    * `id`: `bigint`, described as "Primary key" with associated data tests.
    * `date`: `timestamp without time zone`
    * `text`: `text`
    * `message`: `text`
    * `sender_id`: `bigint`
    * `media_type`: `text`

This interactive documentation provides a clear and accessible way for data consumers, analysts, and engineers to understand the data assets and their transformations within the project.

# Data Enrichment Log — Ethiopia Financial Inclusion Forecast

**Task:** 10Academy Week 11, Task 1 — Data Exploration and Enrichment
**Author:** Maria
**Date:** July 2026

## 1. Purpose

This log documents every record added to the starter dataset
(`ethiopia_fi_unified_data.xlsx`) during Task 1, and one significant
correction identified during exploration. It exists so that every
enrichment can be independently verified against its original source.

## 2. Methodology

Each addition follows a fixed documentation standard, matching the
schema's own requirements for new records:

| Field                              | Requirement                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| `source_url`                       | Direct link to the primary or best-available secondary source                      |
| `original_text`                    | Verbatim quote (under 15 words) supporting the figure                              |
| `confidence`                       | `high` = primary/official source; `medium` = secondary source citing a primary one |
| `collected_by` / `collection_date` | Attribution and recency tracking                                                   |
| `notes`                            | Why the record matters — what gap it fills                                         |

Candidate additions were prioritized by **temporal gap-filling**: indicators
with single-point snapshots or multi-year gaps between observations were
targeted first, since these limit trend/growth-rate analysis the most
(see Task 2 EDA, Dataset Overview section, for the sparsity assessment
that drove this prioritization).

## 3. Summary of Changes

| Metric        | Before | After          |
| ------------- | ------ | -------------- |
| Total records | 57     | 63             |
| Observations  | 30     | 34             |
| Events        | 10     | 12             |
| Impact links  | 14     | 14 (unchanged) |
| Targets       | 3      | 3 (unchanged)  |

## 4. Additions

### 4.1 Observations (4 added)

| ID       | Indicator                 | Value | Date       | Source                                                   | Confidence |
| -------- | ------------------------- | ----- | ---------- | -------------------------------------------------------- | ---------- |
| REC_0058 | Telebirr registered users | 21.8M | 2022-06-30 | Ethio Telecom (via Wikipedia)                            | Medium     |
| REC_0059 | Telebirr registered users | 34.3M | 2023-06-30 | Ethio Telecom 2022/23 Annual Business Performance Report | High       |
| REC_0060 | M-Pesa registered users   | 3.1M  | 2023-12-31 | Safaricom Ethiopia (via Technext)                        | High       |
| REC_0061 | 4G population coverage    | 44%   | 2024-12-31 | ITU (via Ecofin Agency)                                  | Medium     |

**Rationale:** Prior to these additions, `USG_TELEBIRR_USERS` and
`USG_MPESA_USERS` each had only a single 2024/2025 snapshot, making
growth-rate calculation impossible. `ACC_4G_COV` had a 2-year gap
(2023→2025) that these fill with an independent, cross-validating source.

### 4.2 Events (2 added)

| ID       | Event                                    | Date       | Category | Significance                                                                                                                                                                  |
| -------- | ---------------------------------------- | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EVT_0011 | Ethiopia Telecom Sector Liberalization   | 2021-05-01 | policy   | First competitively tendered telecom license, awarded to the Safaricom-led consortium — the root regulatory event enabling Safaricom's later market entry and M-Pesa's launch |
| EVT_0012 | NBE Payment Instrument Issuers Directive | 2020-04-01 | policy   | Established the regulatory framework permitting non-bank mobile money issuers; predates and enables Telebirr                                                                  |

**Rationale:** The original 10 events began with Telebirr's May 2021
launch. Both additions capture the regulatory groundwork that made
Telebirr and M-Pesa possible in the first place, extending the causal
chain one step further back than the starter dataset provided.

## 5. Correction: No 2011 Ethiopia Findex Data Exists

The Week 11 challenge document's own summary table lists a 2011
account-ownership figure of 14% for Ethiopia. Cross-referencing the
World Bank's 2014 Global Findex report shows Ethiopia was not part of
the Global Findex survey until the **2014 edition** — it was one of 9
countries added for the first time that year. No primary 2011 Ethiopia
Findex observation exists.

**Action taken:** No 2011 `ACC_OWNERSHIP` row was added to the dataset.
The starter dataset's existing omission of a 2011 observation is
correct and was left as-is, rather than "fixed" with a fabricated value
matching the (likely erroneous) doc figure.

## 6. Full Source List

1. Ethio Telecom / Wikipedia — https://en.wikipedia.org/wiki/Ethio_Telecom
2. Ethio Telecom 2022/23 Annual Business Performance Report — https://www.ethiotelecom.et/ethio-telecom-2022-23-annual-business-performance/
3. Technext (Safaricom M-Pesa reporting) — https://technext24.com/2024/02/07/safaricoms-m-pesa-3-1-m-users-ethiopia/
4. Ecofin Agency (ITU data) — https://www.ecofinagency.com/news-digital/0206-56088-ethiopias-incumbent-operator-extends-4g-coverage-to-52-new-cities
5. IFC / World Bank PPP (telecom liberalization) — https://ppp.worldbank.org/zh-hans/node/9571
6. Digital Policy Alert (NBE PII Directive) — https://digitalpolicyalert.org/event/25713-implemented-nbe-licensing-and-authorisation-of-payment-instrument-issuers-directive-no-onps012020

## Enrichment Round 2 — Task 4 Usage Target Series (2026-07-20)

Task 4 requires forecasting "% of adults who made or received a digital
payment," but no such indicator_code existed in the dataset — Usage was
previously represented only via operator proxies (Telebirr/M-Pesa users,
P2P/ATM volumes). Three Ethiopia-specific, Findex-anchored observations
were added to create a genuine forecastable target series.

### Added: REC_0062 — Digital payment adoption, 2017

- value_numeric: 12%
- source_url: https://blogs.worldbank.org/en/africacan/financial-inclusion-in-ethiopia-10-takeaways-from-findex-2017
- original_text: "Made or received digital payments in the past year (%) ... 12"
- confidence: high

### Added: REC_0063 — Digital payment adoption, 2021

- value_numeric: 20%
- source_url: https://blogs.worldbank.org/en/africacan/mobile-phone-technology-could-expand-equitable-access-financial-services-ethiopia
- original_text: "20% of adults—used their accounts for digital payments"
- confidence: high

### Added: REC_0064 — Digital payment adoption, 2024

- value_numeric: 35%
- source_url: internal_challenge_doc
- original_text: "Made or received digital payment: ~35%"
- confidence: medium (challenge doc's approximate figure, not independently re-verified against primary 2024 Findex source)
- notes: Lower confidence than the other two since this wasn't independently verified against a primary source

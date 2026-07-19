## Enrichment Round 1 — Telebirr user growth (2026-07-19)

### Finding: 2011 Ethiopia Findex data does not exist

Ethiopia was not included in the Global Findex survey until the 2014 edition
(confirmed: World Bank's 2014 Global Findex report lists Ethiopia as one of
9 countries added for the first time that year). The "2011: 14%" figure in
the Week 11 challenge doc's summary table appears to be an error — there is
no primary Findex source for Ethiopia in 2011. No 2011 ACC_OWNERSHIP row was
added; the dataset's existing omission of 2011 is correct as-is.

### Added: REC_0058 — Telebirr registered users, June 2022

- value_numeric: 21,800,000
- source_url: https://en.wikipedia.org/wiki/Ethio_Telecom
- original_text: "Frehiwot said 21.8 million users signed up with this service"
- confidence: medium (secondary source citing a company statement)
- collected_by: Maria
- collection_date: 2026-07-19
- notes: Fills gap between Telebirr's May 2021 launch and the existing 2025 data point (USG_TELEBIRR_USERS)

### Added: REC_0059 — Telebirr registered users, June 2023

- value_numeric: 34,300,000
- source_url: https://www.ethiotelecom.et/ethio-telecom-2022-23-annual-business-performance/
- original_text: "telebirr has 34.3 Million subscribers with a total transaction value"
- confidence: high (Ethio Telecom's own official annual report)
- collected_by: Maria
- collection_date: 2026-07-19
- notes: Second point establishing Telebirr's growth trajectory (2022 → 2023 → 2025)

### Added: REC_0060 — M-Pesa registered users, December 2023

- value_numeric: 3,100,000
- source_url: https://technext24.com/2024/02/07/safaricoms-m-pesa-3-1-m-users-ethiopia/
- original_text: "Safaricom, has posted 3.1 million M-PESA customers since its launch"
- confidence: high
- collected_by: Maria
- collection_date: 2026-07-19
- notes: Fills gap between M-Pesa's Aug 2023 launch and existing Dec 2024 data point (10.8M), establishing growth trajectory 3.1M → 10.8M

### Added: EVT_0011 — Telecom sector liberalization / first competitive license, May 2021

- source_url: https://ppp.worldbank.org/zh-hans/node/9571
- original_text: "the country's first competitively tendered telecommunications license was awarded"
- confidence: high
- collected_by: Maria
- collection_date: 2026-07-19
- notes: Root regulatory event enabling Safaricom's entry; distinct from EVT_SAFARICOM (market entry, Aug 2022) and EVT_MPESA (product launch, Aug 2023)

### Added: EVT_0012 — NBE Payment Instrument Issuers Directive, April 2020

- source_url: https://digitalpolicyalert.org/event/25713-implemented-nbe-licensing-and-authorisation-of-payment-instrument-issuers-directive-no-onps012020
- original_text: "the National Bank of Ethiopia (NBE) issued the Licensing and Authorisation of Payment Instrument Issuers Directive"
- confidence: high
- collected_by: Maria
- collection_date: 2026-07-19
- notes: Regulatory foundation enabling non-bank mobile money issuers (Telebirr, later M-Pesa); earliest event in the dataset

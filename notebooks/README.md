## Data Quality Assessment

- 76.2% of records are high confidence, 23.8% medium, 0% low
- Only 4 of ~20 indicators have enough observations (3+) for trend analysis:
  ACC_OWNERSHIP (6), ACC_4G_COV (3), ACC_FAYDA (3), USG_TELEBIRR_USERS (3)
- 11 indicators are single-point snapshots — useful as context/baseline,
  not for trend or growth-rate analysis
- Usage pillar has no single Findex-style "% adults" observation; it's
  reconstructed entirely from operator proxy metrics

## Data Gap: No urban/rural disaggregation

All 63 records have `location = "national"`; the `region` field is empty
throughout. Urban vs. rural account ownership comparison (requested in
Task 2) cannot be performed with the current dataset — this would require
pulling Findex microdata directly (individual-level survey responses),
which is outside this dataset's scope. Documented as a limitation.

## Why did Account Ownership stagnate (2021→2024, only +3pp) despite mobile money growth?

1. **Mobile money accounts are likely additive, not incremental-to-unbanked.** Mobile Money Account Rate rose only 4.7%→9.45% (2021-2024) — a small slice of the population — while Telebirr alone claims 55M registered users. Many new mobile money signups are likely existing bank customers adding a wallet, not previously-unbanked adults gaining their first account.

2. **Registered ≠ active.** M-Pesa shows a direct registered-vs-active gap in this data: 10.8M registered but only 7.1M 90-day active (66% activity rate, `USG_ACTIVE_RATE`). If Telebirr has a similar gap, a large share of "55M users" may not clear Findex's usage bar to count as financially included.

3. **Timing mismatch.** Most Telebirr growth (21.8M in 2022 → 34.3M in 2023 → 55M in 2025) happened after the 2021 Findex survey was already fielded. The 2024 survey only captured ~2.5 years of that growth, likely concentrated among already-banked, urban, mobile-literate adopters first.

## Correlation Analysis: Why we did not compute correlation coefficients

The four indicators with enough points to be "trend-worthy" (ACC_OWNERSHIP,
ACC_4G_COV, ACC_FAYDA, USG_TELEBIRR_USERS) never share a common observation
date — Findex surveys occur every 3 years, while operator/infrastructure
data is reported on ad-hoc or quarterly schedules. Computing a numeric
correlation across 3-4 misaligned points would produce a spurious,
non-meaningful coefficient rather than real evidence of association.

Instead, association is assessed qualitatively via the event-timeline
overlay (Step 5): infrastructure and product-launch events cluster
overwhelmingly in 2022-2025, while the last two Findex survey points
(2021, 2024) bracket that entire period. This means we cannot yet
statistically attribute the 2021→2024 Access growth to any specific
event — we can only say the events happened within the window, which is
a necessary but not sufficient basis for causal claims. This is precisely
why the impact_link records use comparable-country evidence (Kenya,
Rwanda, India, Tanzania) rather than in-country statistical correlation —
there isn't enough overlapping in-country data yet to support it directly.

## Insights from impact_link records

14 modeled relationships exist, using comparable-country evidence (Kenya,
Rwanda, India, Tanzania) since in-country statistical correlation isn't
yet supportable (see above). The strongest documented link is Telebirr →
Account Ownership (IMP_0001: +15pp estimated, 12-month lag, Kenya
precedent) — this is the single largest hypothesized effect in the
dataset and the most important one to validate once more Findex data
becomes available.

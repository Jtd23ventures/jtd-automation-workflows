# Compare competitor Facebook and Instagram ads

Use the [JTD Competitor Ad Change Tracker](https://apify.com/jtd23ventures/competitor-ad-change-tracker) with two existing Apify datasets from comparable Meta Ad Library searches.

## Quick start

1. Collect two snapshots with the same advertiser, filters and coverage using your preferred permitted data source. Keep their dataset IDs.
2. Download `compare.py`. Install Python 3.9 or later; no packages required.
3. Set `APIFY_TOKEN` in your local environment. Never commit your token.
4. Run `python compare.py PREVIOUS_DATASET_ID CURRENT_DATASET_ID --max-cost 0.10`.

The script prints JSON changes. Redirect stdout to a local JSON file if desired. The cap applies to the tracker, not upstream collection. Pricing is $0.005 per detected change plus $0.00005 per start; a $0.10 cap allows at most 19 results at these prices. Check current Store pricing. A capped result may be incomplete; consult the Actor run summary in Apify.

## Example output (illustrative)

```json
[{"adArchiveId":"101","event":"changed","changedFields":["text"],"before":{"text":"Old offer"},"after":{"text":"New offer"}}]
```

Supported events: newly_observed, changed, not_observed. Missing ads are not necessarily discontinued. No inference of ad spend, profitability or performance. The script compares supplied snapshots; it does not collect ads, schedule runs, or send alerts. Test with your own datasets before scheduling. This starter has not yet been end-to-end tested against live scraper datasets.

## Daily workflow

Schedule your permitted scraper, retain the previous successful snapshot, compare with the current successful snapshot, review changes, then advance your baseline. Do not advance on failed or incomplete collection. For a complete report, verify the run summary says truncated=false before advancing.

Open an issue for integration requests.

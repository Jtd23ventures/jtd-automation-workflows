# n8n: Compare competitor Meta ads with Apify

Import `n8n-workflow.json` into n8n. In Configure snapshots, replace both placeholders with existing accessible Apify dataset IDs from equivalent successful Meta Ad Library collections. In Compare ads with JTD, create a Header Auth credential with name `Authorization` and value `Bearer YOUR_APIFY_TOKEN` (never commit or share the token). Run manually and inspect output. Default tracker cap is $0.10; at $0.005 per result plus $0.00005 start, this allows 19 results. Upstream scraping costs separately. Check the Actor run summary for truncation before treating the report as complete. Missing ads do not prove discontinuation. This starter does not scrape, schedule, persist baselines or send notifications. No n8n runtime test has been performed yet; verify import and execution before submitting to the template directory.

[Actor listing](https://apify.com/jtd23ventures/competitor-ad-change-tracker)

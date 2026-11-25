"""Compare two existing Apify ad datasets. Python 3.9+, standard library only."""
import argparse
import json
import os
import urllib.request
import urllib.parse
from decimal import Decimal

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("previous")
    p.add_argument("current")
    p.add_argument("--max-cost", type=Decimal, required=True)
    args = p.parse_args()
    if not args.max_cost.is_finite() or args.max_cost < Decimal("0.01"):
        p.error("max-cost must be finite and at least 0.01 USD")
    for value in (args.previous, args.current):
        if not value.isascii() or not value.isalnum():
            p.error("Supply dataset IDs, not URLs")
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        p.error("Set APIFY_TOKEN in your environment")
    base = "https://api.apify.com/v2"
    def request(path, payload=None):
        req = urllib.request.Request(base + path,
            data=None if payload is None else json.dumps(payload).encode(),
            headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as response:
            return json.load(response)
    query = urllib.parse.urlencode({"maxTotalChargeUsd": str(args.max_cost), "memory": 128, "timeout": 60})
    run = request("/acts/jtd23ventures~competitor-ad-change-tracker/run-sync-get-dataset-items?" + query,
                  {"previousDatasetId": args.previous, "currentDatasetId": args.current})
    print(json.dumps(run, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

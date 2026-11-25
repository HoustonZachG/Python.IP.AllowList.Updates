# Python.IP.AllowList.Updates

# Automated IP Allow-List Governance (Python)

## Overview
Routine access control audits are essential for preventing unauthorized access to restricted subnetworks containing sensitive healthcare and enterprise data. This Python utility automates the review of a network allow list (`allow_list.txt`) by cross-referencing approved IP addresses against a revocation list (`remove_list`) and updating the configuration file automatically.

## Key Skills Demonstrated
* **File Handling & Resource Safety:** Using Python `with` statements (`"r"` and `"w"` modes) to safely read and overwrite files without memory leaks or file corruption.
* **Data Parsing & Manipulation:** Converting raw text strings into structured lists using `.split()` and `.join()` for programmatic inspection.
* **Conditional Filtering:** Iterating through active network entries (`for` loop + `if` conditional) to revoke unauthorized IP addresses.

## How It Works
1. **Ingest & Parse:** Opens `allow_list.txt` in read mode and splits the continuous string into a list of individual IP addresses.
2. **Audit & Revoke:** Iterates through the allow list and removes any IP address matching an entry in `remove_list`.
3. **Update Configuration:** Joins the remaining authorized IP addresses back into a space-separated string and overwrites `allow_list.txt`.

#!/usr/bin/env python3
"""No-op configure hook for the capability-neutral World Model skeleton."""

from __future__ import annotations

import json


if __name__ == "__main__":
    print(json.dumps({
        "schema": 1,
        "pack": "world",
        "status": "configured",
        "capabilities": [],
        "writes": [],
    }, sort_keys=True))

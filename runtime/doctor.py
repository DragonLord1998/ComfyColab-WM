#!/usr/bin/env python3
"""Report the intentional zero-capability World Model state."""

from __future__ import annotations

import json


if __name__ == "__main__":
    print(json.dumps({
        "schema": 1,
        "pack": "world",
        "status": "ok",
        "capabilities": [],
        "public_node_ids": [],
        "dependencies": [],
        "network_used": False,
        "writes": [],
    }, sort_keys=True))

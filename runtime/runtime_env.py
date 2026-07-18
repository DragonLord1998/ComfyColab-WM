#!/usr/bin/env python3
"""Emit the intentionally empty World Model environment contribution."""

from __future__ import annotations

import json


if __name__ == "__main__":
    print(json.dumps({"schema": 1, "pack": "world", "environment": {}}, sort_keys=True))

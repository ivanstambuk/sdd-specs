#!/usr/bin/env python3
"""
Lightweight placeholder for spec linting.

Intended to be extended to enforce style rules beyond schema validation
(e.g., naming patterns, required sections in spec.md).
"""

import sys


def main() -> int:
  print("lint-specs.py: no-op placeholder (extend for real linting).")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())


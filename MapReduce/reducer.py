#!/usr/bin/env python3
import sys
from collections import defaultdict

scores = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        category, word, rating = line.split('\t')
        rating = float(rating)
        key = f"{category}\t{word}"
        scores[key].append(rating)
    except:
        continue

for key, rating_list in scores.items():
    avg = sum(rating_list) / len(rating_list)
    print(f"{key}\t{avg:.2f}")

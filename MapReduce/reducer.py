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
        scores[(category, word)].append(rating)
    except:
        continue

category_groups = defaultdict(list)

for (category, word), rating_list in scores.items():
    avg = sum(rating_list) / len(rating_list)
    category_groups[category].append((word, avg))

for category in sorted(category_groups.keys()):
    
    reverse = True if category == "positive" else False
    sorted_items = sorted(category_groups[category], key=lambda x: x[1], reverse=reverse)
    
    for word, avg in sorted_items:
        print(f"{category}\t{word}\t{avg:.2f}")

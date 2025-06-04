#!/usr/bin/env python3
import sys
from collections import defaultdict

scores = defaultdict(list)

# Read and group ratings per (category, word)
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

# Calculate average and count
for (category, word), rating_list in scores.items():
    count = len(rating_list)
    avg = sum(rating_list) / count
    category_groups[category].append((word, avg, count))

# Print output sorted by average rating
for category in sorted(category_groups.keys()):
    reverse = True if category == "positive" else False
    sorted_items = sorted(category_groups[category], key=lambda x: x[1], reverse=reverse)
    
    for word, avg, count in sorted_items:
        # print(f"{category}\t{word}\t{avg:.2f}\t{count}")
        print(f"{category:<10}\t\t{word:<10}\t\t{avg:.2f}\t\t{count}")

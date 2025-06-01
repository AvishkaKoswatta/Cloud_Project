#!/usr/bin/env python3
import sys
import string

stopwords = set([
    "the", "is", "are", "was", "were", "and", "or", "of", "to", "in", "on", "it",
    "this", "that", "with", "as", "for", "an", "a", "at", "by", "be", "from", "has",
    "have", "had", "but", "not", "so", "if", "they", "them", "we", "you", "i", "my",
    "me", "he", "she", "him", "her", "its", "our", "your", "their", "just", "do",
    "did", "does", "done", "up", "down", "out", "into", "over", "under", "all",
    "some", "more", "very", "can", "will", "would", "could", "should", "no", "yes"
])

positive_words = set([
    "amazing", "awesome", "great", "good", "love", "fun", "cool", "nice", "perfect", "excellent"
])

negative_words = set([
    "bad", "worst", "terrible", "boring", "waste", "crash", "buggy", "hate", "slow", "poor"
])

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        text, rating = line.rsplit('\t', 1)
        rating = float(rating)
    except:
        continue

    words = text.lower().split()
    for word in words:
        word = word.strip(string.punctuation)

        if word.isalpha() and len(word) >= 3 and word not in stopwords:
            if word in positive_words:
                print(f"positive\t{word}\t{rating}")
            elif word in negative_words:
                print(f"negative\t{word}\t{rating}")

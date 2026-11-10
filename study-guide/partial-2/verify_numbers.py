"""Deterministic arithmetic checks for LDS1071 Midterm II worked examples.

Run from the repository root:
    python study-guide/partial-2/verify_numbers.py
No third-party dependencies.
"""
from math import isclose, log10, sqrt

# Exercise 1: K-means means, inertia, and assignment stability.
points = [1, 3, 9, 12]
centers = [sum(points[:2]) / 2, sum(points[2:]) / 2]
assert centers == [2.0, 10.5]
assert isclose(sum((x - (centers[0] if i < 2 else centers[1])) ** 2
                   for i, x in enumerate(points)), 6.5)
assert [(0 if abs(x - centers[0]) <= abs(x - centers[1]) else 1)
        for x in points] == [0, 0, 1, 1]

# Exercise 2: successive inertia improvements.
inertia = [900, 440, 210, 185, 170]
assert [a-b for a, b in zip(inertia, inertia[1:])] == [460, 230, 25, 15]

# Exercise 4: model selection chooses minimum criterion.
assert [790, 620, 574, 590].index(min([790, 620, 574, 590]))+1 == 3
assert [775, 585, 520, 515].index(min([775, 585, 520, 515]))+1 == 4

# Exercise 5: distances and linkage merge heights.
locations = {'A': 0, 'B': 3, 'C': 7, 'D': 13}
assert abs(locations['B']-locations['D']) == 10
assert min(abs(locations[x]-locations['C']) for x in ['A', 'B']) == 4
assert max(abs(locations[x]-locations['C']) for x in ['A', 'B']) == 7
assert min(abs(locations[x]-locations['D']) for x in ['A', 'B', 'C']) == 6
assert max(abs(locations[x]-locations[y])
           for x in ['A', 'B'] for y in ['C', 'D']) == 13

# Exercise 7: silhouette coefficients.
assert isclose((9-3)/max(3, 9), 2/3)
assert isclose((4-5)/max(5, 4), -1/5)

# Exercise 8: PCA explained-variance sequence.
eigs = [6, 2, 1, 1]
assert [v/sum(eigs) for v in eigs] == [0.6, 0.2, 0.1, 0.1]
assert 0.8 < 0.85 <= 0.9

# Exercise 10: counts by exact fixed vocabulary.
docs = ['modelo aprende modelo', 'datos aprende', 'modelo datos datos']
vocab = ['modelo', 'aprende', 'datos']
counts = [[doc.split().count(token) for token in vocab] for doc in docs]
assert counts == [[2, 1, 0], [0, 1, 1], [1, 0, 2]]
assert [[int(value > 0) for value in row] for row in counts] == [
    [1, 1, 0], [0, 1, 1], [1, 0, 1]]

# Exercise 11: use EXACT unsmoothed base-10 convention.
assert log10(1000/10) == 2
assert log10(1000/100) == 1
assert isclose((1+log10(2))*2, 2.6020599913, abs_tol=1e-8)
assert (1+log10(10))*1 == 2
assert log10(1000/1000) == 0

# Exercise 12: cosine similarities.
u, v, w = (2, 0, 1), (1, 0, 2), (0, 3, 0)
cosine = lambda a, b: (sum(x*y for x, y in zip(a, b)) /
                       sqrt(sum(x*x for x in a)*sum(y*y for y in b)))
assert isclose(cosine(u, v), 0.8)
assert isclose(cosine(u, w), 0)
assert isclose(cosine(u, tuple(3*x for x in u)), 1)

# Exercise 15: classification metrics, positive == 'urgent'.
tp, fp, fn, tn = 30, 10, 15, 65
assert tp+fp+fn+tn == 120
assert isclose((tp+tn)/120, 95/120)
assert isclose(tp/(tp+fp), 0.75)
assert isclose(tp/(tp+fn), 2/3)
assert isclose(2*tp/(2*tp+fp+fn), 12/17)

# Exercise 16: only the point-estimate difference is derivable.
assert isclose(0.83-0.81, 0.02)
print('All Midterm II arithmetic checks passed.')

# Additional numerical example: DBSCAN (epsilon-neighborhood includes the point).
from math import dist, exp
coordinates = [(0, 0), (1, 0), (0, 1), (2, 0),
               (6, 0), (7, 0), (6, 1), (10, 10)]
neighborhoods = [[j + 1 for j, v in enumerate(coordinates)
                  if dist(u, v) <= 1.1 + 1e-12]
                 for u in coordinates]
assert neighborhoods == [[1, 2, 3], [1, 2, 4], [1, 3], [2, 4],
                         [5, 6, 7], [5, 6], [5, 7], [8]]
core = {i+1 for i, neigh in enumerate(neighborhoods) if len(neigh) >= 3}
assert core == {1, 2, 5}
border = {j for i in core for j in neighborhoods[i-1]} - core
assert border == {3, 4, 6, 7}
assert set(range(1, 9)) - core - border == {8}
assert dist(coordinates[3], coordinates[4]) == 4.0

# Additional numerical example: constrained 1D two-Gaussian EM iteration.
observations = [0.0, 1.0, 3.0]
gamma1 = [exp(-(x-0)**2/2) / (exp(-(x-0)**2/2)+exp(-(x-3)**2/2))
          for x in observations]
gamma2 = [1-g for g in gamma1]
assert all(isclose(x, y, abs_tol=1e-6)
           for x, y in zip(gamma1, [0.989013, 0.817574, 0.010987]))
n1, n2 = sum(gamma1), sum(gamma2)
assert isclose(n1, 1.8175744762, abs_tol=1e-8)
assert isclose(n1/3, 0.6058581587, abs_tol=1e-8)
mu1 = sum(x*g for x, g in zip(observations, gamma1))/n1
mu2 = sum(x*g for x, g in zip(observations, gamma2))/n2
assert isclose(mu1, 0.4679507306, abs_tol=1e-8)
assert isclose(mu2, 2.6635628481, abs_tol=1e-8)

# Additional numerical example: average, centroid, and Ward linkage.
assert isclose((7+4)/2, 5.5)
assert isclose((13+10+6)/3, 29/3)
assert isclose(abs((0+3+7)/3-13), 29/3)
ward = lambda n_u, n_v, mu_u, mu_v: (n_u*n_v/(n_u+n_v))*(mu_u-mu_v)**2
assert isclose(ward(1, 1, 0, 3), 4.5)
assert isclose(ward(2, 1, 1.5, 7), 121/6)
assert isclose(ward(1, 1, 7, 13), 18)
assert isclose(ward(2, 1, 1.5, 13), 529/6)
assert isclose(ward(2, 2, 1.5, 10), 72.25)

# Additional numerical example: BPE, with per-word boundaries and documented ties.
from collections import Counter
word_tokens = {'set': ['s','e','t'], 'new': ['n','e','w'],
               'renew': ['r','e','n','e','w'], 'reset': ['r','e','s','e','t']}
frequencies = {'set': 1, 'new': 2, 'renew': 2, 'reset': 1}
def pair_counts():
    return Counter({pair: total for pair, total in
        ((pair, sum(freq*sum(a == pair[0] and b == pair[1]
                        for a,b in zip(seq, seq[1:]))
                    for word,seq in word_tokens.items()
                    for freq in [frequencies[word]]))
         for pair in {(a,b) for seq in word_tokens.values()
                       for a,b in zip(seq,seq[1:])})})
initial_pairs = pair_counts()
assert initial_pairs == Counter({('s','e'):2, ('e','t'):2, ('n','e'):4,
                                 ('e','w'):4, ('r','e'):3, ('e','n'):2,
                                 ('e','s'):1})
def do_merge(pair):
    new = ''.join(pair)
    for word, seq in word_tokens.items():
        updated, idx = [], 0
        while idx < len(seq):
            if idx+1 < len(seq) and (seq[idx],seq[idx+1]) == pair:
                updated.append(new)
                idx += 2
            else:
                updated.append(seq[idx])
                idx += 1
        word_tokens[word] = updated
for pair, count in [(('n','e'),4),(('ne','w'),4),(('r','e'),3),(('re','new'),2)]:
    scores = pair_counts()
    assert scores[pair] == max(scores.values()) == count
    do_merge(pair)
assert word_tokens == {'set': ['s','e','t'], 'new':['new'],
                       'renew':['renew'], 'reset':['re','s','e','t']}

# Additional numerical example: log-TF, unsmoothed IDF, and cosine ranking.
words = ['sweet', 'nurse', 'love', 'how', 'sorrow', 'is']
corpus = ['sweet sweet nurse love', 'sweet sorrow',
          'how sweet is love', 'nurse']
idf = {word: log10(4/sum(word in d.split() for d in corpus)) for word in words}
assert isclose(idf['sweet'], log10(4/3))
assert isclose(idf['love'], log10(2))
assert isclose(idf['how'], log10(4))
def tfidf(text):
    tokens = text.split()
    return [(1+log10(tokens.count(word)))*idf[word] if word in tokens else 0.0
            for word in words]
query = tfidf('sweet love')
scores = [cosine(query, tfidf(doc)) for doc in corpus]
assert all(isclose(a,b, abs_tol=1e-6) for a,b in zip(
    scores, [0.7468654212, 0.0778893249, 0.3574976314, 0.0]))
assert sorted(range(4), key=lambda i: scores[i], reverse=True) == [0,2,1,3]
assert isclose((10000-100)/10000, 0.99)

print('All additional BPE, search, DBSCAN, GMM, and linkage checks passed.')

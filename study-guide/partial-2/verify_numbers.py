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

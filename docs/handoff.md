# Agent handoff

## Lecture PDF naming pass

- Scope: rename the twelve newly uploaded PDFs numbered 15–26 in `course-material/lectures/`, while retaining their exact Git blob SHA (byte-for-byte preservation).
- Conventions: `NN_Topic-1_Topic-2.pdf` from `README.md`; the lecture number remains the number of the original uploaded filename.
- Evidence: top navigation/first slides were inspected for classes 16–26; the topics appear in `docs/course-map.md`. Class 15 was over the connector's available PDF text-reading size; its descriptive title includes PCA based on lecture 16's explicit opening PCA review and the dimensionality-reduction sequence. Inspect the class-15 agenda if/when raw-file access becomes available and refine only if necessary.
- Class 22's PDF cover labels itself “Sesión 21”, although its uploaded filename was “Clase 22 ML (1).pdf”. Do not silently modify numbering; reconcile against the official course plan if a conflicting class number matters.
- The lecture-14 PDF is absent and was not created.
- No notebooks, original PDF contents, or other course artifacts were modified by the renaming pass.

## Next steps
- If additional lectures are uploaded, inspect opening agenda/navigation, rename consistently, and extend `docs/course-map.md`.

# Manuscript conversion checks

- Converted the finished paper/main.tex and every included section and table with installed official Pandoc 3.3.
- Mathematics was protected before prose conversion; custom norm, expectation, real-number, differential and operator macros were expanded to standard KaTeX-compatible LaTeX.
- Compiled main.aux supplied the equation, theorem, section, figure and table references. All 33 numbered equations were preserved; 28 labeled equation positions were cross-checked against the compiled numbering.
- Preserved 7 complete proofs, 6 propositions and 1 corollary. Proof end marks are explicit.
- Protected 216 inline and 40 display-math segments (including proof end marks). Numbered aligned expressions retain their number on the corresponding row.
- Preserved all seven numerical table rows, two figure captions, source transcriptions, eight compiled bibliography entries and their existing source/DOI links, and both execution-code blocks.
- Figure links target the public GitHub raw PNG paths requested by the parent. No local path, unresolved reference, unsupported author macro or placeholder remains.
- Taylor Kalin is the sole author in the header. ORCID and contact details are retained. Author/methods disclosure remains a separate section, and the dissemination disclosure is preserved.
- Manuscript length: 43600 characters; title 129 characters; abstract 1505 characters.
- Source main.tex SHA-256: 1a961cb3f2ac472c2689b7192d46deabaecf811ba70bdc568602fa582bdcf4b1.
- Conversion verified preservation and formatting, not an independent scientific peer review.

- Synchronized the final funding/competing-interests paragraph and the corrected scientific notation in the numerical table after the initial conversion; equation and proof counts are unchanged.

- Joined the split appendix source hash into one inline code value; no mathematical content changed.
- Updated the funding paragraph after Taylor Kalin confirmed self-funding; no mathematical content changed.

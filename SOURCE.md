# Source and scope

The object examined is **arXiv:2609.28999v2**, by Thibault Fredon, Abhay K. Ram,
Fabrice Debbasch, Julien Zylberman, and Nuno F. Loureiro, *On the numerical
limitations of dual Koopman von Neumann embeddings for solving conservative
nonlinear ordinary differential equations on quantum computers*.

- [Versioned abstract](https://arxiv.org/abs/2609.28999v2)
- [Versioned PDF](https://arxiv.org/pdf/2609.28999v2)
- [Versioned HTML](https://arxiv.org/html/2609.28999v2)
- First submission: 24 September 2026; v2 revision: 25 September 2026.
- PDF length: 17 pages; byte length: 959,353.
- SHA-256: `f895d195c935bcc9e3d0b14d2499f59aa497b8fcdce7d69f13fbc74d10301add`.
- The user-supplied PDF and a fresh download of the versioned arXiv PDF are
  byte-identical.

On 28 October 2026, the official arXiv record still listed v2 as its latest
version and did not list a journal reference. A bounded search of the exact
identifier/title with correction and erratum terms did not identify a dedicated
correction. That search does not establish that none exists. No claim is made
about an unexamined manuscript, future revision, or version of record.

Equation references in this note use the **PDF numbering**. The HTML converter
renumbers some appendix equations, so a different HTML equation number is not
itself an error in the original work. Targeted formulas and assumptions were
checked against the PDF's rendered pages as well as extracted text.

The central target passages are:

| PDF location | Subject |
|---|---|
| pp. 5-6, Eqs. (30)-(31); p. 13, Eq. (C1) | Geometric separation definition and small-deformation criterion |
| pp. 14-15, Eqs. (D6)-(D10) and following prose | Phase fringe, variance, and claimed inference limit |
| p. 6, Section V after Eq. (35) | Sampling-cost covariance prefactor |
| pp. 5 and 7, Eqs. (22)-(25), (45) | Ehrenfest-Reynolds definitions and Lotka-Volterra calibration |
| p. 6, Eq. (35) and preceding regularity assumption | Gaussian observable expansion and remainder |
| p. 12, Appendix B.2 | Covariance evolution and matrix-norm estimate |

The original paper correctly identifies the distinction between the evolution
of a probability distribution and that of its mean. Its Gaussian/moment closure
and constant-covariance approximation are explicitly disclosed. This correction
does not count those disclosed assumptions as newly discovered errors, and does
not claim that the Koopman-von Neumann framework or all quantum nonlinear-ODE
solvers fail.

The original PDF is not redistributed in this repository. Its arXiv license is
the perpetual nonexclusive distribution license, not a blanket license for a
third party to relicense it. Short attributed quotations and targeted formulas
support the mathematical criticism; the new manuscript, proofs, code, and plots
are separate work.

# Primary references checked

The bibliography contains eight relevant primary works. Full-text PDFs were
opened and the portions used in the manuscript were inspected. Bibliographic
DOIs and publication metadata were checked against official arXiv/publisher
records and Crossref registration metadata where applicable.

| Key | Work and verified identifier | Role |
|---|---|---|
| `original` | Fredon et al., arXiv:2609.28999v2 | Audited source |
| `bhmt` | Brassard et al. (2002), DOI [10.1090/conm/305/05215](https://doi.org/10.1090/conm/305/05215) | Standard amplitude estimation, Theorem 12 |
| `aaronsonrall` | Aaronson and Rall (2020), DOI [10.1137/1.9781611976014.5](https://doi.org/10.1137/1.9781611976014.5); checked arXiv:1908.10846v6 | QFT-free amplitude estimation, Section 3 |
| `rall` | Rall (2020), DOI [10.1103/PhysRevA.102.022408](https://doi.org/10.1103/PhysRevA.102.022408); arXiv:2004.06832v3 | Observable estimation, Lemma 5 |
| `joseph` | Joseph (2020), DOI [10.1103/PhysRevResearch.2.043102](https://doi.org/10.1103/PhysRevResearch.2.043102); arXiv:2003.09980v4 | KvN simulation and observable estimation context |
| `transport` | Zylberman et al., arXiv:2508.15691v2 | Related split transport construction |
| `rallcoherent` | Rall (2021), DOI [10.22331/q-2021-10-19-566](https://doi.org/10.22331/q-2021-10-19-566); checked arXiv:2103.09717v4 | Coherent estimation assumptions and query accounting |
| `montanaro` | Montanaro (2015), DOI [10.1098/rspa.2015.0301](https://doi.org/10.1098/rspa.2015.0301); checked arXiv:1504.06987v3 | Variance-aware mean estimation and sampling distinction |

Version distinctions matter: Aaronson-Rall v6 explicitly corrects an earlier
algebraic error and numbers its amplitude-estimation statement Theorem 3.
Rall's 2021 publisher page identifies v3 as the published version and v4 as a
later benchmarking correction. Montanaro v3 corrects a total-variation-distance
complexity result. This note uses those works for their specified estimation
results and does not equate their checked preprints with every published detail.

The source-specific counterexamples are the contribution of this correction.
The characteristic-function identity, elementary covariance identities,
Taylor estimates, and standard amplitude-estimation algorithms are not claimed
as new general theory.

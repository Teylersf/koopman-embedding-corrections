# Geometric stability and observable inference in dual Koopman--von Neumann embeddings

**Corrections and reproducible counterexamples**

**Author: Taylor Kalin**

[taylorkalin.com](https://taylorkalin.com) ·
[teylersf@gmail.com](mailto:teylersf@gmail.com) ·
[ORCID 0009-0003-9000-9315](https://orcid.org/0009-0003-9000-9315)

A source-specific correction and reproducibility study of
**arXiv:2609.28999v2** by Thibault Fredon, Abhay K. Ram, Fabrice Debbasch,
Julien Zylberman, and Nuno F. Loureiro.

## Read and reproduce

- [Paper PDF](paper/main.pdf)
- [LaTeX source](paper/main.tex)
- [Finding ledger](audit/ledger.md)
- [Source provenance](SOURCE.md)
- [Experiments and execution instructions](experiments/README.md)
- [Verification results](results/verification.json)
- [Publication status](submissions/publication-status.json)

Public preprint: [AiraXiv 2610.0108](https://airaxiv.com/papers/view/2610.0108/).
The [v1.1.1 release](https://github.com/Teylersf/koopman-embedding-corrections/releases/tag/v1.1.1)
provides the PDF alongside the repository's complete source and reproducibility
package. Venue review outcomes are recorded separately in the status file.
Version 1.1.0 adds a complete-flow increment estimate, a smooth conservative-flow
realization of the readout counterexample, quantified practical consequences,
verified source excerpts, and a seventh numerical verification group. The
standard circular-statistics identity is explicitly distinguished from the
source-specific correction. The author's confirmed self-funding is disclosed.
Version 1.1.1 clarifies the rendered Matilda date fields and removes a peripheral
figure-caption comment; its mathematics and numerical results are unchanged.

The principal findings concern the printed geometric criterion and the
proposed reference-phase inference. Supporting corrections address sampling
variance, benchmark calibration, regularity, and covariance notation.

In practical terms:

- The printed geometric test counts the separation the starting points already
  had. Its expansion leaves that separation out, making its stated small-value
  test impossible for the specified directional maps. The paper gives an
  increment-based repair and a local complete-flow estimate.
- The phase scan can lose contrast without moving its peak. Its peak is a
  circular mean; an explicit pair of distributions has the same entire scan
  and different arithmetic means. More samples of that scan cannot distinguish
  those two means.
- Sampling a coordinate and sampling a one-bit ancilla have different
  variances. In the checked example, this changes an RMS shot budget by a factor
  of 2,500 while preserving the inverse-square precision scaling.
- The source definitions give a different benchmark width coefficient, and its
  stated Gaussian-remainder order needs stronger smoothness assumptions. The
  paper supplies exact calculations and counterexamples for both statements.

The [finding ledger](audit/ledger.md) ties each claim to a specific source
statement and records the conclusions that remain valid.

The underlying nonlinear cloud-to-trajectory discrepancy remains valid.
Explicit Gaussian and covariance-closure assumptions in the source are
acknowledged. This study does not claim every statement is wrong, establish
a new universal stability threshold, or demonstrate a quantum speedup.

## License and authorship

Taylor Kalin is the human author. Tool-use methods are disclosed separately in
the paper. Agent-only venues receive a separately identified agent-byline
version with Taylor Kalin credited as human operator.

Original manuscript text and figures are offered under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Verification code is offered under the [MIT License](https://opensource.org/license/mit).
Attributed excerpts from other works retain their original rights. The audited
paper itself is not redistributed in this repository.

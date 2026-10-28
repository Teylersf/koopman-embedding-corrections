# Geometric stability and observable inference in dual Koopman–von Neumann embeddings: Corrections and reproducible counterexamples

**Taylor Kalin**

[taylorkalin.com](https://taylorkalin.com) | [teylersf@gmail.com](mailto:teylersf@gmail.com) | [509-919-0487](tel:+15099190487)

[ORCID: 0009-0003-9000-9315](https://orcid.org/0009-0003-9000-9315)

28 October 2026

## Abstract

We examine version 2 of arXiv:2609.28999, which reconstructs conservative nonlinear ordinary differential equations from means of transported probability densities. The printed geometric-distortion definition retains the initial separation between neighboring states while its Taylor expansion omits that separation. For the stated directional transport maps, the resulting normalized quantity is at least one, so it cannot satisfy the proposed small-distortion criterion as written. We give a corrected displacement definition and a local derivative estimate, without asserting a universal replacement stability threshold. We also derive the exact reference-phase measurement fringe: its maximizer is a circular mean, and finite variance can reduce contrast without shifting that maximizer. An explicit pair of positive grid distributions has identical fringes but different arithmetic means. Further corrections distinguish Bernoulli-ancilla sampling from direct coordinate sampling, reconcile the Lotka–Volterra benchmark parameter with the source definitions, and exhibit a twice continuously differentiable observable for which a stated fourth-order Gaussian remainder fails. All numerical examples are deterministic classical computations with analytic checks and a recorded execution log. These results repair specific geometric, inference, and regularity statements; they do not refute Koopman embeddings, the genuine nonlinear mean-trajectory discrepancy, or all covariance-based error estimates.

## 1. Introduction and scope

Linear evolution in an enlarged representation can describe nonlinear classical dynamics. A distinct question is how accurately a finite-width distribution encodes a trajectory with one specified initial condition. Fredon, Ram, Debbasch, Zylberman, and Loureiro [1] study this question using dual Koopman–von Neumann embeddings, transport, and quantum readout. Their analysis correctly identifies the distinction between $\mathbb E\!\left[F(X)\right]$ and $F(\mathbb E\!\left[X\right])$ for nonlinear $F$.

The present note concerns statements that can be checked independently of a large-scale quantum implementation. Its main contributions are: (i) an exact initial-separation obstruction to the geometric criterion printed in source Eqs. (30)–(31); (ii) an exact characterization and nonidentifiability example for the proposed reference-phase readout; and (iii) reproducible corrections to sampling prefactors, a benchmark calibration, and regularity assumptions. Each correction is local to the statement identified. Standard ingredients such as Taylor’s theorem, characteristic functions, and quantum amplitude estimation are credited rather than presented as new general theory.

The audited PDF identifies itself as arXiv:2609.28999v2. The supplied local file was compared byte-for-byte with the versioned public PDF: 959,353 bytes, SHA-256:

> f895d195c935bcc9e3d0b14d2499f59aa497b8fcdce7d69f13fbc74d10301add

The checked arXiv record lists v2, revised 25 September 2026; no later version or journal reference was listed when checked on 28 October 2026. No claim is made about an unexamined subsequent revision. Appendix A records the targeted source passages.

## 2. Related work and the valid reconstruction problem

The Koopman representation and its use in quantum simulation have an extensive history; Joseph [2] develops a KvN route for nonlinear classical dynamics. The transport implementation invoked by the source is the related Trotter-based algorithm of Zylberman et al. [3]. We do not re-audit that algorithm’s complete spatial, time-step, or gate complexity.

For a normalized transported density $\rho$, write $m=\mathbb E\!\left[X\right]$ and $\dot x_*=F(x_*)$. Under the boundary conditions needed for integration by parts, the exact first-moment identity is

$$
\dot m=\mathbb E\!\left[F(X)\right],\qquad
 \dot m-F(m)=\mathbb E\!\left[F(X)\right]-F(m).\qquad\text{(1)}
$$

The last term can be nonzero with perfect transport and perfect estimation of the actual mean. This cloud-to-trajectory discrepancy is separate from any readout error. The source’s Lipschitz estimate, its Eq. (15), is consistent with this identity. Its approximately Gaussian, second-order closure and constant covariance-norm approximation are explicitly disclosed assumptions, not newly discovered omissions. We do not treat phase-volume conservation as covariance conservation.

Amplitude estimation estimates a probability encoded by a specified circuit. The established coherent-query bounds of Brassard et al. [4] and Aaronson and Rall [5], and observable-estimation methods of Rall [6, 7] and Montanaro [8], distinguish query accuracy from the cost of preparing and inverting the required operations. Our counterexamples to a particular phase-inference argument do not contradict these algorithms or their accuracy guarantees. They identify which quantity the source circuit actually encodes and which assumptions are needed to infer a different quantity from it.

## 3. Initial separation and the geometric criterion

Let $\Phi_h$ denote a flow map for $h\geq0$, and let $B^d=\{\xi\in\mathbb R^d:\left\lVert \xi\right\rVert_2\leq1\}$. Write $\sigma$ for the effective width $\sigma_F$ in the source’s geometric definition. Work in a coordinate chart in which $B(x,\sigma)$ and the short trajectories considered below remain inside the domain, so coordinate wrapping is absent. The maximal relative drift in source Eq. (30), p. 5, is

$$
D_i^{\rm raw}(h;x,\sigma)
 :=\max_{\xi\in B^d}
 \left|\Phi_h(x+\sigma\xi)_i-\Phi_h(x)_i\right|.\qquad\text{(2)}
$$

It is a separation of final positions. Source Eq. (30) then identifies it with $h\max_{\xi\in B^d}|F_i(x+\sigma\xi)-F_i(x)|+O(h^2)$. That identification drops the separation already present at time zero. Indeed, a uniform short-time flow expansion gives

$$
\Phi_h(x+\sigma\xi)_i-\Phi_h(x)_i
 =\sigma\xi_i+h\bigl(F_i(x+\sigma\xi)-F_i(x)\bigr)+O(h^2).\qquad\text{(3)}
$$

For fixed $\sigma>0$, the first term cannot be included in an $O(h^2)$ remainder. In particular, $D_i^{\rm raw}(0;x,\sigma)=\sigma$.

#### Proposition 3.1: Obstruction for the stated directional maps

Suppose $\partial_iF_i=0$ on the relevant neighborhood. The directional flow used in a Trotter substep is exactly

$$
\Phi_h^{(i)}(x)=x+hF_i(x)e_i.\qquad\text{(4)}
$$

If $D_i^{\rm raw}$ is evaluated using this map, then $D_i^{\rm raw}\geq\sigma$. Consequently, if each component in source Eq. (31) is evaluated using its corresponding directional substep,

$$
\frac{\bigl(\sum_{i=1}^d(D_i^{\rm raw})^2\bigr)^{1/2}}
 {\sqrt d\,\sigma}\geq1.\qquad\text{(5)}
$$

#### Proof

Choose $\xi=e_i$ in (2). The coefficient does not change under this perturbation because it is independent of coordinate $i$. Hence $\Phi_h^{(i)}(x+\sigma e_i)_i-\Phi_h^{(i)}(x)_i=\sigma$. Taking the maximum proves the componentwise bound and summing proves (5). Centers at different intermediate substeps do not change the argument, provided their neighborhoods remain in the chart.

$\square$

Thus the approximately $0.1$ condition printed in source Eq. (31) cannot hold under the directional-map interpretation given in its geometric discussion. If the intended map were instead the complete flow, the time-zero contradiction in (3) would still remain: the normalized raw separation tends to $1$, rather than $0$, as $h\to0$.

This obstruction occurs for a genuinely nonlinear conservative field. Set

$$
F(q,p)=(\sin(2\pi p),0),\qquad
 H(q,p)=-\frac{\cos(2\pi p)}{2\pi}.\qquad\text{(6)}
$$

Then $\dot q=\partial_pH$, $\dot p=-\partial_qH$, and $\Phi_h(q,p)=(q+h\sin(2\pi p),p)$. Both own-coordinate derivatives vanish. A packet with means $(1/2,1/2)$ and a $p$ marginal symmetric about $1/2$ has $\mathbb E\!\left[\sin(2\pi P)\right]=0$. Its mean therefore remains at the fixed-point trajectory $(1/2,1/2)$, exactly, on any interval without coordinate wrapping. A smooth compactly supported symmetric packet can ensure this condition. The printed geometric condition nevertheless fails. This example concerns the geometric condition; its covariance need not remain constant, and no constant-covariance error theorem is invoked.

### 3.1 A corrected displacement quantity

An explicit repair is to compare the increments, subtracting the initial separation inside the absolute value:

$$
D_i^{\rm inc}(h;x,\sigma):=
 \max_{\xi\in B^d}\left|
 [\Phi_h(x+\sigma\xi)-(x+\sigma\xi)]_i
 -[\Phi_h(x)-x]_i\right|.\qquad\text{(7)}
$$

For the exact directional map (4),

$$
D_i^{\rm inc}
 =h\max_{\xi\in B^d}|F_i(x+\sigma\xi)-F_i(x)|.\qquad\text{(8)}
$$

This equality has no time-discretization remainder. It uses the own-coordinate condition and is specific to a directional substep.

#### Proposition 3.2: Local increment bound

Assume $F_i\in C^2$ on $B(x,\sigma)$ and use the directional map (4). Then

$$
\frac{D_i^{\rm inc}}{\sigma}
 \leq h\left\lVert \nabla F_i(x)\right\rVert_2+
 \frac{h\sigma}{2}
 \sup_{y\in B(x,\sigma)}\left\lVert D^2F_i(y)\right\rVert_{\rm op}.\qquad\text{(9)}
$$

If $F_i\in C^3$ and its third derivative has operator norm at most $M_3$ on the ball, the supremum-Hessian term may instead be replaced by

$$
\frac{h\sigma}{2}\left\lVert D^2F_i(x)\right\rVert_{\rm op}
 +\frac{h\sigma^2M_3}{6}.\qquad\text{(10)}
$$

#### Proof

Apply the one-dimensional Taylor formula along the segment $s\mapsto x+s\sigma\xi$. The linear term has absolute value at most $\sigma\left\lVert \nabla F_i(x)\right\rVert_2$ and the integral quadratic remainder is at most $\sigma^2\sup\left\lVert D^2F_i\right\rVert_{\rm op}/2$. Substitute in (8). Expanding one order further gives (10).

$\square$

For a complete smooth flow, (8) has an additional uniform $O(h^2)$ term on a fixed neighborhood. After division by $\sigma$ this is $O(h^2/\sigma)$; a joint small-width, small-step limit requires additional control. It must not be discarded as a grid-uniform statement.

The two terms in (9) separate linear stretching from local curvature. Increment distortion itself can be nonzero for an affine field, even though averaging then follows the exact trajectory. If only the nonlinear part is desired, one can further subtract $h\sigma\nabla F_i(x)\cdot\xi$ inside (7); its normalized magnitude is bounded by the Hessian term alone. These are standard local Taylor estimates. They repair the definition and expose its assumptions; they do not establish a new universal Ehrenfest–Reynolds threshold or a global trajectory-accuracy theorem.

## 4. Phase fringes, arithmetic means, and sampling

The source already contains a direct encoding of the mean of a bounded observable in Eqs. (32)–(34). A separate phase-reference procedure in Appendix D.3 requires a different analysis. We take its probability in source Eq. (D6) as the starting point, avoiding the missing affine probability conversion in source Eq. (37).

### 4.1 The exact statistic measured by a reference scan

Let $\Theta$ be the real observable encoded in the phase and let $a$ be the reference angle. On either a finite probability grid or a continuum probability space, define

$$
P(a):=\mathbb E\!\left[\cos^2(\Theta-a)\right],\qquad z:=\mathbb E\!\left[e^{2i\Theta}\right].\qquad\text{(11)}
$$

The finite-grid formula is exact, with the probabilities summing to one; no Riemann-sum approximation is required for the following statements.

#### Proposition 4.1: Exact phase-reference fringe

For every real $a$,

$$
P(a)=\frac12+\frac12\operatorname{Re}(e^{-2ia}z).\qquad\text{(12)}
$$

If $z\ne0$, its maximizing reference satisfies $a_*=\tfrac12\arg z\pmod\pi$, and its contrast is $|z|$. This circular mean generally differs from $\mathbb E\!\left[\Theta\right]$.

#### Proof

Use $\cos^2u=(1+\cos2u)/2$ and linearity of expectation. Writing $z=|z|e^{i\varphi}$ gives $P(a)=1/2+(|z|/2)\cos(\varphi-2a)$, proving the assertion.

$\square$

Source Eq. (D8) correctly displays variance as a leading reduction of the fringe amplitude. The paragraph after source Eq. (D10), p. 15, then introduces $\cos(2\theta_{\rm err})=1-2\operatorname{Var}(\Theta)$ and uses an additive shift in a squared cosine. Multiplying a cosine’s amplitude and shifting its argument are different operations: a fixed shift generally introduces an odd component about the original peak. Equation (12) identifies the relevant quantities without this substitution.

#### Corollary 4.2: Positive variance without phase bias

If $Y:=\Theta-\mu$ has a symmetric distribution and $C:=\mathbb E\!\left[\cos2Y\right]>0$, then

$$
P(a)=\frac12+\frac C2\cos[2(\mu-a)],\qquad a_*=\mu\pmod\pi.\qquad\text{(13)}
$$

The conclusion holds even when $\operatorname{Var}(\Theta)>0$.

#### Proof

Symmetry gives $\mathbb E\!\left[\sin2Y\right]=0$, hence $z=e^{2i\mu}C$. Apply Proposition 4.1.

$\square$

For the ideal Gaussian $\Theta\sim N(\mu,\sigma^2)$ on $\mathbb R$, $C=e^{-2\sigma^2}$. A symmetric truncated Gaussian on $[\mu-b,\mu+b]$ with $b<\pi/4$ also has $C>0$, since $\cos2Y>0$ throughout its support. The same result holds exactly for symmetric finite-grid weights. Thus the counterexample does not depend on an unbounded phase-space domain. A reference interval of length less than $\pi$ containing $\mu$ fixes the relevant branch of the maximum. Nonzero variance reduces contrast but does not impose a nonzero phase bias in this family. With increasing samples the maximum can be located arbitrarily accurately; reduced contrast affects the resources required.

The origin of a phase displacement can also be isolated locally. If $\Theta=\mu+sZ$, $\mathbb E\!\left[Z\right]=0$, and $\mathbb E\!\left[|Z|^5\right]<\infty$, Taylor expansion of $\mathbb E\!\left[e^{2isZ}\right]$ on the branch near $1$ yields

$$
a_* =\mu-\frac23s^3\mathbb E\!\left[Z^3\right]+O(s^5),\qquad s\to0.\qquad\text{(14)}
$$

Here $\mu$ is fixed, and $Z$ has a fixed distribution with the stated moments. The second moment changes the real part at order $s^2$; the leading imaginary part is $-4s^3\mathbb E\!\left[Z^3\right]/3$. This is a moment expansion of the exact fringe, not a general claim that all nonlinear inference biases begin at the same order.

### 4.2 A fixed-frequency fringe need not identify the arithmetic mean

The positive-variance counterexample disproves a mandatory phase-bias floor. Conversely, it does not make the circular mean a valid arithmetic mean estimator for arbitrary packets. A complete scan of $a$ in (12) determines only the one complex moment $z$.

#### Proposition 4.3: Same entire fringe, different arithmetic means

There exist strictly positive probability weights on four binary-grid points in $[0,1]$ with identical $P(a)$ for every $a$ and different arithmetic means.

#### Proof

Choose $\mu=1/2$, $a=1/8$, $b=1/16$, and the ordered support $x=(\mu-a,\mu-b,\mu+b,\mu+a)$. Set $c=\sin(2b)/\sin(2a)$, $v=(-c,1,-1,c)$, and

$$
p_j^{\pm}=\frac14\pm\eta v_j,\qquad 0<\eta<\frac14.\qquad\text{(15)}
$$

Since $0<c<1$, these weights are positive. Moreover,

$$
\sum_jv_j=0,\qquad
 \sum_jv_je^{2ix_j}=2ie^{2i\mu}
       \bigl(c\sin(2a)-\sin(2b)\bigr)=0.\qquad\text{(16)}
$$

The two distributions therefore have the same normalization and the same $z$. Their means differ by

$$
\sum_j(p_j^+-p_j^-)x_j=4\eta(ac-b)>0.\qquad\text{(17)}
$$

The strict inequality follows because $\sin t/t$ is decreasing for $0<t<\pi/2$, so $c>b/a$.

$\square$

At $\eta=0.1$ the mean separation is approximately $1.9659219701\times10^{-4}$. All four support points lie on a $16$-point binary grid. This is an identifiability statement for the fixed-frequency reference-fringe family. It is not an impossibility theorem for algorithms that encode a different function, obtain other Fourier moments, or measure additional information from the state.

### 4.3 Direct mean encoding and its resource assumptions

Let a state have grid probabilities $p_x$, and let $0\leq f(x)\leq1$. The Hadamard circuit with diagonal phase $\vartheta(x)=2\arccos\sqrt{f(x)}$ gives ancilla-zero amplitudes $\sqrt{p_x}(1+e^{i\vartheta(x)})/2$. Therefore its probability is exactly

$$
p_f=\sum_xp_x\cos^2\!\left(\frac{\vartheta(x)}2\right)
     =\sum_xp_xf(x)=\mathbb E\!\left[f(X)\right].\qquad\text{(18)}
$$

This is the source’s own Eqs. (32)–(34), read as a finite-grid identity. Standard amplitude estimation can estimate this encoded probability with additive accuracy using $O(\epsilon^{-1})$ coherent queries at fixed success probability [4, 5]; more general observable estimation is also established [6]. These are query statements requiring appropriate coherent state preparation, inverse operations, reflections, and accurate observable encoding. Their gate costs and state-preparation success costs remain to be counted. No new amplitude estimation algorithm or end-to-end quantum speedup is claimed here.

### 4.4 Two sampling experiments have different variances

The measurement-cost prefactor in source Sec. V, p. 6, is written in terms of the packet covariance. For an ancilla trial $Y\in\{0,1\}$ with success probability $p_f$, however, independent trials give

$$
\operatorname{Var}\!\left(\frac1M\sum_{m=1}^MY_m\right)
 =\frac{p_f(1-p_f)}{M}.\qquad\text{(19)}
$$

If instead one samples the coordinate $X$ directly in the computational basis, its sample mean has variance $\operatorname{Var}(X)/M$. These statements concern different recorded random variables. For $f(X)=X$ and any distribution on $[0,1]$ symmetric about $1/2$, $p_f=1/2$ and the ancilla variance per shot is $1/4$, irrespective of the coordinate variance. A narrow Gaussian packet can have arbitrarily small coordinate variance without making these ancilla outcomes less random. Source Appendix D.1 analyzes direct Gaussian samples, while Appendix D.2 separately gives the Bernoulli variance factor. The former cannot be transferred as the prefactor of the latter circuit.

The inverse-square accuracy exponent for ordinary independent sampling survives this correction. For example, Hoeffding’s inequality for the ancilla sample mean gives failure probability at most $2e^{-2M\epsilon^2}$. The correction concerns the measured variable and its variance prefactor, rather than a refutation of standard sampling or amplitude-estimation scaling. Finally, estimating the actual packet mean accurately does not remove the separate difference between that mean and the nonlinear trajectory launched at its initial center.

## 5. Calibration of the Lotka–Volterra example

The source’s Eq. (22) defines

$$
L=\sqrt d\max_i\sup_{x\in\Omega}\left\lVert \nabla F_i(x)\right\rVert_2,
 \qquad H=\sqrt d\max_i\sup_{x\in\Omega}\left\lVert D^2 F_i(x)\right\rVert_F.\qquad\text{(20)}
$$

Its effective width and parameter, source Eqs. (23), (25), are

$$
\sigma_F^2=\frac{\left\lVert \Sigma\right\rVert_F}{\sqrt d},\qquad
 R=\frac{\sqrt d\,\sigma_F H}{2L}.\qquad\text{(21)}
$$

For $\Sigma=\sigma^2 I$, the definition gives $\sigma_F=\sigma$. The logarithmic Lotka–Volterra coordinates in the source give

$$
F_q(q,p)=-\alpha+\beta e^{-p},\qquad
 F_p(q,p)=\delta-\gamma e^{-q}.\qquad\text{(22)}
$$

The Euclidean norm of each row gradient equals the Frobenius norm of its row Hessian at every point:

$$
\left\lVert \nabla F_q\right\rVert_2=\left\lVert D^2F_q\right\rVert_F=\beta e^{-p},\qquad
 \left\lVert \nabla F_p\right\rVert_2=\left\lVert D^2F_p\right\rVert_F=\gamma e^{-q}.\qquad\text{(23)}
$$

Consequently $H=L$ on any common domain used in Eq. (20), and for this two-dimensional example

$$
\frac R\sigma=\frac{1}{\sqrt2}=0.7071067812\ldots.\qquad\text{(24)}
$$

This differs from the source’s Eq. (45), which states $R/\sigma=\gamma/\beta=2.29$. The inconsistency is with the displayed definitions, independent of whether the common supremum is evaluated globally or the same rowwise maxima are evaluated locally. With the source parameters $\beta=e^{-1/3}$, $\gamma=e^{1/2}$, the ratio $\gamma/\beta$ is actually $2.300975891\ldots$; that small decimal discrepancy is secondary to using the wrong ratio. At $\sigma=0.01$, Eq. (24) gives $R=0.0070710678\ldots$, instead of $0.0229$.

Both values are small, so this calculation does not overturn the qualitative success of that example. It changes the numerical calibration offered as evidence for the proposed criterion. It also prevents interpreting the reported value as a direct evaluation of the stated $L,H,\sigma_F$ definitions.

The paper’s recommendation of roughly ten grid points across a packet width is explicitly an order-of-magnitude numerical choice. We do not turn that choice into a sharp theorem or claim a benchmark fails solely because a chosen width spans fewer cells. The mismatched width annotations and left/right panel descriptions in source Fig. 4 are documented in the audit ledger as reproducibility and editorial issues, separate from the algebraic calibration error.

## 6. Regularity required by the Gaussian remainder

Source Eq. (35), p. 6, assumes a Gaussian packet and an observable $f$ twice continuously differentiable near its mean, but assigns the expansion a remainder $O(\left\lVert \Sigma\right\rVert^2)$:

$$
\mathbb E\!\left[f(X)\right]=f(\mu)+\frac12\operatorname{tr}
              (\Sigma D^2f(\mu))+O(\left\lVert \Sigma\right\rVert^2).\qquad\text{(25)}
$$

The stated differentiability does not imply that order, even for an ideal Gaussian.

#### Proposition 6.1: A $C^2$ counterexample

Set $\mu=1/2$ and $f(x)=|x-\mu|^3$ on $[0,1]$. This observable is $C^2$, satisfies $0\leq f\leq1/8$, and has $f(\mu)=f'(\mu)=f''(\mu)=0$. For a Gaussian of width $\sigma$ centered at $\mu$, its expectation has leading order $\sigma^3$, rather than $O(\sigma^4)$.

#### Proof

For an untruncated standard normal $Z$,

$$
\mathbb E\!\left[|\sigma Z|^3\right]=2\sqrt{\frac2\pi}\,\sigma^3.\qquad\text{(26)}
$$

The observable may be extended to a bounded $C^2$ function on $\mathbb R$ by a smooth cutoff that is one near $\mu$; this changes the displayed expectation only by exponentially small terms as $\sigma\to0$. Alternatively, normalize the Gaussian on $[0,1]$ itself. Its mean remains $\mu$, its variance $\tau_\sigma^2$ satisfies $\tau_\sigma^2\sim\sigma^2$, and the expectation in (26) has only exponentially small changes. Consequently

$$
\frac{\mathbb E\!\left[f(X)\right]}{\tau_\sigma^4}
 \sim 2\sqrt{\frac2\pi}\,\frac1\sigma\longrightarrow\infty.\qquad\text{(27)}
$$

The purported second-order covariance remainder is therefore not a consequence of the stated $C^2$ hypothesis.

$\square$

The untruncated calculation is an exact Gaussian test; the compact version addresses the localized packets used on a bounded computational domain. Source Appendix D.1 itself extends a narrow Gaussian integral to the real axis. The exponentially small boundary correction cannot repair the algebraic order in (27).

A standard sufficient stronger hypothesis makes the intended order precise. Here the operator norm of a fourth derivative means the norm of its associated four-linear form.

#### Proposition 6.2: A sufficient fourth-derivative bound

Let $X=\mu+Y$ with $Y\sim N(0,\Sigma)$ in fixed dimension $d$. Suppose $f\in C^4(\mathbb R^d)$ and $\sup_y\left\lVert D^4f(y)\right\rVert_{\rm op}\leq M_4$. Then

$$
\begin{aligned}
\left|\mathbb E\!\left[f(X)\right]-f(\mu)-\frac12\operatorname{tr}
                         (\Sigma D^2f(\mu))\right|
 &\leq\frac{M_4}{24}
       \left[(\operatorname{tr}\Sigma)^2+
                         2\operatorname{tr}(\Sigma^2)\right]\qquad\text{(28)}\\&\leq\frac{M_4(d+2)}{24}\left\lVert \Sigma\right\rVert_F^2.
\end{aligned}
$$

#### Proof

Taylor expansion through cubic order has pointwise remainder bounded by $M_4\left\lVert Y\right\rVert_2^4/24$. Centered Gaussian odd moments vanish, and $\mathbb E\!\left[Y^\top D^2f(\mu)Y\right]=\operatorname{tr}(\Sigma D^2f(\mu))$. The Gaussian fourth-moment identity is $\mathbb E\!\left[\left\lVert Y\right\rVert_2^4\right]=(\operatorname{tr}\Sigma)^2+
2\operatorname{tr}(\Sigma^2)$. Finally, $(\operatorname{tr}\Sigma)^2\leq d\left\lVert \Sigma\right\rVert_F^2$.

$\square$

Local $C^4$ hypotheses can be used with an explicit tail estimate and control outside the local neighborhood; they cannot silently replace the global bound in this proposition. This is a standard Taylor and Gaussian-moment estimate, included to supply a repair rather than a novel general approximation theorem. For the particular coordinate observables $f=x_i$ and $f=x_ix_j$, the relevant moment identities are exact for every distribution with the required moments. The regularity counterexample therefore does not invalidate direct measurement of means and covariance entries.

## 7. Reproducible experiments

The companion implementation uses explicit analytic fields, finite probability vectors, and fixed matrices; it requires no external dataset, original-paper PDF, quantum processor, or proprietary software. The numerical results are classical corroboration of the displayed algebra, not independent human peer review or evidence of a quantum speedup. The execution environment, exact commands, source hashes, result hashes, and assertions are recorded in the repository. Appendix C provides an inspectable execution summary and the main reported values.

The geometric experiment evaluates the source definition and the repaired displacement definition on the same nonlinear shear. Readout experiments use actual finite-grid probability vectors: symmetric Gaussian samples and a positive four-node pair. The checks compare the complete reference-phase fringes rather than estimating a maximum from noisy measurements. Further checks compare the two sampling variances, reproduce the benchmark ratio, and demonstrate the regularity counterexample by Gaussian quadrature. The covariance appendix checks exact finite-matrix identities. A small rounding tolerance is used only for floating-point evaluation; the main counterexamples also have analytic proofs.

| Check | Numerical value | Analytic comparison |
|:---|---:|---:|
| Raw geometric ratio, $h=10^{-3}$ | 1.0000098691 | $\geq1$ |
| Increment ratio, same map | 0.0044399602 | $0.0044399602$ |
| Maximum symmetric-packet phase bias | $1.67\times10^{-16}$ | $0$ |
| Same-fringe arithmetic-mean gap | $0.0001965922$ | $4\eta(ac-b)$ |
| Lotka–Volterra $R/\sigma$ | 0.7071067812 | $1/\sqrt2$ |
| $C^2$ cubic-moment coefficient | 1.5957691216 | $2\sqrt{2/\pi}$ |
| Dense covariance norm, $t=0.1$ | 1.5068242214 | appendix bound 1.3403624549 |

**Table 1.** Selected deterministic checks. Phase error is floating-point rounding. The covariance row concerns the appendix’s smaller constant; the larger main-text constant repairs that example. Full inputs and results are recorded in the checked JSON and execution log.

![Figure 1](https://raw.githubusercontent.com/Teylersf/koopman-embedding-corrections/main/figures/geometry-criterion.png)

**Figure 1.** The source geometric quantity retains the initial separation, whereas the repaired displacement difference vanishes with the time step. Both are evaluated for the same nonlinear Hamiltonian shear. This comparison addresses the printed definition; it is not a validation of a universal corrected stability threshold.

![Figure 2](https://raw.githubusercontent.com/Teylersf/koopman-embedding-corrections/main/figures/phase-inference.png)

**Figure 2.** Finite width changes the contrast of a symmetric packet’s exact reference-phase fringe without shifting its maximizing reference. The finite-grid calculations include positive-variance packets. The distinct four-node nonidentifiability example is given in the text and numerical log.

## 8. Discussion and limitations

The geometric error is an algebraic inconsistency between a definition and its expansion. Subtracting the initial separation repairs that inconsistency, but does not by itself establish that any chosen smallness threshold guarantees long-time trajectory accuracy. A useful theorem must specify the map, local derivative bounds, packet support, quadrature, time horizon, and reconstruction error to be controlled.

The readout correction likewise separates tasks. A fixed-frequency fringe does not determine an arbitrary arithmetic mean. Symmetry can eliminate the phase bias, while nonsymmetric packets can introduce one. These facts neither remove the nonlinear discrepancy in Eq. (1) nor impose a universal covariance floor on estimating an encoded expectation. The appropriate accuracy and resource statements depend on the chosen circuit and statistical experiment.

The benchmark calibration correction does not show that the Lotka–Volterra simulation fails: both the printed and corrected initial parameters are small in that example. The covariance proof repairs are not a refutation of every main-text bound. Gaussian closure may be useful over restricted time windows; its practical accuracy requires checks beyond the counterexamples here. No exhaustive error inventory, end-to-end quantum advantage, new general moment-closure theory, or universal impossibility theorem is claimed.

## 9. Conclusion

The geometric criterion printed in arXiv:2609.28999v2 retains an initial separation that its expansion omits. The exact directional-map calculation makes the normalized quantity at least one. The proposed phase inference also conflates fringe contrast with phase displacement; its output is a circular mean, and fixed-frequency fringe data need not identify an arithmetic mean. Correcting these statements requires explicit definitions and inference assumptions. The accompanying examples and proofs supply reproducible repairs while preserving the valid distinction between transported-density means and individual nonlinear trajectories.

## Author and methods disclosure

Taylor Kalin is the human author and is responsible for this submission. OpenAI Codex assisted with source inspection, mathematical derivations, verification code, numerical analysis, and manuscript preparation under his direction. Separate AI-agent checks were used during preparation; they are not represented as independent human expert review. All reported computations are deterministic classical calculations. No quantum-hardware experiment is claimed. This disclosure describes methods separately from the author byline.

### Funding and competing interests

This study was self-funded by Taylor Kalin, including computing resources and AI tools. No external funding was received. No competing interests were reported for this study.

## Prior dissemination and parallel-submission disclosure

This is one correction study. Its public GitHub repository is <https://github.com/Teylersf/koopman-embedding-corrections>. AiraXiv is an intended preprint deposit. AgentPub and AAES versions are planned after the Publish.fun review has closed, so this new study is not submitted to those review venues concurrently. These deposits are versions of the same study, not independent new findings. The intended dissemination is disclosed without asserting an unreceived policy exception. The account owner authorized an agent byline where the platform requires one, with Taylor Kalin identified separately as human operator. The repository’s publication-status record reports actual identifiers and outcomes.

## References

[1] Thibault Fredon, Abhay K. Ram, Fabrice Debbasch, Julien Zylberman, and Nuno F. Loureiro. On the numerical limitations of dual Koopman–von Neumann embeddings for solving conservative nonlinear ordinary differential equations on quantum computers, 2026. Version 2, revised 25 September 2026; audited version. [Source](https://arxiv.org/abs/2609.28999v2) · [DOI](https://doi.org/10.48550/arXiv.2609.28999).

[2] Ilon Joseph. Koopman–von Neumann approach to quantum simulation of nonlinear classical dynamics. *Physical Review Research*, 2:043102, 2020. [Source](https://arxiv.org/abs/2003.09980v4) · [DOI](https://doi.org/10.1103/PhysRevResearch.2.043102).

[3] Julien Zylberman, Thibault Fredon, Nuno F. Loureiro, and Fabrice Debbasch. Trotter-based quantum algorithm for solving transport equations with exponentially fewer time-steps, 2025. Checked preprint: version 2, 25 August 2025. [Source](https://arxiv.org/abs/2508.15691v2).

[4] Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp. Quantum amplitude amplification and estimation. In *Quantum Computation and Information*, volume 305 of *Contemporary Mathematics*, pages 53–74. American Mathematical Society, 2002. [Source](https://arxiv.org/abs/quant-ph/0005055) · [DOI](https://doi.org/10.1090/conm/305/05215).

[5] Scott Aaronson and Patrick Rall. Quantum approximate counting, simplified. In *Symposium on Simplicity in Algorithms*, pages 24–32. Society for Industrial and Applied Mathematics, 2020. Checked preprint: version 6, 3 November 2021, including its corrected proof. [Source](https://arxiv.org/abs/1908.10846v6) · [DOI](https://doi.org/10.1137/1.9781611976014.5).

[6] Patrick Rall. Quantum algorithms for estimating physical quantities using block encodings. *Physical Review A*, 102:022408, 2020. [Source](https://arxiv.org/abs/2004.06832v3) · [DOI](https://doi.org/10.1103/PhysRevA.102.022408).

[7] Patrick Rall. Faster coherent quantum algorithms for phase, energy, and amplitude estimation. *Quantum*, 5:566, 2021. Checked preprint: version 4, 12 December 2022; the publisher identifies version 3 as the published version. [Source](https://arxiv.org/abs/2103.09717v4) · [DOI](https://doi.org/10.22331/q-2021-10-19-566).

[8] Ashley Montanaro. Quantum speedup of Monte Carlo methods. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 471(2181):20150301, 2015. Checked preprint: version 3, 11 July 2017. [Source](https://arxiv.org/abs/1504.06987v3) · [DOI](https://doi.org/10.1098/rspa.2015.0301).

## A. Targeted source passages and version scope

All locators in this appendix refer to the PDF of arXiv:2609.28999v2 [1], not the HTML converter’s appendix numbering. The 17-page supplied PDF is byte-identical to a fresh versioned arXiv download: 959,353 bytes, with SHA-256 `f895d195c935bcc9e3d0b14d2499f59aa497b8fcdce7d69f13fbc74d10301add`. The official record checked on 28 October 2026 lists v2, revised 25 September 2026, and no journal reference. The following transcriptions were checked against rendered PDF pages. No persistence claim is made for an unexamined revision or version of record.

### A.1 Geometric definition and criterion

On PDF p. 5, source Eq. (30) defines the “maximal relative drift” as

$$
\begin{aligned}
\Delta_{\sigma_F}x_i
&:=\max_{\boldsymbol\xi\in B^d}
\left|x_i(\mathbf x+\sigma_F\boldsymbol\xi,\Delta t)
             -x_i(\mathbf x,\Delta t)\right|\\
&=\Delta t\max_{\boldsymbol\xi\in B^d}
\left|F_i(\mathbf x+\sigma_F\boldsymbol\xi)-F_i(\mathbf x)\right|
+O(\Delta t^2).
\end{aligned}
$$

On p. 6, source Eq. (31) gives

$$
\frac{\sqrt{\sum_i(\Delta_{\sigma_F}x_i)^2}}{\sqrt d\,\sigma_F}
\lesssim 10^{-1}.
$$

Appendix C, p. 13, repeats the position-difference definition as (C1). Its following sentence defines $x_i(\mathbf x,t)$ as the value of the coordinate after a directional translation starting at $\mathbf x$. Thus the omission of the initial offset is not explained by defining $x_i$ to mean displacement. The main text, p. 3, source Eq. (9), requires $\partial_{x_i}F_i=0$ for each directional factor; this is stronger than divergence-freeness and is explicitly acknowledged there.

### A.2 Phase fringe and the claimed precision scale

Appendix D.3, p. 14, source Eqs. (D6)–(D7), gives the probability

$$
P_0(a)=\left\langle\cos^2(\theta-a)\right\rangle_\rho
=\frac12+\frac12\left\langle\cos\bigl(2(\theta-a)\bigr)
\right\rangle_\rho+O(2^{-n}).
$$

Here the expectation identity is exact on the discrete distribution; the displayed $O(2^{-n})$ concerns comparison with a continuum integral. The source’s next expansion, (D8), is

$$
\begin{aligned}
P_0(a)={}&\frac12+\frac12\cos\bigl(2(\langle\theta\rangle_\rho-a)\bigr)
\bigl(1-2\operatorname{Var}_\rho(\theta)\bigr)\\
&+O\!\left(\left\langle
|\theta-\langle\theta\rangle_\rho|^3\right\rangle_\rho\right).
\end{aligned}
$$

After (D10), p. 15, the prose states that the precision is “at best $\operatorname{Var}_\rho(\theta)$” and assigns the scale $O(\|\Sigma\|\,\|D^2\theta\|)$. It introduces $\cos(2\theta_{\mathrm{err}})=1-2\operatorname{Var}_\rho(\theta)$ and then writes a shifted form $P_0\sim\cos^2(\langle f\rangle_\rho-m\epsilon+\theta_{\mathrm{err}})$. The correction targets that contrast-to-phase inference. It does not deny the distinct nonlinear cloud-to-trajectory discrepancy discussed in source Section IV.

### A.3 Sampling and observable regularity

Source Section V, p. 6, defines $f:\Omega\to[0,1]$ and uses $\theta=2\arccos\sqrt f$, yielding $P_0=\langle f\rangle_\rho$. The paragraph following source Eq. (35) assigns the shot count $M=O(\Sigma/\epsilon^2)$ to estimating this probability. Appendix D.1 instead analyzes direct coordinate samples, while D.2 separately analyzes Bernoulli measurements. These measurement models have different variances.

Immediately before source Eq. (35), $f$ is assumed twice continuously differentiable near the mean and $\rho$ multivariate Gaussian. The displayed expansion is

$$
\int_\Omega f(\mathbf x)\rho(\mathbf x)\,d\mathbf x
=f(\langle\mathbf x\rangle)
+\frac12\operatorname{Tr}\!\left(\Sigma D^2f(\langle\mathbf x\rangle)\right)
+O(\|\Sigma\|^2).
$$

The regularity counterexample concerns this remainder under the stated $C^2$ assumption. It does not challenge the polynomial identities for coordinate and squared-coordinate observables.

### A.4 Ehrenfest–Reynolds calibration

On p. 5, source Eqs. (22)–(25) define

$$
\begin{aligned}
L&=\sqrt d\max_i\sup_{\mathbf x\in\Omega}\|\nabla F_i(\mathbf x)\|_2,
&H&=\sqrt d\max_i\sup_{\mathbf x\in\Omega}\|D^2F_i(\mathbf x)\|_F,\\
\sigma_F^2&=\frac{\|\Sigma\|_F}{\sqrt d},
&R&=\frac{\sqrt d\,\sigma_F H}{2L}.
\end{aligned}
$$

The source states $\sigma_F=\sigma$ for $\Sigma=\sigma^2I$. For its logarithmic Lotka–Volterra example, source Eq. (45), p. 7, writes

$$
\frac R\sigma=\frac\gamma\beta=2.29.
$$

The numerical-calibration correction compares that display with the definitions above, rather than imposing a different definition of $R$.

### A.5 Disclosed approximations and preserved conclusions

Source Section IV.B, p. 4, explicitly describes approximately Gaussian second-order closure and a constant covariance Frobenius norm. It acknowledges that covariance conservation is stronger than phase-space volume conservation. Section IV.C, p. 5, says the choice of about ten grid points used in its width criterion is an arbitrary order-of-magnitude estimate. These disclosures remain part of the scope of the source’s claims. The present note does not treat them as newly discovered omissions. The valid distinction $\langle F(X)\rangle\ne F(\langle X\rangle)$ for nonlinear dynamics is retained.

## B. Covariance and width-normalization repairs

These supporting corrections concern the source’s Appendix B.2 and its Eq. (41). They do not replace a complete covariance theorem for the nonlinear flow.

For a linear deviation equation $\dot Y=JY$, the second-moment matrix $C=\mathbb E\!\left[YY^\top\right]$ satisfies exactly

$$
\dot C=JC+CJ^\top.\qquad\text{(29)}
$$

The source prints $JC+CJ$ with $J_{ij}=\partial_jF_i$. A covariance derivative must be symmetric, and the printed expression need not be. For example,

$$
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C=\begin{pmatrix}4&0\\0&1\end{pmatrix}\qquad\text{(30)}
$$

gives

$$
JC+CJ^\top=\begin{pmatrix}0&-3\\-3&0\end{pmatrix},\qquad
 JC+CJ=\begin{pmatrix}0&5\\-5&0\end{pmatrix}.\qquad\text{(31)}
$$

This linear Hamiltonian example isolates the transpose issue with no nonlinear closure remainder. These displayed matrices are dimensionless algebra examples. Multiplying $C$ by $\epsilon^2$, for example with $\epsilon=0.01$, preserves the contradiction while making it a localized covariance in the unit box. Centered bounded data realize that covariance; short trajectories can be confined to the same chart. The correct norm estimate is

$$
\left\lVert \dot C\right\rVert_F\leq2\left\lVert J\right\rVert_2\left\lVert C\right\rVert_F.\qquad\text{(32)}
$$

If $r=\max_i\left\lVert \nabla F_i\right\rVert_2$, the general row estimate is $\left\lVert J\right\rVert_2\leq\left\lVert J\right\rVert_F\leq\sqrt d\,r$. The source’s main definition $L=\sqrt d\,r$ supplies this factor; its Appendix B.2 redefinition omits it. The same appendix also moves the inner index sum outside the square in the displayed expansion of $\left\lVert JC\right\rVert_F^2$, discarding cross terms. The implementation includes a dense four-dimensional Hamiltonian example that checks this distinction. Using the main-text $L$ repairs the elementary matrix estimate, so the example is not presented as a counterexample to every main-text covariance bound.

Finally, source Eq. (41) identifies $\sqrt{\left\lVert \Sigma^{1/2}\right\rVert_F}$ with $\sigma_F$. Under the explicit isotropic test $\Sigma=\sigma^2I$, these quantities are respectively $d^{1/4}\sqrt\sigma$ and $\sigma$. The width defined in source Eq. (23) is instead

$$
\sigma_F=\left(\frac{\left\lVert \Sigma\right\rVert_F}{\sqrt d}\right)^{1/2}.\qquad\text{(33)}
$$

Correcting this identity is necessary before using that displayed formula to balance a measurement error with the packet’s localization scale. It does not create a universal lower bound on the accuracy of measuring a mean.

## C. Pinned execution evidence

The numerical code and checked results are pinned to Git commit

> b8f3100e8360510e956edc4b77b1ba61bf8d6094

in the repository <https://github.com/Teylersf/koopman-embedding-corrections>. This is the code snapshot; the publication commit additionally contains the finished manuscript and PDF. To reproduce the numerical values:

~~~sh
git clone https://github.com/Teylersf/koopman-embedding-corrections.git
cd koopman-embedding-corrections
git checkout b8f3100e8360510e956edc4b77b1ba61bf8d6094
python -m pip install -r requirements.txt
python -X utf8 experiments/verify.py
python -X utf8 experiments/make_figures.py
~~~

The source and result hashes below identify the exact executed files. All six check groups completed with exit status zero. This is an author-environment execution record, not a third-party certification. The complete log and JSON are included in the repository and release archive; the numerical table and explicit constructions make the main claims inspectable within this paper.

~~~text
AUTHOR-ENVIRONMENT EXECUTION RECORD
Deterministic classical checks, not independent human peer review or third-party certification.
Command: python -X utf8 experiments/verify.py
Started UTC: 2026-10-28T21:25:55.827272+00:00
Python: 3.12.14 (main, Aug 25 2026, 14:01:42) [MSC v.1944 64 bit (AMD64)]
Platform: win32
NumPy: 2.3.5
Script SHA-256:
  d31f8924db3cfd234806f615e82357c0
  c8e89b191041363676e62502a0056add
PASS: geometric_criterion
PASS: phase_and_sampling
PASS: single_frequency_nonidentifiability
PASS: LV_calibration
PASS: C2_remainder
PASS: covariance_and_width
All assertions passed: true
Exit status: 0
Verification JSON SHA-256:
  17368c8586be78a587793e40914ed995
  f0c0f3cc0296b3b52e6fa5341e8286df
Elapsed seconds: 0.016653
~~~

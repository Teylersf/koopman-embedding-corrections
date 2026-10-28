"""Generate paper tables and execution evidence from the checked JSON/log."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'results/verification.json').read_text(encoding='utf-8'))
c = data['checks']
geometry = next(row for row in c['geometric_criterion']['rows'] if row['dt'] == .001)
max_bias = max(abs(row['phase_bias']) for row in c['phase_and_sampling']['gaussian_rows'])
bias_mantissa, bias_exponent = format(max_bias, '.2e').split('e')
bias_latex = '$' + bias_mantissa + r'\times10^{' + str(int(bias_exponent)) + '}$'
pair = c['single_frequency_nonidentifiability']
lv = c['LV_calibration']
dense = c['covariance_and_width']['dense_linear_Hamiltonian']
table = r'''\begin{table}[tbp]
\centering\small
\begin{tabular}{p{.46\linewidth}rr}
\toprule
Check & Numerical value & Analytic comparison\\
\midrule
Raw geometric ratio, $h=10^{-3}$ & %.10f & $\geq1$\\
Increment ratio, same map & %.10f & $0.0044399602$\\
Maximum symmetric-packet phase bias & %s & $0$\\
Same-fringe arithmetic-mean gap & $%.10f$ & $4\eta(ac-b)$\\
Lotka--Volterra $R/\sigma$ & %.10f & $1/\sqrt2$\\
$C^2$ cubic-moment coefficient & %.10f & $2\sqrt{2/\pi}$\\
Dense covariance norm, $t=0.1$ & %.10f & appendix bound %.10f\\
\bottomrule
\end{tabular}
\caption{Selected deterministic checks. Phase error is floating-point rounding.
The covariance row concerns the appendix's smaller constant; the larger
main-text constant repairs that example. Full inputs and results are recorded
in the checked JSON and execution log.}
\label{tab:checks}
\end{table}
''' % (geometry['raw_Eq31_ratio'], geometry['corrected_displacement_ratio'],
       bias_latex, pair['mean_difference'], lv['R_over_sigma_from_Eqs22_25'],
       c['C2_remainder']['untruncated_coefficient'], dense['actual_covariance_norm'], dense['appendix_bound'])
(ROOT / 'paper/results-table.tex').write_text(table, encoding='utf-8', newline='\n')

commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
if len(commit) != 40:
    raise ValueError('Exact code commit is required.')
log = (ROOT / 'results/execution.log').read_text(encoding='utf-8').split('Complete results follow:')[0].strip()
assert 'All assertions passed: true' in log
script_sha = hashlib.sha256((ROOT / 'experiments/verify.py').read_bytes()).hexdigest()
result_sha = hashlib.sha256((ROOT / 'results/verification.json').read_bytes()).hexdigest()
assert script_sha in log and result_sha in log
tex = r'''\section{Pinned execution evidence}
\label{sec:execution}
The numerical code and checked results are pinned to Git commit
\begin{quote}\small\ttfamily
%s%s
\end{quote}
in the repository
\url{https://github.com/Teylersf/koopman-embedding-corrections}.
This is the code snapshot; the publication commit additionally contains the
finished manuscript and PDF. To reproduce the numerical values:
\begin{Verbatim}[fontsize=\small]
git clone https://github.com/Teylersf/koopman-embedding-corrections.git
cd koopman-embedding-corrections
git checkout %s
python -m pip install -r requirements.txt
python -X utf8 experiments/verify.py
python -X utf8 experiments/make_figures.py
\end{Verbatim}
The source and result hashes below identify the exact executed files. All
six check groups completed with exit status zero. This is an author-environment
execution record, not a third-party certification. The complete log and JSON
are included in the repository and release archive; the numerical table and
explicit constructions make the main claims inspectable within this paper.
\begin{Verbatim}[fontsize=\scriptsize,breaklines=true]
%s
\end{Verbatim}
''' % (commit[:20], commit[20:], commit, log)
# fancyvrb does not define breaklines; wrapped hash lines below are sufficient.
tex = tex.replace(',breaklines=true', '')
tex = tex.replace('Script SHA-256: ' + script_sha,
                  'Script SHA-256:\n  ' + script_sha[:32] + '\n  ' + script_sha[32:])
tex = tex.replace('Verification JSON SHA-256: ' + result_sha,
                  'Verification JSON SHA-256:\n  ' + result_sha[:32] + '\n  ' + result_sha[32:])
(ROOT / 'paper/sections/execution.tex').write_text(tex, encoding='utf-8', newline='\n')
(ROOT / 'results/code-pin.json').write_text(json.dumps({'code_commit': commit,
    'script_sha256': script_sha, 'results_sha256': result_sha}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'paper_data_generated': True, 'code_commit': commit,
                  'script_sha256': script_sha, 'results_sha256': result_sha}))

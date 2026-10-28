"""Record hashes of the paper, source and reproducibility artifacts."""
from pathlib import Path
import hashlib
import json
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / name for name in (
    'paper/main.pdf', 'paper/main.tex', 'paper/references.bib',
    'experiments/verify.py', 'experiments/make_figures.py',
    'results/verification.json', 'results/execution.log',
    'submissions/manuscript.md', 'submissions/metadata.json')]
paths += sorted((ROOT / 'paper/sections').glob('*.tex'))
paths += sorted((ROOT / 'figures').glob('*'))
reader = PdfReader(ROOT / 'paper/main.pdf')
assert reader.metadata.author == 'Taylor Kalin'
assert len(reader.pages) == 15
assert all('??' not in page.extract_text() for page in reader.pages)
data = {'canonical_author': reader.metadata.author, 'pages': len(reader.pages),
        'code_pin': json.loads((ROOT / 'results/code-pin.json').read_text()),
        'artifacts': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                       'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
(ROOT / 'results/artifact-manifest.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'pages': len(reader.pages), 'author': reader.metadata.author,
                  'artifacts_recorded': len(paths), 'all_pdf_reference_checks_passed': True}))

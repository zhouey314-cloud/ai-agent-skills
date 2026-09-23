from pathlib import Path
names='requirement-clarifier faq-builder evidence-content content-qa eval-engineering-lite meeting-to-actions research-synthesizer workflow-planner failure-analyzer project-handoff'.split()
for name in names:
    text=(Path('skills')/name/'SKILL.md').read_text()
    for section in ['## Input schema','## Output schema','## Example','## Failure modes']:
        assert section in text,(name,section)
    assert 'synthetic_unverified' in text,name
print(f'SKILL_CONTRACT_PASS count={len(names)}')

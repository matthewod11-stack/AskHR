import os
from pathlib import Path

RAW = Path(os.getenv("DATA_RAW_DIR", "data/raw")).resolve()

SAMPLES = {
    "handbook/performance.md": """# Performance Improvement Plan (PIP)\n\n**Standard duration**: 30–60 days.\n**Steps**:\n1. Document issues (SBI)\n2. Set SMART goals\n3. Support/resources\n4. Milestones (checkpoints)\n5. Consequences\n""",
    "onboarding/306090.md": """# 30/60/90 Plan — Engineer\n\n## 30 days: Learn\n- Dev env, codebase, team rituals\n## 60 days: Contribute\n- Ship 1–2 scoped features\n## 90 days: Own\n- Lead a small project; on-call readiness\n""",
    "policy/pto.md": """# PTO Policy\n\nAccrual begins on hire date. Exempt FT accrue monthly; non-exempt accrue per pay period. Carryover subject to local law.\n""",
    "policy/discipline.md": """# Progressive Discipline\n\nVerbal warning → Written warning → Final warning → Termination (may skip steps for severe misconduct).\n""",
    "templates/offer_letter.md": """# Offer Letter Template\n\nIncludes title, start date, compensation, at-will statement, IP/Confidentiality, and contingencies.\n"""
}

def main():
    created = []
    for rel, content in SAMPLES.items():
        p = RAW / rel
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            created.append(str(p))
    if created:
        print("Seeded sample files:")
        for c in created:
            print(" -", c)
    else:
        print("Sample pack already present; nothing to seed.")

if __name__ == "__main__":
    main()

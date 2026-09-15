from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")

required = [
    "PMP / PMBOK Practice Dashboard",
    "https://pmp-practice.markellosecosystem.com/",
    "Back to markellosecosystem",
    "Integration Management",
    "Stakeholder Management",
    "EVM",
    "Process vs Procedure",
    "PMP Assistant",
]
for item in required:
    if item not in html:
        raise SystemExit(f"Missing required content: {item}")

section = html.split('<section id="processes"', 1)[1].split('</section>', 1)[0]
if section.count('class="process-card"') != 10:
    raise SystemExit("Expected exactly 10 Knowledge Area process cards")
process_count = len(re.findall(r'<li>[^<]+ <em>[^<]+</em></li>', section))
if process_count != 49:
    raise SystemExit(f"Expected 49 processes, found {process_count}")

for control in ("assistant-button", "language-gr", "language-en", "theme-toggle", "settings-button", "info-button"):
    if f'id="{control}"' not in html:
        raise SystemExit(f"Missing canonical shell control: {control}")

if "prefers-reduced-motion" not in html or "localStorage" not in html:
    raise SystemExit("Accessibility or local appearance preference contract missing")

print("dashboard validation passed: 10 Knowledge Areas, 49 processes")

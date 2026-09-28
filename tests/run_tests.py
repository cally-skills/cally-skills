from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "cally-life-decision": {"decision-principles.md", "output-format.md"},
    "cally-marriage-crossroads": {
        "cally-methodology-public.md",
        "marriage-variables.md",
        "risk-model.md",
        "reversibility.md",
        "output-format.md",
    },
}


def fail(message: str) -> None:
    raise AssertionError(message)


def frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md has no YAML frontmatter")
    block = match.group(1)
    name = re.search(r"(?m)^name:\s*(.+)$", block)
    description = re.search(r"(?m)^description:\s*(.+)$", block)
    if not name or not description:
        fail("SKILL.md requires name and description")
    return name.group(1).strip(), description.group(1).strip()


def test_skill_structure() -> None:
    for directory, references in EXPECTED.items():
        skill_dir = SKILLS / directory
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"Missing {skill_file}")
        text = skill_file.read_text(encoding="utf-8")
        name, description = frontmatter(text)
        if name != directory or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"Invalid public skill name: {name}")
        if not 1 <= len(description) <= 1024:
            fail(f"Invalid description length for {name}")
        for reference in references:
            if not (skill_dir / "references" / reference).is_file():
                fail(f"Missing runtime reference: {directory}/{reference}")


def test_no_private_methodology() -> None:
    private = SKILLS / "cally-marriage-crossroads" / "references" / "cally-methodology.md"
    if private.exists():
        fail("Private methodology entered the public package")
    for path in SKILLS.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            internal_markers = ("对应案例：", "TODO" + "-CALLY", "REVIEW" + "-CALLY")
            if any(marker in text for marker in internal_markers):
                fail(f"Internal methodology marker found in {path}")


def test_public_cases() -> None:
    path = ROOT / "tests" / "cases.json"
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not 5 <= len(cases) <= 15:
        fail("Public example set must remain limited")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)) or any(not value for value in ids):
        fail("Public case ids must be unique and non-empty")
    for case in cases:
        for key in ("prompt", "expect_route", "must_check", "must_not"):
            if key not in case:
                fail(f"Case {case['id']} misses {key}")


def test_public_boundaries() -> None:
    life = (SKILLS / "cally-life-decision" / "SKILL.md").read_text(encoding="utf-8")
    marriage = (SKILLS / "cally-marriage-crossroads" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in ("事实查询", "情绪表达", "不替用户决定", "不预测"):
        if phrase not in life + marriage:
            fail(f"Missing public boundary: {phrase}")
    for phrase in ("即时", "可信支持", "专业人士"):
        if phrase not in marriage:
            fail(f"Missing marriage safety boundary: {phrase}")


def test_readability_checks() -> None:
    data = json.loads((ROOT / "tests" / "readability-checks.json").read_text(encoding="utf-8"))
    expected = {
        "abstract_noun_density",
        "sentence_length",
        "translationese",
        "user_first_paragraph_clarity",
        "jargon_leakage",
    }
    if set(data.get("checks", [])) != expected:
        fail("Readability check names are incomplete")

    jargon = ("风险暴露", "选择集", "可逆性", "退出能力", "变量权重", "方向性判断", "决策窗口", "证据降权")
    translationese = ("基于上述分析", "综上所述", "进行一个", "从而实现", "就此而言")
    for sample in data.get("samples", []):
        first = sample.get("first_paragraph", "").strip()
        text = sample.get("user_text", "").strip()
        if not first or len(re.findall(r"[\u4e00-\u9fff]", first)) > 40:
            fail(f"Unclear or overlong first paragraph: {sample.get('id')}")
        combined = first + text
        if any(term in combined for term in jargon):
            fail(f"Jargon leakage in {sample.get('id')}")
        if any(term in combined for term in translationese):
            fail(f"Translationese in {sample.get('id')}")
        sentences = [part for part in re.split(r"[。！？；\n]+", combined) if part]
        if any(len(re.findall(r"[\u4e00-\u9fff]", sentence)) > 40 for sentence in sentences):
            fail(f"Sentence too long in {sample.get('id')}")
        abstract_hits = sum(combined.count(term) for term in jargon)
        chinese_count = max(1, len(re.findall(r"[\u4e00-\u9fff]", combined)))
        if abstract_hits / chinese_count > 0.02:
            fail(f"Abstract noun density too high in {sample.get('id')}")

    output_files = [
        SKILLS / "cally-life-decision" / "references" / "output-format.md",
        SKILLS / "cally-marriage-crossroads" / "references" / "output-format.md",
    ]
    for path in output_files:
        text = path.read_text(encoding="utf-8")
        if "单句尽量控制在 35–40 个中文字内" not in text:
            fail(f"Missing sentence-length guidance in {path}")
        if "每段只" not in text or "人话" not in text and "日常词" not in text:
            fail(f"Missing plain-language guidance in {path}")


def main() -> int:
    tests = [
        test_skill_structure,
        test_no_private_methodology,
        test_public_cases,
        test_public_boundaries,
        test_readability_checks,
    ]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:
            failures += 1
            print(f"FAIL {test.__name__}: {exc}")
    print(f"\n{len(tests) - failures}/{len(tests)} public test groups passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

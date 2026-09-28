# Cally Skills

**Cross-platform decision intelligence skills**

> Alpha. Interfaces, behaviors, and evaluation criteria may change between versions.

Cally Skills turns structured decision frameworks into portable Agent Skills for high-cost, hard-to-reverse life decisions.

The current Alpha includes a general life-decision router and **Marriage Crossroads（婚姻岔路口）**, the most developed and extensively tested module in the repository.

## Included skills

- `cally-life-decision` — **人生怎么选**  
  Helps reframe difficult choices, identify the variables that can actually change the decision, and route supported domains.

- `cally-marriage-crossroads` — **婚姻岔路口**  
  Helps analyze repair, observation, separation, negotiation, divorce, option protection, and exit planning without reducing complex marriage decisions to a simple “leave or stay.”

These skills are built to improve judgment, not automate life decisions. They do not replace legal, medical, financial, or crisis-response professionals.

## Status and scope

- Current version: **v0.3 Alpha**.
- Core skills use the portable `SKILL.md` directory structure with optional `references/`.
- Target adapters: OpenAI Codex, Meta Muse Code, and Qwen Code.
- Current behavioral validation primarily covers major marriage-decision scenarios.
- Current Alpha has been internally evaluated across 76 internal real-agent and adversarial decision-boundary scenarios.
- The project will continue to evolve through versioned methodology, compatibility, and regression updates.

Internal evaluation is not independent professional validation and does not establish an accuracy or safety rate.

This repository is not a legal, medical, financial, mental-health, emergency, or crisis-intervention service. High-risk or jurisdiction-specific situations require appropriate local services or qualified professionals.

## Repository structure

```text
skills/      Canonical Agent Skills
adapters/    Platform-specific discovery and installation notes
tests/       Public structural and behavioral regression tests
docs/        Release notes and compatibility documentation
```

`skills/` is the canonical source. Platform adapters must not create independently maintained copies of a Skill.

## Local validation

The repository regression suite uses the Python standard library:

```shell
python tests/run_tests.py
```

Each Skill should also be checked with a compatible Agent Skills validator before release. Internal real-Agent transcripts, adversarial prompts, and research evaluations are not included in this repository; published scenario counts describe the tested sample only and do not prove safety, accuracy, or reliability.

## Installation and compatibility

The Skill directories follow the common Agent Skills shape: a required `SKILL.md` with `name` and `description`, plus on-demand supporting files. See:

- `adapters/codex/README.md`
- `adapters/muse/README.md`
- `adapters/qwen/README.md`
- `docs/cross-platform-compatibility.md`

Windows Codex Desktop project-level junction discovery has a known compatibility issue documented in the release notes. Do not assume a junction or symlink strategy works on every client or operating system.

## Safety and limitations

- Do not treat labels, diagnoses, predictions, or user interpretations as established facts.
- Do not infer that a test pass means a response is safe in every real situation.
- If immediate danger is indicated, prioritize local emergency help, trusted support, and the user's ability to seek help over long-form decision analysis.
- Do not use the skills as a substitute for qualified legal, medical, financial, immigration, child-protection, or crisis support.

## License and contributions

Use of this Alpha is governed by `LICENSE.md`. It is not distributed under a standard open-source license.

Compatibility, adapter, documentation, installation, test-case, and bug-report contributions are welcome. Core Cally methodology and branded judgment logic remain maintainer-only; see `CONTRIBUTING.md`.

# Agent Skills / skills.sh Compatibility Check — v0.3 Alpha

Check date: 2026-09-28  
Scope: format, dependency, and validator compatibility for the v0.3 Alpha repository.

## Reference format checked

The check used the current Agent Skills specification and skills.sh documentation:

- https://agentskills.io/specification
- https://www.skills.sh/docs
- https://www.skills.sh/docs/cli

The common format requires a Skill directory with `SKILL.md`; frontmatter requires `name` and `description`. Names must be lowercase hyphenated identifiers of at most 64 characters and match their directory. Descriptions must state capability and activation context. `references/`, `scripts/`, and `assets/` are optional, and Skill file references should be relative to the Skill root.

## Local results

| Check | `cally-life-decision` | `cally-marriage-crossroads` |
|---|---|---|
| Stable lowercase hyphenated directory | Pass | Pass |
| Frontmatter name matches directory | Pass | Pass |
| Required `name` and `description` | Pass | Pass |
| Description states capability and use context | Pass | Pass |
| Relative references resolve | Pass | Pass |
| `SKILL.md` below 500 lines | Pass | Pass |
| No runtime script or package dependency | Pass | Pass |
| No personal path or platform-only command in Skill runtime | Pass | Pass |
| Bundled `quick_validate.py` | Pass | Pass |

## Discovery quality

- `cally-life-decision` has a broad but bounded discovery description: it targets high-cost or hard-to-reverse personal decisions and excludes emotion-only expression and factual queries. It routes unsupported domains without claiming that specialist modules exist.
- `cally-marriage-crossroads` has a specific marriage-decision description and explicitly excludes deciding divorce/continuation for the user or predicting a partner's psychology.
- Both directory names are stable and appropriate for public installation. The Chinese display names remain documentation text rather than non-portable frontmatter extensions.

## Dependencies and portability

- The runtime Skills are instruction-only Markdown and require no local executable, Python package, environment variable, API key, network service, or absolute path.
- Public regression tests use the Python standard library. Internal real-Agent tests have separate dependencies and are not included in this repository.
- The core frontmatter uses only common `name` and `description` fields. It does not depend on Codex-, Muse-, or Qwen-specific fields.
- Platform discovery locations remain adapter concerns. Generated `.agents/skills`, `.codex/skills`, and `.qwen/skills` copies are ignored and are not canonical sources.

## Public runtime boundary

The public marriage Skill uses `references/cally-methodology-public.md` and a reviewed Lite reference set. The complete `references/cally-methodology.md`, internal case mappings, research markers, and private evaluation artifacts are excluded. Every relative reference required by the public Skill is present in the staging package.

## Conclusion

The two public Skill directories are structurally compatible with the common Agent Skills format. The repository includes a public regression runner and should be validated again after any Skill or adapter change.

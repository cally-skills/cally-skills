# Cally Skills v0.3 Alpha — Release Notes

## V0.1 — Initial skill structure

- Established `cally-life-decision` as the general entry point for high-cost or hard-to-reverse decisions.
- Established `cally-marriage-crossroads` for major marriage decisions.
- Separated `SKILL.md` routing and workflow from on-demand references.
- Added initial Codex, Muse Code, and Qwen Code adapter notes.

## V0.2 — Real-agent validation baseline

- Added real-agent and adversarial validation for routing, fact discipline, premature direction, safety, and decision boundaries.
- Added regression protection and structured evaluation records.
- Kept complete prompts, outputs, traces, and detailed human evaluations outside the public repository.

## V0.3 — Public methodology runtime

- Added the public Lite methodology runtime for `cally-marriage-crossroads`.
- Added handling for risk escalation, difficult-to-reverse actions, repair willingness versus capacity, commitment evidence, observation design, time pressure, bilateral conflict, realistic ability to leave, sunk cost, judgment updates, and endorsement boundaries.
- Added Chinese readability guidance so internal analytical terms are translated into direct, everyday language for users.
- Added a limited public regression set and cross-platform adapter documentation.

The Alpha has been internally evaluated across 76 internal real-agent and adversarial decision-boundary scenarios. Internal evaluation is not independent professional validation and does not establish an accuracy or safety rate.

## Known limitations

- The current Alpha is validated most deeply for major marriage decisions.
- It does not replace legal, medical, financial, immigration, child-protection, mental-health, emergency, or crisis professionals.
- The public regression set is intentionally limited and is not a representative benchmark.
- The public runtime contains the rules required to operate the Skills, not the complete proprietary Cally methodology.
- Some Muse Code and Qwen Code installation/routing behaviors remain unverified in the target Windows/runtime environments.

## Modules not yet developed

No specialist Skills currently exist for career, relocation/immigration, parenting, real estate/large assets, or general relationships outside the marriage module. The general router can structure these decisions but must not present itself as a specialist module.

## Windows Codex Desktop discovery limitation

On the tested Windows Codex Desktop Alpha build, project-level junction and hardlink mappings under `.agents/skills` or `.codex/skills` caused workspace refresh failures. The repository uses root `AGENTS.md` as a project-level discovery fallback. This result is specific to the tested version and environment and should be rechecked on later clients.

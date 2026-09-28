# OpenAI Codex adapter

本仓库是一个 Agent Skills repository。核心源码位于根目录 `skills/`，每个 `skills/<skill-name>/SKILL.md` 及其 references 符合 OpenAI Agent Skills 使用的目录结构。

这不等于本仓库已经是完整的 OpenAI portable Plugin。若未来以 Plugin 形式分发，还需要 `plugin.json` 等 Plugin manifest 与相应的插件级元数据；这些文件不属于当前 Alpha 仓库。

## 第一版使用方式

- 作为 Agent Skills 仓库使用时，以根目录 `skills/` 为规范技能目录。
- OpenAI Agents API 沙箱可把包含这些 Skill 子目录的父目录注册为 `environment.capability_directories`。
- Codex 个人 Skill 的本机安装位置与具体发行方式可能随产品更新变化。

## 本地项目发现验证（2026-09-26）

在 Codex Desktop `0.155.0-alpha.9` 的 Windows 环境中，已实际测试：

- `.agents/skills` 整体 junction；
- `.agents/skills` 普通目录 + 逐 Skill junction；
- `.agents/skills` hardlink mapping；
- `.codex/skills` hardlink mapping。

四种方式都会让 Windows sandbox 在下一次 workspace refresh 时以 `helper_unknown_error: setup refresh had errors` 失败，因此本仓库不保留会破坏执行环境的 junction/hardlink，也不复制第二份 Skill。

当前可工作的项目级 fallback 是根目录 `AGENTS.md`：它把相关请求映射到唯一源码 `skills/cally-life-decision/SKILL.md` 和 `skills/cally-marriage-crossroads/SKILL.md`。这验证了本版本中的项目路由方案，不代表 `.agents/skills` 或 `.codex/skills` 已获得兼容性确认。后续 Codex 版本仍需重新验证 junction discovery。

## 验证

两个公开 Skill 应在干净 staging 中通过兼容的 Skill validator 和 `python tests/run_tests.py`。内部真实模型输出与完整人工评估不属于公开包。

# 跨平台兼容说明（核对日期：2026-09-26）

## 最小公共核心

OpenAI、Meta Muse Code、Qwen Code 的官方资料都支持“一个 Skill 目录 + `SKILL.md` + 可选 supporting files”的结构。第一版核心 frontmatter 只使用：

```yaml
---
name: kebab-case-name
description: what the skill does and when to use it
---
```

详细说明放 Markdown body，按需引用 `references/`。这是本仓库唯一维护的核心层。

## OpenAI Codex / Agent Skills

- OpenAI 声明 Skills 兼容开放 Agent Skills 标准。
- 可移植插件从根目录 `skills/<skill-name>/SKILL.md` 发现 Skill；可选资源包括 `references/`、`scripts/`、`assets/`。
- 模型在发现阶段先看到 `name` 和 `description`，匹配后才加载完整说明。
- Agents API 沙箱通过 `environment.capability_directories` 注册 Skill 父目录。
- 当前公开资料未给出 Codex Desktop 本地项目“自动发现目录”的单一推荐答案；不要仅依据其他平台对 `.codex/skills` 的扫描支持反推 Codex 自身行为。
- Windows Codex Desktop `0.155.0-alpha.9` 实测中，`.agents/skills` 的整体 junction、逐 Skill junction、hardlink mapping，以及 `.codex/skills` hardlink mapping，都会触发 workspace refresh 的 sandbox helper 错误。失败映射已清理。
- 当前项目使用根目录 `AGENTS.md` 作为可工作的 discovery fallback，指向唯一源码 `skills/`；这不是对 junction 兼容性的替代证明。后续版本仍需重新验证。

官方资料：

- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins

## Meta Muse Code

- 项目 Skill 官方位置：`<repo>/.agents/skills/<skill-id>/SKILL.md`。
- Muse 还扫描 repo-local `.codex/skills`、`.claude/skills`，以及部分外部个人 Skill 根目录。
- 官方命令包括 `muse skills validate`、`muse skills install` 和 `muse skills import --from codex`。
- 因而 Muse 可以导入 Codex Skill；“能导入”不等于所有专属字段、hook 或调用行为完全一致。本仓库只依赖公共字段。
- Known compatibility note: 自然语言自动路由、references 保留和中文 description 的选择表现，尚未在目标 Windows/runtime 环境中完成验证。

官方资料：

- https://dev.meta.ai/docs/muse-code/extending

## Qwen Code

- 项目 Skill 官方位置：`<repo>/.qwen/skills/<skill-name>/SKILL.md`；个人位置为 `~/.qwen/skills/`。
- 模型依据 `description` 自动调用；也可通过 `/<skill-name>` 显式调用。
- `name` 和 `description` 必填。`priority`、`paths`、`user-invocable`、`disable-model-invocation` 等是 Qwen 扩展字段，第一版不写入公共核心。
- Known compatibility note: junction/symlink 映射唯一源码的兼容性，尚未在目标 Windows/runtime 环境中完成验证；不支持时应使用不提交仓库的安装副本。

官方资料：

- https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/

## Adapter 策略

`adapters/platform-map.json` 记录唯一源码和平台目标位置。第一版 adapter 只提供说明，不自动写入隐藏平台目录，避免仓库内出现三份正文。后续若增加安装器，应满足：

1. 从 `skills/` 单向生成；
2. 生成目录加入 `.gitignore`；
3. 不回写核心正文；
4. 安装前验证目标路径；
5. 对尚未验证的平台行为明确标注兼容性限制。

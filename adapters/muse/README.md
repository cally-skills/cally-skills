# Meta Muse Code adapter

Muse Code 官方项目 Skill 位置是 `<repo>/.agents/skills/<skill-id>/SKILL.md`，并声明会扫描 repo-local `.codex/skills` 和 `.claude/skills`。官方 CLI 还提供 `muse skills import --from codex`、`muse skills install` 与 `muse skills validate`。

本仓库不提交复制的 `.agents/skills/`。第一版建议在测试环境中从核心 `skills/<skill-id>` 安装或导入，并用：

```text
muse skills validate ./skills/cally-life-decision
muse skills validate ./skills/cally-marriage-crossroads
```

Known compatibility note: 从本仓库根 `skills/` 直接导入时 references 相对路径是否完整保留，以及自然语言自动选择与 slash invocation 的实际表现，尚未在目标 Windows/runtime 环境中完成验证。

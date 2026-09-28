# Qwen Code adapter

Qwen Code 官方项目 Skill 位置是 `<repo>/.qwen/skills/<skill-name>/SKILL.md`。模型根据 frontmatter 的 `description` 自动决定是否调用，也可用 `/<skill-name>` 显式调用。

本仓库的唯一核心源码保留在 `skills/`。测试部署时，把整个 Skill 目录（包括 `references/`）映射或复制到 `.qwen/skills/`；生成目录不得提交，避免形成第二份维护源。

第一版只使用三个平台共有的 `name` 与 `description` 字段，不把 Qwen 专属的 `priority`、`paths`、`user-invocable` 或 `disable-model-invocation` 放进核心 frontmatter。

Known compatibility note: 目录 junction 或 symlink 是否能被安全发现，尚未在目标 Windows/Qwen Code runtime 环境中完成验证。若目标环境不支持，应使用由 adapter 生成且不提交仓库的安装副本。

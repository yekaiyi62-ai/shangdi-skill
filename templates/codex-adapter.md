# Codex 平台适配规则

生成Codex格式的Skill时，参考此文档进行转换。

## Claude Code vs Codex 格式差异

| 维度 | Claude Code | Codex |
|------|------------|-------|
| Skill位置 | `.claude/skills/[name]/SKILL.md` | `.codex/agents/[name].md` 或 `AGENTS.md` |
| 元数据 | YAML frontmatter (`---`) | 文档开头的标题和描述段落 |
| 工具调用 | `WebSearch`, `Read`, `Write`, `Agent` 等 | 自然语言描述工具需求 |
| 子Agent | `Agent` 工具，支持 `subagent_type` | 描述为独立任务委派 |
| 文件操作 | `Read`/`Write`/`Edit` 工具 | 标准文件操作描述 |

## 转换规则

### 1. 元数据转换

**Claude Code 格式**：
```yaml
---
name: my-skill
description: |
  这是一个Skill的描述。
  触发词：xxx
---
```

**Codex 格式**：
```markdown
# my-skill

这是一个Skill的描述。
触发词：xxx
```

### 2. 工具调用转换

Claude Code的工具名需要转为通用描述：

| Claude Code | Codex 等价描述 |
|------------|---------------|
| `WebSearch` | 「搜索互联网获取最新信息」 |
| `Read file` | 「读取文件 [路径]」 |
| `Write file` | 「创建/写入文件 [路径]」 |
| `Edit file` | 「编辑文件 [路径] 中的 [内容]」 |
| `Bash command` | 「执行命令：[命令]」 |
| `Agent subagent` | 「启动独立子任务处理 [描述]」 |
| `Glob pattern` | 「查找匹配 [模式] 的文件」 |
| `Grep pattern` | 「在代码中搜索 [模式]」 |

### 3. 目录结构转换

**Claude Code 团队结构**：
```
.claude/skills/[team-name]/
├── SKILL.md
├── members/
│   ├── role-1/SKILL.md
│   └── role-2/SKILL.md
└── shared/
```

**Codex 团队结构**：
```
.codex/
├── agents/
│   ├── [team-name].md          # 协调器
│   ├── [team-name]-role-1.md   # 成员1
│   └── [team-name]-role-2.md   # 成员2
└── shared/
    └── [team-name]/
```

### 4. 子Agent调用转换

**Claude Code**：
```markdown
用Agent工具启动子agent，subagent_type设为对应成员。
```

**Codex**：
```markdown
将此任务委派给独立的agent处理。
提供完整的任务描述和上下文，让agent独立完成后返回结果。
```

## 双平台同时输出

当用户选择「两者都要」时：

1. 先生成Claude Code版本（主版本）
2. 按上述规则自动转换为Codex版本
3. 两个版本放在各自平台的标准位置
4. 共享数据（shared/）只需要一份，两个平台共用

## Codex特有注意事项

- Codex对长文档的上下文窗口可能有限制，尽量精简
- Codex不支持frontmatter，所有元数据放在文档开头
- Codex的agent之间通信以文件为媒介，而非直接调用
- 测试时需要在Codex环境中验证agent是否能正确识别和执行指令

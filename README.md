# 上帝 · 造物术

> 输入任意需求，生成有真实能力的Skill或Skill团队。

**上帝**是一个元Skill（Meta-Skill）：不只是生成问答机器人，而是生成有完整输入→处理→输出工作流的专业工具。支持Claude Code和Codex双平台。

## 核心特性

- **造万物**：功能Skill、人物Skill、团队Skill，根据需求动态设计
- **有真实能力**：每个Skill有输入→处理→输出的完整工作流，能调用工具
- **团队模式**：一次生成多个协同工作的Skill，含总调度器和共享数据
- **双平台**：同时支持 Claude Code 和 Codex

## 三种Skill类型

### 1. 功能Skill
有明确的输入→处理→输出流程，能调用工具，有专业工作流。

```
例：雅思写作教练
输入：用户作文 → 按4维度评分 → 输出评分报告+修改建议+范文
```

### 2. 人物Skill
蒸馏人物思维框架，具备Agentic研究能力。

```
例：芒格思维顾问
输入：商业问题 → 用芒格的心智模型分析 → 输出芒格式判断
```

### 3. 团队Skill
一次生成多个协同工作的Skill，含总调度器。

```
例：雅思备考团队
协调器 → 口语教练 / 写作教练 / 听力训练师 / 词汇监督 / 学习规划师
共享用户档案和进度追踪
```

## 快速开始

### 安装

将本项目的 `SKILL.md` 安装为 Claude Code Skill：

```bash
# 克隆到本地
git clone https://github.com/[your-repo]/shangdi.git

# 复制到 Claude Code skills 目录
cp -r shangdi/ ~/.claude/skills/shangdi/
```

### 使用

在 Claude Code 中直接说：

```
「帮我造一个代码审查助手」        → 生成单个功能Skill
「生成一个雅思备考团队」          → 生成团队Skill
「蒸馏芒格的思维方式」            → 生成人物Skill
「我想提升写作能力，有什么建议？」  → 诊断后推荐方案
```

## 项目结构

```
shangdi/
├── SKILL.md                    # 核心：上帝元Skill
├── README.md
├── references/
│   ├── capability-matrix.md    # Skill能力矩阵参考
│   └── team-patterns.md        # 团队编排模式参考
├── templates/
│   ├── functional-skill.md     # 功能Skill模板
│   ├── team-coordinator.md     # 团队协调器模板
│   ├── person-skill.md         # 人物Skill模板
│   └── codex-adapter.md        # Codex平台适配规则
├── scripts/
│   └── quality_check.py        # Skill质量检查工具
└── examples/
    └── ielts-team/             # 示例：雅思备考团队
        ├── SKILL.md            # 团队协调器
        ├── members/
        │   ├── speaking-coach/
        │   ├── writing-coach/
        │   ├── listening-trainer/
        │   ├── vocabulary-supervisor/
        │   └── study-planner/
        └── shared/
            ├── user-profile.md
            └── progress.md
```

## 生成流程

```
Phase 0  需求解析 → 判断类型（单Skill/团队/人物/模糊）
Phase 1  能力设计 → 定义输入/输出/工具/工作流
Phase 2  领域调研 → 按需调研专业知识
Phase 3  Skill构建 → 按模板组装，支持双平台输出
Phase 4  质量验证 → 功能测试 + 团队协同测试
Phase 5  交付 → 安装到平台 + 使用演示
```

## 质量检查

```bash
# 检查单个Skill
python3 scripts/quality_check.py path/to/SKILL.md

# 检查团队Skill
python3 scripts/quality_check.py path/to/team-dir --team
```

## License

MIT

<div align="center">

# 上帝 · 造物术

> *「不只是造聊天人偶，每个Skill都是能做事的专业工具。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue)](https://github.com/openai/codex)

<br>

**输入任意需求，自动生成有真实输入→处理→输出能力的Skill或Skill团队。**

<br>

传统的Skill只会聊天问答。<br>
上帝生成的Skill有完整的工作流、能调用工具、有结构化输出。<br>
一次可以生成一整个协同工作的团队。

[看效果](#效果示例) · [安装](#安装) · [它能造什么](#三种skill类型) · [工作原理](#工作原理) · [项目结构](#项目结构)

</div>

---

## 效果示例

### 示例1：雅思写作教练（功能Skill）

不是泛泛地说「写得不错」，而是按官方4维度逐项评分、逐句标注问题、给出高分替换：

```
用户      ❯ [粘贴一篇Task 2作文]

写作教练   ❯ ═══════════════════════════════
             写作评分 · Task 2
             题目：是否应该限制私家车
             字数：267 词
            ═══════════════════════════════

            📊 分数：6.0 / 9.0

            维度细分：
              TA  任务完成    6.0  立场清晰但论证不够深入
              CC  连贯衔接    6.0  段落结构合理，但段内衔接偏弱
              LR  词汇资源    5.5  "good"出现6次，缺少同义替换
              GRA 语法准确    6.5  有复杂句，但从句连接偶有错误

            📝 逐段反馈：

            【开头段】
              ❌ "In modern society..." → 考官反感的套话，直接改写题目
              ⚡ "I think" → "I would argue that"（更学术）

            【主体段1】
              ❌ "cars are very good for people" → "private vehicles 
                 offer considerable convenience"
              ⚡ 缺少具体例子，加一个数据会更有说服力

            💡 提分关键：LR是最弱项。把重复的"good/bad/important"
               替换为话题词汇，可以直接提0.5分。
```

### 示例2：雅思团队协调器（团队Skill）

一个入口，自动分发到对应教练：

```
用户      ❯ 不知道今天练什么

协调器     ❯ 看了一下你的进度：
            - 写作已经3天没练了，上次Task 2拿了6.0
            - 口语昨天刚练过Part 2，拿了6.5
            - 词汇测试正确率从65%提到了78%，进步明显

            建议今天的安排：
            ┌─────────────────────────────┐
            │ 📋 今日任务 · 4月15日        │
            │ 备考第23天 · 距考试37天       │
            ├─────────────────────────────┤
            │ □ 写作练习：Task 2 一篇      │
            │   预计时间：60分钟            │
            │   找：写作教练                │
            │                              │
            │ □ 词汇复习：教育话题          │
            │   预计时间：30分钟            │
            │   找：词汇监督                │
            │                              │
            │ 总计：约1.5小时               │
            └─────────────────────────────┘

            要开始写作练习吗？我帮你转给写作教练出题。
```

### 示例3：口语教练模拟考

```
用户      ❯ 练一个Part 2

口语教练   ❯ 好，给你一道当季真题：

            ┌─────────────────────────────┐
            │ Describe a skill that you   │
            │ learned from an older person│
            │                             │
            │ You should say:             │
            │ - what the skill is         │
            │ - who you learned it from   │
            │ - how you learned it        │
            │ - and explain how you felt  │
            │   about learning this skill │
            └─────────────────────────────┘

            直接打字回答，像在考场上说的那样。
            不用太完美，我要看你的真实水平才能帮你提分。

用户      ❯ Well, I'd like to talk about cooking, which I 
            learned from my grandmother...
            [用户的完整回答]

口语教练   ❯ ═══════════════════════════
              口语评分 · Part 2
              话题：A skill from an older person
            ═══════════════════════════

            📊 分数：6.0 / 9.0

            维度细分：
              FC  流利连贯    6.0  基本流利，but/and用太多
              LR  词汇资源    5.5  "very good""very nice"重复
              GRA 语法准确    6.5  有复杂句，时态基本正确
              P   发音       6.0  (基于文本估计)

            ✅ 做得好：
              - 四个提示点都回答到了
              - 有个人感受的表达

            ⚠️ 需要改进：
              - "very good" → "incredibly rewarding"
              - "my grandmother is very old" → "my grandmother,
                who is in her eighties"（定语从句加分）
              - 连接词太单一，试试 "What struck me most was..."

            💡 高分替换：
              原文："I think cooking is very important"
              升级："I've come to realize that cooking is an
                     invaluable life skill"
              原因：come to realize 比 I think 更有深度
```

---

## 与传统Skill的区别

| | 传统Skill | 上帝生成的Skill |
|---|------|------|
| **能力** | 只会聊天问答 | 有输入→处理→输出的完整工作流 |
| **输出** | 自由文本 | 结构化格式（评分卡、报告、计划表） |
| **工具** | 不调用工具 | 可以搜索、读写文件、执行命令 |
| **数量** | 一次一个 | 一次可生成协同工作的团队 |
| **协作** | 独立运行 | 团队共享数据、互相联动 |
| **平台** | 单平台 | Claude Code + Codex |

---

## 三种Skill类型

### 1. 功能Skill

有明确的输入→处理→输出流程，能调用工具，有专业工作流。

```
例：雅思写作教练
输入：用户作文 → 按4维度评分 → 输出评分报告 + 逐句修改建议 + 高分范文
```

### 2. 人物Skill

蒸馏人物思维框架，具备Agentic研究能力。不只是模仿说话，是用他的认知框架分析问题。

```
例：芒格思维顾问
输入：商业问题 → WebSearch获取最新事实 → 用芒格的心智模型分析 → 输出芒格式判断
```

### 3. 团队Skill

一次生成多个协同工作的Skill，含总调度器和共享数据。

```
例：雅思备考团队
协调器 ← 用户入口，自动分发
├── 口语教练    模拟练习 + 4维度评分
├── 写作教练    作文批改 + 逐句反馈 + 范文
├── 听力训练师  题型攻略 + 精听方案
├── 词汇监督    话题词汇 + 测试 + 搭配训练
└── 学习规划师  制定计划 + 进度追踪 + 动态调整
    共享：用户档案 + 进度追踪
```

---

## 安装

### Claude Code

```bash
# 克隆到本地
git clone https://github.com/[your-repo]/shangdi.git

# 复制到 Claude Code skills 目录
mkdir -p ~/.claude/skills/shangdi
cp -r shangdi/* ~/.claude/skills/shangdi/
```

### 使用

在 Claude Code 中直接说：

```
> 帮我做一个代码审查助手          → 生成单个功能Skill
> 生成一个雅思备考团队            → 生成团队Skill（5个教练 + 协调器）
> 蒸馏芒格的思维方式              → 生成人物Skill
> 我想提升写作能力                → 诊断后推荐方案
```

### 使用已有的雅思团队示例

```bash
# 直接安装雅思团队示例
cp -r shangdi/examples/ielts-team ~/.claude/skills/ielts-team

# 然后在 Claude Code 中说
> 帮我练雅思口语
> 改一下这篇作文
> 今天练什么
```

---

## 工作原理

输入需求后，上帝做五件事：

**1. 需求解析** — 判断你要造什么：单个功能Skill？一个团队？还是人物Skill？模糊需求会通过1-2轮追问定位。

**2. 能力设计** — 不是拿到需求就开始搜索，而是先设计Skill的能力矩阵：输入类型、处理逻辑、输出格式、需要什么工具、工作流怎么走。这一步决定了Skill的上限。

**3. 领域调研** — 根据能力矩阵中的知识需求，启动并行Agent调研。功能Skill调研行业标准和最佳实践，人物Skill调研思维框架和表达风格。

**4. Skill构建** — 按模板组装可运行的SKILL.md。每个Skill都有：问题路由（输入分类）、执行工作流（Step by Step）、输出格式规范、质量检查清单。

**5. 质量验证** — 用样本输入测试完整工作流，检查输出是否符合格式规范、是否有专业价值。团队模式额外测试协同和数据交接。

```
Phase 0  需求解析 → 判断类型
Phase 1  能力设计 → 定义输入/输出/工具/工作流
Phase 2  领域调研 → 按需调研专业知识
Phase 3  Skill构建 → 按模板组装，支持双平台
Phase 4  质量验证 → 功能测试 + 协同测试
Phase 5  交付 → 安装 + 使用演示
```

---

## 团队模式详解

团队Skill是上帝最独特的能力。一次生成多个协同工作的Skill，共享数据，自动协调。

### 架构

```
          用户
           ↕
       ┌─────────┐
       │ 协调器    │ ← 分发任务、汇总进度、生成报告
       └────┬────┘
            │
    ┌───────┼───────┐
    ↓       ↓       ↓
  成员A   成员B   成员C
    │       │       │
    └───────┼───────┘
            ↓
       ┌─────────┐
       │ 共享数据  │ ← 用户档案、进度追踪
       └─────────┘
```

### 共享数据

团队成员通过共享文件协作：

| 文件 | 用途 |
|------|------|
| `shared/user-profile.md` | 用户基本信息、目标、当前水平 |
| `shared/progress.md` | 各模块练习记录、得分趋势 |

每个成员启动时读取共享数据了解用户情况，完成后更新练习记录。协调器负责汇总和生成综合报告。

---

## 项目结构

```
shangdi/
├── SKILL.md                         # 核心：上帝元Skill
├── README.md
├── references/
│   ├── capability-matrix.md         # Skill能力矩阵参考
│   └── team-patterns.md            # 团队编排模式参考
├── templates/
│   ├── functional-skill.md          # 功能Skill模板
│   ├── team-coordinator.md          # 团队协调器模板
│   ├── person-skill.md              # 人物Skill模板
│   └── codex-adapter.md            # Codex平台适配规则
├── scripts/
│   └── quality_check.py            # Skill质量检查工具
└── examples/
    └── ielts-team/                  # 示例：雅思备考团队
        ├── SKILL.md                 # 团队协调器（入口）
        ├── members/
        │   ├── speaking-coach/      # 口语教练
        │   ├── writing-coach/       # 写作教练
        │   ├── listening-trainer/   # 听力训练师
        │   ├── vocabulary-supervisor/ # 词汇监督
        │   └── study-planner/       # 学习规划师
        └── shared/                  # 团队共享数据
            ├── user-profile.md      # 用户档案模板
            └── progress.md          # 进度追踪模板
```

---

## 质量检查

每个生成的Skill都可以用内置工具自检：

```bash
# 检查单个Skill
python3 scripts/quality_check.py path/to/SKILL.md

# 检查团队Skill（自动检查协调器 + 所有成员）
python3 scripts/quality_check.py path/to/team-dir --team
```

检查项：

| 检查项 | 说明 |
|--------|------|
| frontmatter | 有name和description |
| 问题路由 | 覆盖主要输入类型 |
| 工作流 | 有完整的Step链 |
| 输入输出 | 有明确定义 |
| 能力边界 | 写了能做什么和不能做什么 |
| 检查点 | 关键步骤有用户确认 |
| 输出格式 | 有结构化格式规范 |
| 领域知识 | 使用了专业标准 |

---

## Roadmap

- [x] 核心元Skill（上帝造物术）
- [x] 三种Skill类型支持（功能/人物/团队）
- [x] 团队模式（协调器 + 成员 + 共享数据）
- [x] Codex平台适配
- [x] 雅思备考团队示例
- [x] 质量检查工具
- [ ] 更多示例：产品团队、代码审查、内容创作
- [ ] `npx skills add` 一键安装支持
- [ ] 团队Skill的Web UI进度面板
- [ ] 团队成员之间的自动触发联动

---

## Contributing

欢迎贡献！特别欢迎以下方向：

- **新示例**：用上帝生成一个团队Skill，提交到 `examples/`
- **新模板**：为特定领域设计Skill模板
- **平台适配**：添加更多平台支持（Cursor、Gemini CLI等）
- **质量检查**：完善 `quality_check.py` 的检查规则

请先开 Issue 讨论，再提 PR。

---

## License

MIT — 随便用，随便改，随便造。

<div align="center">

<br>

*传统Skill教AI怎么说。*<br>
*上帝教AI怎么做。*

<br>

MIT License

</div>

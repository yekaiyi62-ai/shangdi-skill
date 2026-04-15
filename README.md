<div align="center">

# 上帝 · 造物术

**输入任意需求，推演出专属于你的 AI 团队——有工作流、有知识库、有长期记忆。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-V2-brightgreen)](SKILL.md)

</div>

---

## 先看一个真实的场景

你准备考雅思。你告诉上帝：「帮我备考雅思，目标 7 分，还有 46 天。」

上帝不会给你一个通用的「学习助手」。它会先问你几个问题：

> 上帝：你上次考了多少？哪科差最多？每天能投入多少时间？

你告诉它：上次 6.0，写作和口语最弱，每天晚上有两小时。

然后你拿到的是这个：

```
推荐团队结构（请确认或调整）：

协调器         ← 你的入口，负责路由、进度报告、周/月复盘
├── 写作教练   ← Task 1 & Task 2 批改、按4维度评分、逐句修改
├── 口语教练   ← Part 1/2/3 模拟、FC/LR/GRA/P评分、发音建议
├── 听力训练师 ← 精听方法、题型策略、Section 3/4 攻克
├── 词汇监督   ← 话题词汇积累、搭配训练、测试出题
└── 学习规划师 ← 制定计划、进度追踪、模拟考安排

共享知识库：官方 Band 评分标准、中国考生常见错误、话题词汇分类
长期记忆：你的练习记录 + 弱点追踪 + 每周复盘 + 月度总结

要调整成员或开始生成吗？
```

这是上帝造物术做的事：**从你的需求推演出专属的团队**，不是套模板。

---

## 它和传统 Prompt/Skill 有什么不同

| | 传统 Prompt | 上帝生成的 Skill |
|---|---|---|
| **记忆** | 每次对话从零开始 | 记住你的练习记录、弱点状态、历史进度 |
| **知识** | 依赖 AI 的通用知识 | 专属知识库：官方评分标准 + 角色专属策略 |
| **输出** | 随机的自由文本 | 结构化输出，每次都有格式可预期 |
| **工作流** | 一步到位，全靠 AI 发挥 | Step-by-step，关键节点你来确认 |
| **弱点追踪** | 无 | 状态机：发现→训练中→待复查→已改善→已稳定 |
| **团队** | 一个 Prompt 一个角色 | 一次生成完整协作团队 |
| **结构** | 固定的通用模板 | 从你的需求推演出来的专属结构 |

---

## 三种造物类型

### 功能 Skill

有明确的输入→处理→输出，能调用工具，有结构化结果。

适合：代码审查、文案批改、数据分析、翻译润色……任何有专业标准的重复性任务。

### 人物 Skill

蒸馏某人的思维框架，用他的认知逻辑处理你的问题，而不只是模仿他说话。

适合：芒格的投资判断、费曼的解释方式、某个领域专家的决策框架……

### 团队 Skill

一次生成多个协同工作的角色——协调器负责路由、成员各司其职、共享知识库和记忆系统把团队连成一个整体。

适合：考试备考、健身计划、产品开发、内容创作……需要多角色配合的长期任务。

---

## 团队 Skill 实际上是什么样的

以雅思备考团队为例，看看一次完整的交互：

### 场景一：第一次练写作

```
用户      ❯ [粘贴一篇 Task 2 作文]

写作教练  ❯ ═══════════════════════════════
             写作评分 · Task 2
             题目：是否应该限制私家车
             字数：267 词
            ═══════════════════════════════

            📊 估计分数：6.0 / 9.0

            维度细分：
              TA  任务完成    6.0  立场清晰，但每个论点缺具体例子
              CC  连贯衔接    6.0  段落结构合理，主体段内部有跳跃
              LR  词汇资源    5.5  ⚠️ "good" 出现 6 次，"important" 出现 4 次
              GRA 语法准确    6.5  复杂句结构可以，从句连接偶有错误

            📝 逐段问题：

            【开头段】
              ❌ "In modern society..." → 考官最反感的套话，直接改写题目
              ⚡ "I think" → "I would argue that"（更学术，主观性更清晰）

            【主体段 1】
              ❌ "cars are very good for people"
                 → "private vehicles offer considerable convenience to commuters"
              ⚠️ 论点→解释→例子，你写了论点和解释，但没有例子
                 → 加一句："For instance, in cities like Beijing..."

            💡 最值得练的一点：LR 是你最弱的维度，也是最容易提分的。
               把"good/bad/important/nice"替换为话题词汇，
               可以直接从 5.5 → 6.5，差的只是背单词的时间。

            要看同题目的范文吗？
```

写作教练完成批改后，它会做几件事：

```
→ 追加到 shared/progress.md：
  | 2026-04-10 | 写作 | Task 2·社会 | TA:6/CC:6/LR:5.5/GRA:6.5 总:6.0 | LR停滞，词汇重复 |

→ 追加到 shared/session-log.md：
  | 2026-04-10 | 写作教练 | Task 2 批改 | 总分 6.0 | LR 三次停滞，建议专项训练 |

→ 更新 shared/weak-points.md：
  "写作 LR 词汇重复" 状态：发现 → 训练中（连续 3 次停滞，正式立案）
```

---

### 场景二：三周后协调器的周复盘

```
协调器    ❯ 第 3 周复盘 · 2026-04-07 ~ 2026-04-13

            本周练了 5 次：写作 1 / 口语 1 / 词汇 1 / 听力 2

            📊 分数变化：
            ┌──────────┬──────┬──────┬──────┐
            │ 科目      │ 上周  │ 本周  │ 变化  │
            ├──────────┼──────┼──────┼──────┤
            │ 写作      │ 6.1  │ 6.0  │ → 停滞│
            │ 口语      │ 5.8  │ 5.9  │ ↑    │
            │ 词汇正确率 │ 69%  │ 78%  │ ↑↑   │
            │ 听力      │ —    │ 训练中 │ 开始  │
            └──────────┴──────┴──────┴──────┘

            🔄 弱点状态变化：
            - 写作 CC 衔接弱：训练中 → 待复查（连续 2 次 CC ≥ 6.0 ✅）
            - 听力 Section 3/4：新发现 → 训练中
            - 口语 FC 停顿：训练中（未变化）

            ⚠️ 需要注意：
            - 写作 LR 连续三次 6.0，停滞超过 2 周，下周安排专项训练
            - 阅读至今零练习，距考试 53 天，不能再拖

            📅 下周建议（04-14 ~ 04-20）：
            1. 写作：Task 2 专项 LR 训练，目标 LR ≥ 6.5
            2. 口语：陌生话题 Part 2（验证 FC 改善是否真的有效）
            3. 听力：每天 30 分钟精听，专注角色标记
            4. 阅读：做一次摸底，评估当前水平

            已归档：本周 session-log → archive/week-03.md
```

---

### 场景三：弱点从发现到解决的完整过程

弱点不是记录下来就算了，它有自己的生命周期：

```
2026-03-30  口语教练发现：LR 词汇贫乏，大量使用 nice/good/very
            → 状态：发现 ← 在 weak-points.md 立案

2026-04-01  词汇监督制定计划：按话题系统积累，每周出一次口语词汇专练
            → 状态：训练中

2026-04-11  口语教练：LR:6.0，有进步（话题：描述一项技能）
            → 第 1 次通过

2026-04-15  口语教练：LR:6.0，稳定（话题：工作/学习）
            → 第 2 次连续通过 → 状态：待复查

2026-04-22  口语教练：LR:6.0，第 3 次通过（陌生话题验证）
            → 状态：已改善 → 协调器在周复盘中标注

2026-05-06  口语教练：LR:5.5，复发！（陌生话题压力下词汇又贫乏了）
            → 状态：复发 → 立即退回训练中
            → 词汇监督增加陌生话题专练

2026-05-20  连续 3 次 LR ≥ 6.0（包括陌生话题）
            → 状态：已稳定 ← 正式解决
```

这不是 Prompt，这是一个有记忆、有状态、会跟进的系统。

---

## 上帝如何工作（五个阶段）

### Phase 0：需求解析

判断造什么。通过 1-2 轮追问，定位你的需求——单个功能 Skill？多角色团队？人物蒸馏？

对于团队需求，上帝会识别领域类型，然后用该领域的设计问题和你对话，从你的具体答案推演出团队结构。这不是选模板，是一次设计对话。

### Phase 1：能力设计

先设计，再调研。定义每个角色的输入/输出/工具/工作流，设计团队的路由规则和数据交接方式。

### Phase 2：领域调研

按照能力设计中识别的知识需求，启动并行 Agent 调研——功能型调研行业标准，人物型调研六个维度（著作/对话/表达/决策/他者/时间线），结果全部写入 `references/research/`。

### Phase 3：Skill 构建

按三层知识架构组装：

```
团队共享知识库 (references/)
  knowledge-index.md  ← 路由表：什么问题读什么文件，不一次性加载全部
  domain-overview.md  ← 领域结构
  official-standards.md  ← 官方评分标准/行业规范
  common-errors.md  ← 常见错误

成员专属知识库 (members/[role]/references/)
  每个角色自己的评分细则、策略、题型分类

用户长期记忆 (shared/)
  user-profile.md     ← 档案（目标/水平/时间规划）
  progress.md         ← 详细练习记录
  weak-points.md      ← 弱点状态机
  session-log.md      ← 每次任务摘要，滚动 7 天
  weekly-reviews.md   ← 周复盘，滚动 4 周
  monthly-summary.md  ← 月度总结
  archive/            ← 历史归档
```

每个角色 SKILL.md 里都写明：启动时读哪些文件、完成后写哪些文件——包括 session-log 和弱点状态更新。

### Phase 4：质量验证

用真实输入测试工作流。团队模式额外测试：协调器路由是否正确、成员数据交接是否完整、共享记忆读写是否一致。

### Phase 5：交付

写入目标平台（Claude Code 或 Codex），展示使用方式，用一个样本走一遍完整流程。

---

## 安装

### npx 一键安装（推荐）

```bash
npx skills add yekaiyi62-ai/shangdi-skill --skill shangdi
```

### 手动安装

```bash
git clone https://github.com/yekaiyi62-ai/shangdi-skill.git
mkdir -p ~/.claude/skills/shangdi
cp -r shangdi-skill/* ~/.claude/skills/shangdi/
```

### 直接使用雅思团队示例

```bash
cp -r shangdi-skill/examples/ielts-team ~/.claude/skills/ielts-team
```

---

## 在 Claude Code 中触发

```
> 帮我做一个代码审查助手          → 生成功能 Skill
> 生成一个雅思备考团队            → 生成团队（5 教练 + 协调器 + 完整知识库）
> 帮我准备 CFA 1 级，6 个月后考试  → 推演出和雅思完全不同的考试团队
> 蒸馏芒格的思维方式              → 生成人物 Skill
> 帮我养好我的猫（英国短毛猫，2岁）→ 推演出宠物照护团队
> 我想提升写作能力                → 1-2 轮追问后给出方案
```

---

## 质量检查工具

每个生成的团队都可以自检：

```bash
python3 scripts/quality_check.py path/to/team-dir --team
```

V2 检查项（14 项）：

```
团队结构：
  ✓ knowledge-index.md 存在且有路由表
  ✓ shared/ 下 6 个文件 + archive/ 目录齐全
  ✓ 每个成员有自己的 references/ 专属知识库
  ✓ weak-points.md 包含 6 个状态定义

协调器：
  ✓ frontmatter / 问题路由 / 工作流步骤 / 检查点
  ✓ 输出格式规范 / 知识读取规则 / session-log 写入
  ✓ 弱点追踪 / 文件引用路径验证

每个成员：
  ✓ 以上所有 + 输入输出定义 / 能力边界 / 领域知识
```

---

## 项目结构

```
shangdi/
├── SKILL.md                              # 核心元 Skill（上帝的大脑）
├── references/
│   ├── domain-patterns.md               # 领域设计维度参考（思考工具，非固定模板）
│   ├── team-patterns.md                  # 团队编排模式
│   ├── team-knowledge-architecture.md    # 三层知识架构规范
│   └── capability-matrix.md              # Skill 能力矩阵参考
├── templates/
│   ├── functional-skill.md               # 功能 Skill 模板
│   ├── team-coordinator.md               # 协调器模板（含周/月复盘）
│   ├── person-skill.md                   # 人物 Skill 模板
│   └── codex-adapter.md                  # Codex 适配规则
├── scripts/
│   └── quality_check.py                  # V2 质量检查（14 项）
└── examples/
    └── ielts-team/                       # 完整示例：雅思备考团队（V2）
        ├── SKILL.md                      # 协调器（智能推荐 + 周/月复盘）
        ├── references/                   # 团队共享知识库
        │   ├── knowledge-index.md        #   路由表
        │   ├── exam-overview.md          #   雅思结构与分数换算
        │   ├── official-rubrics.md       #   官方 Band 5-8 描述
        │   └── common-errors.md          #   中国考生常见错误
        ├── members/                      # 5 个专业教练
        │   ├── writing-coach/
        │   ├── speaking-coach/
        │   ├── listening-trainer/
        │   ├── vocabulary-supervisor/
        │   └── study-planner/
        └── shared/                       # 用户长期记忆（真实填充的示例数据）
            ├── user-profile.md           #   真实学员档案（目标7分/备考22天）
            ├── progress.md               #   15条练习记录（3月25日至今）
            ├── weak-points.md            #   4个当前弱点（含状态演化）+ 1个已改善
            ├── session-log.md            #   最近7天会话（4月10-16日）
            ├── weekly-reviews.md         #   3周复盘（含趋势分析和下周建议）
            ├── monthly-summary.md        #   3月月度总结
            └── archive/
```

---

## Roadmap

### 已完成

- [x] 核心元 Skill（Phase 0-5 完整流程）
- [x] 三种类型（功能/人物/团队）
- [x] 三层知识架构（团队共享 / 成员专属 / 用户记忆）
- [x] V2 长期记忆（session-log → 周复盘 → 月总结 → 归档）
- [x] 弱点状态机（发现→训练中→待复查→已改善→已稳定→复发）
- [x] 领域设计维度参考（推演工具，非固定模板）
- [x] Codex 平台适配
- [x] 雅思团队完整示例（含真实数据填充的 V2 长期记忆）
- [x] V2 质量检查工具（14 项）

### 进行中

- [ ] `npx skills add` 一键安装
- [ ] 更多示例：CFA 备考团队、健身团队、内容创作流水线

### 后端演进路线

Skill 系统先做扎实，存储层逐步演进：

| 版本 | 存储 | 状态 |
|------|------|------|
| V1 | 纯 Markdown | ✅ 完成 |
| V2 | Markdown + 周/月复盘 | ✅ 当前 |
| V3 | Markdown + JSON 索引（快速检索）| 规划中 |
| V4 | SQLite 本地数据库 | 规划中 |
| V5 | 运行时后端 | 远期 |

---

## Contributing

特别欢迎：

- **新示例**：用上帝生成一个团队提交到 `examples/`（附真实数据填充的 shared/）
- **新领域设计问题**：在 `references/domain-patterns.md` 补充新领域的设计维度
- **质量检查扩展**：完善 `quality_check.py`

请先开 Issue 讨论再 PR。

---

## License

MIT — 随便用，随便改，随便造。

---

<div align="center">

传统 Prompt 教 AI 怎么说。<br>
上帝教 AI 怎么做——而且记得你上次做了什么。

</div>

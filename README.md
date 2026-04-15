<div align="center">

# 上帝 · 造物术

**输入任意需求，自动生成有真实工作流、专属知识库、长期记忆的 AI Skill 或 AI 团队。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-V2-brightgreen)](SKILL.md)

<br>

传统 Prompt 只教 AI「怎么说」。<br>
上帝教 AI「怎么做」——有工作流、有工具调用、有专属知识、有长期记忆。

<br>

[效果示例](#效果示例) · [三种 Skill 类型](#三种-skill-类型) · [安装](#安装) · [工作原理](#工作原理) · [V2 架构](#v2-架构) · [项目结构](#项目结构)

</div>

---

## 它解决什么问题

你可能遇到过这些场景：

- 写了一个很长的 System Prompt，但 AI 每次对话都忘记上次做了什么
- 想让 AI 帮你练雅思，但它给的反馈千篇一律，没有专业标准
- 需要一个「团队」——写作、规划、执行各司其职，却不知道怎么组织
- 做了一份 Skill，但 AI 拿到后不知道先做什么，全靠自由发挥

上帝造物术生成的 Skill 解决这四个问题：

| 问题 | 解决方式 |
|------|---------|
| 没有记忆 | 长期记忆系统：session-log → 周复盘 → 月总结 → 归档 |
| 没有专业知识 | 三层知识库：团队共享 + 角色专属 + 官方标准 |
| 没有团队协作 | 一次生成协调器 + N 个成员，自动路由和交接 |
| 没有工作流 | 每个 Step 有明确输入/输出，关键节点有用户确认 |

---

## 效果示例

### 示例 1：雅思写作教练（功能 Skill）

不是泛泛地说「写得不错」，而是按官方 4 维度评分、逐句标注、给出高分替换：

```
用户      ❯ [粘贴一篇 Task 2 作文]

写作教练  ❯ ═══════════════════════════════
             写作评分 · Task 2
             题目：是否应该限制私家车
             字数：267 词
            ═══════════════════════════════

            📊 分数：6.0 / 9.0

            维度细分：
              TA  任务完成    6.0  立场清晰但论证不够深入
              CC  连贯衔接    6.0  段落结构合理，段内衔接偏弱
              LR  词汇资源    5.5  "good" 出现 6 次，缺少同义替换
              GRA 语法准确    6.5  有复杂句，从句连接偶有错误

            📝 逐段反馈：

            【开头段】
              ❌ "In modern society..." → 考官反感的套话，直接改写题目
              ⚡ "I think" → "I would argue that"（更学术）

            【主体段 1】
              ❌ "cars are very good for people"
                 → "private vehicles offer considerable convenience"
              ⚡ 缺少具体例子，加一个数据会更有说服力

            💡 提分关键：LR 是最弱项。把重复的 "good/bad/important"
               替换为话题词汇，可以直接提 0.5 分。
```

### 示例 2：雅思团队协调器（团队 Skill）

一个入口，自动分发到对应教练，基于真实的练习数据推荐：

```
用户      ❯ 不知道今天练什么

协调器    ❯ 看了一下你的记录：
            - 写作已经 3 天没练了，上次 Task 2 拿了 6.0
            - 口语昨天刚练过 Part 2，拿了 6.5
            - 词汇测试正确率从 65% → 78%，进步明显

            建议今天的安排：
            ┌─────────────────────────────┐
            │ 📋 今日任务 · 4月16日        │
            │ 备考第 23 天 · 距考试 37 天  │
            ├─────────────────────────────┤
            │ □ 写作练习：Task 2 一篇      │
            │   预计 60 分钟 → 找写作教练  │
            │                             │
            │ □ 词汇复习：教育话题         │
            │   预计 30 分钟 → 找词汇监督  │
            └─────────────────────────────┘

            要开始写作练习吗？我帮你转给写作教练出题。
```

### 示例 3：口语教练模拟考

```
用户      ❯ 练一个 Part 2

口语教练  ❯ 好，给你一道当季真题：

            ┌───────────────────────────────────┐
            │ Describe a skill that you learned  │
            │ from an older person               │
            │                                   │
            │ You should say:                   │
            │ - what the skill is               │
            │ - who you learned it from         │
            │ - how you learned it              │
            │ - and explain how you felt        │
            └───────────────────────────────────┘

            直接打字回答，我要看你真实水平才能帮你提分。

用户      ❯ Well, I'd like to talk about cooking, which I
            learned from my grandmother...

口语教练  ❯ ═══════════════════════════
             口语评分 · Part 2
             话题：A skill from an older person
            ═══════════════════════════

            📊 分数：6.0 / 9.0

            维度细分：
              FC  流利连贯    6.0  基本流利，but/and 用太多
              LR  词汇资源    5.5  "very good""very nice" 重复
              GRA 语法准确    6.5  有复杂句，时态基本正确
              P   发音        6.0  (基于文本估计)

            ⚡ 高分替换：
              "I think cooking is very important"
              → "I've come to realize that cooking is an
                 invaluable life skill"
              原因：come to realize 比 I think 更有深度
```

---

## 三种 Skill 类型

### 1. 功能 Skill

有明确的输入→处理→输出流程，能调用工具，有结构化输出。

```
例：雅思写作教练
输入：用户作文
处理：按官方 4 维度评分 → 逐句标注 → 高分替换
输出：评分报告 + 修改建议 + 可选范文
```

**适合场景**：代码审查、文案评分、数据分析、翻译润色、格式转换……

### 2. 人物 Skill

蒸馏人物思维框架，具备 Agentic 研究能力。不只是模仿说话，是用他的认知框架分析问题。

```
例：芒格思维顾问
输入：商业问题
处理：WebSearch 获取最新事实 → 用芒格的心智模型分析
      逆向思考 + 多元思维框架 + 第一性原理
输出：芒格式判断（附上他会如何提问和反驳）
```

**适合场景**：决策顾问、思维框架、创业分析、投资判断……

### 3. 团队 Skill

一次生成多个协同工作的 Skill，含总调度器、共享知识库、长期记忆。

```
例：雅思备考团队
                用户
                 ↕
            ┌─────────┐
            │  协调器  │ ← 分发任务 + 智能推荐 + 进度报告 + 周/月复盘
            └────┬────┘
         ┌───────┼───────┬───────┐
         ↓       ↓       ↓       ↓
      口语教练 写作教练 听力训练师 词汇监督
         │       │       │       │
         └───────┴───────┴───────┘
                    ↓
              ┌──────────┐
              │ 共享知识库 │ ← 评分标准 + 专属知识 + 用户档案 + 长期记忆
              └──────────┘
```

**适合场景**：备考团队、健身教练组、产品团队、内容创作流水线……

---

## 与传统 Skill/Prompt 的区别

|  | 传统 Prompt | 上帝生成的 Skill |
|---|---|---|
| **记忆** | 每次对话从零开始 | 长期记忆：session-log → 周复盘 → 月总结 |
| **知识** | 依赖 AI 通用知识 | 专属知识库（官方标准 + 角色专属 + 通用规则）|
| **输出** | 自由文本，不可预期 | 结构化格式（评分卡、报告、计划表）|
| **工作流** | 一步到位，靠 AI 发挥 | Step-by-step，关键节点用户确认 |
| **团队** | 一个 Prompt 一个角色 | 一次生成完整协作团队 |
| **弱点追踪** | 无 | 状态机：发现→训练中→待复查→已改善→已稳定 |

---

## 安装

### 方式 1：npx 一键安装（推荐）

```bash
npx skills add yekaiyi62-ai/shangdi-skill --skill shangdi
```

### 方式 2：手动安装

```bash
git clone https://github.com/yekaiyi62-ai/shangdi-skill.git
mkdir -p ~/.claude/skills/shangdi
cp -r shangdi-skill/* ~/.claude/skills/shangdi/
```

### 使用

在 Claude Code 中直接说：

```
> 帮我做一个代码审查助手
> 生成一个雅思备考团队
> 蒸馏芒格的思维方式
> 我想提升写作能力
> 做一个健身打卡团队
```

### 直接使用雅思团队示例

```bash
cp -r shangdi-skill/examples/ielts-team ~/.claude/skills/ielts-team
```

然后在 Claude Code 中：
```
> 帮我练雅思口语
> 改一下这篇作文
> 今天练什么
> 给我出一周计划
```

---

## 工作原理

上帝做五件事：

### Phase 0：需求解析

判断你要造什么——单个功能 Skill、多角色团队、还是人物 Skill。模糊需求会通过 1-2 轮追问定位，不会变成问卷调查。

同时读取 `references/domain-patterns.md`，识别领域类型（8 种：考试学习/健身健康/宠物照护/选购决策/产品执行/内容创作/研究分析/技能习得），不同领域生成不同的角色模式和记忆文件结构。

### Phase 1：能力设计

不是拿到需求就搜索，而是先定义 Skill 的能力矩阵：

```yaml
inputs:   # 接收什么
outputs:  # 产出什么（含格式规范）
tools:    # 需要 WebSearch / Read / Write / Bash / Agent
workflow: # Step-by-step 处理流程（含检查点）
knowledge: # 需要调研哪些领域知识
```

### Phase 2：领域调研

根据能力矩阵的知识需求，启动并行 Agent 调研：

- **功能型**：行业标准、评分体系、最佳实践、常见错误
- **人物型**：著作/对话/表达 DNA/决策案例/外部视角/时间线（6 个维度）
- **团队型**：每个角色分别调研 + 协作模式

所有调研结果写入 `references/research/`，不存文件 = 没做。

### Phase 3：Skill 构建

按三层知识架构组装：

```
团队共享知识库 (references/)
  → knowledge-index.md  知识路由表：什么问题读什么文件
  → domain-overview.md  领域总览
  → official-standards.md  官方评分标准/行业规范
  → common-errors.md  常见错误

成员专属知识库 (members/[role]/references/)
  → 角色特有的评分细则、题型分类、训练方法

用户长期记忆 (shared/)
  → user-profile.md    用户档案（目标/水平/时间规划）
  → progress.md        练习记录和得分趋势
  → weak-points.md     弱点状态机
  → session-log.md     每次任务摘要（保留 7 天）
  → weekly-reviews.md  周复盘（保留 4 周）
  → monthly-summary.md 月度总结
  → archive/           历史归档
```

### Phase 4：质量验证

用样本输入测试完整工作流。团队模式额外测试协调器路由、成员数据交接、共享数据读写。

### Phase 5：交付

写入对应平台标准位置，展示使用方式，用一个样本演示工作流程。支持 Claude Code 和 Codex 双平台。

---

## V2 架构

### 长期记忆系统

V2 最大的升级：Skill 不再「失忆」。

```
每次任务完成
    ↓
session-log.md（追加一条摘要）
    ↓ 每 7 天
weekly-reviews.md（协调器汇总本周数据）
session-log → archive/week-XX.md（归档）
    ↓ 每 4 周
monthly-summary.md（月度趋势 + 策略调整）
weekly-reviews → archive/month-XX.md（归档）
```

启动时读取规则：
1. `shared/user-profile.md` — 必读
2. `shared/weak-points.md` — 必读（如有）
3. `shared/progress.md` 最近 10 条 — 必读
4. `shared/weekly-reviews.md` 最近 2 周 — 推荐
5. `shared/archive/` — **不默认读取**，用户要求时才读

### 弱点状态机

每个弱点都有生命周期，不是发现了就忘了：

```
发现 → 训练中 → 待复查 → 已改善 → 已稳定
                              ↘
                            复发 → 训练中（重新进入循环）
```

每条弱点记录必须包含：弱点名称、当前状态、首次发现日期、来源证据（哪次练习、什么表现）、下一步动作。

### 领域动态生成

8 种领域类型，生成不同的角色模式和 `shared/` 文件结构：

| 领域 | 默认角色 | 特有记忆文件 |
|------|---------|------------|
| 考试学习 | 各科教练 + 规划师 | progress.md + weak-points.md |
| 健身健康 | 训练师 + 营养师 + 恢复师 | body-metrics.md + workout-log.md |
| 宠物照护 | 喂养 + 健康 + 行为 | pet-profile.md + health-log.md |
| 选购决策 | 需求分析 + 比较研究 + 防坑 | decision-log.md |
| 产品执行 | PM + 设计 + 研发 + 数据 | sprint-log.md + metrics.md |
| 内容创作 | 选题 + 写作 + 审核 + 排版 | content-calendar.md |
| 研究分析 | 文献综述 + 数据分析 + 写作 | research-log.md |
| 技能习得 | 理论 + 实操 + 反馈 | practice-log.md |

---

## 项目结构

```
shangdi/
├── SKILL.md                              # 核心：上帝元 Skill（入口）
├── README.md
├── references/
│   ├── capability-matrix.md              # Skill 能力矩阵参考
│   ├── team-patterns.md                  # 团队编排模式（星型/流水线/并行）
│   ├── team-knowledge-architecture.md    # 三层知识架构规范（详细）
│   └── domain-patterns.md               # 8 种领域动态生成规则
├── templates/
│   ├── functional-skill.md               # 功能 Skill 模板（含 V2 长期记忆规则）
│   ├── team-coordinator.md               # 团队协调器模板（含周/月复盘）
│   ├── person-skill.md                   # 人物 Skill 模板
│   └── codex-adapter.md                  # Codex 平台适配规则
├── scripts/
│   └── quality_check.py                  # Skill 质量检查工具（V2）
└── examples/
    └── ielts-team/                       # 示例：雅思备考团队（完整 V2）
        ├── SKILL.md                      # 协调器（含周/月复盘工作流）
        ├── references/                   # 团队共享知识库
        │   ├── knowledge-index.md        #   知识路由表
        │   ├── exam-overview.md          #   雅思考试结构和评分换算
        │   ├── official-rubrics.md       #   官方 Band 描述（5-8 分）
        │   └── common-errors.md          #   中国考生常见错误
        ├── members/
        │   ├── speaking-coach/           # 口语教练
        │   │   ├── SKILL.md
        │   │   └── references/speaking-rubric.md
        │   ├── writing-coach/            # 写作教练
        │   │   ├── SKILL.md
        │   │   └── references/writing-rubric.md
        │   ├── listening-trainer/        # 听力训练师
        │   │   ├── SKILL.md
        │   │   └── references/listening-strategies.md
        │   ├── vocabulary-supervisor/    # 词汇监督
        │   │   ├── SKILL.md
        │   │   └── references/topic-vocabulary.md
        │   └── study-planner/           # 学习规划师
        │       ├── SKILL.md
        │       └── references/planning-strategies.md
        └── shared/                       # 用户长期记忆（V2）
            ├── user-profile.md           #   用户档案模板
            ├── progress.md               #   练习记录
            ├── weak-points.md            #   弱点状态机
            ├── session-log.md            #   会话摘要（7 天窗口）
            ├── weekly-reviews.md         #   周复盘（4 周窗口）
            ├── monthly-summary.md        #   月度总结
            └── archive/                  #   历史归档
```

---

## 质量检查

每个生成的 Skill 都可以用内置工具自检：

```bash
# 检查单个 Skill
python3 scripts/quality_check.py path/to/SKILL.md

# 检查团队 Skill（自动检查协调器 + 所有成员）
python3 scripts/quality_check.py path/to/team-dir --team
```

V2 检查项（团队模式）：

```
🏗️ 团队结构检查：
  知识索引    → references/knowledge-index.md 存在且有路由表
  长期记忆    → shared/ 下 6 个文件 + archive/ 目录齐全
  成员知识库  → 每个成员有自己的 references/ 目录
  弱点状态机  → weak-points.md 包含完整的 6 个状态

📋 协调器检查：
  问题路由 / 工作流 / 检查点 / 输出格式 / 知识读取规则 /
  会话日志写入 / 弱点追踪 / 文件路径验证

👤 成员检查（每个成员）：
  frontmatter / 问题路由 / 工作流 / 输入输出 / 能力边界 /
  检查点 / 输出格式 / 领域知识 / 知识读取规则 /
  会话日志写入 / 弱点追踪 / 文件路径验证
```

---

## Roadmap

### 已完成 (V1 + V2)

- [x] 核心元 Skill（上帝造物术，5 个 Phase）
- [x] 三种 Skill 类型（功能/人物/团队）
- [x] 三层知识架构（团队共享 + 成员专属 + 用户记忆）
- [x] V2 长期记忆系统（session-log → 周复盘 → 月总结 → 归档）
- [x] 弱点状态机（6 个状态 + 证据要求）
- [x] 8 种领域动态生成规则
- [x] Codex 平台适配
- [x] 雅思备考团队完整示例（5 教练 + 协调器 + 完整知识库）
- [x] V2 质量检查工具（14 项检查）

### 进行中

- [ ] `npx skills add` 一键安装
- [ ] 更多示例：健身团队、产品团队、内容创作流水线

### 后端演进路线

上帝造物术的定位是先把 Skill 系统做扎实，存储层逐步演进：

| 版本 | 存储 | 状态 |
|------|------|------|
| V1 | 纯 Markdown | ✅ 完成 |
| V2 | Markdown + 周/月复盘 | ✅ 当前版本 |
| V3 | Markdown + JSON 索引 | 规划中 |
| V4 | SQLite 本地数据库 | 规划中 |
| V5 | 运行时后端服务 | 远期 |

---

## Contributing

欢迎贡献！特别欢迎：

- **新示例**：用上帝生成一个团队，提交到 `examples/`
- **新领域**：在 `references/domain-patterns.md` 添加新的领域类型
- **质量检查**：完善 `quality_check.py` 的检查规则
- **平台适配**：添加 Cursor、Gemini CLI 等平台支持

请先开 Issue 讨论，再提 PR。

---

## License

MIT — 随便用，随便改，随便造。

---

<div align="center">

传统 Skill 教 AI 怎么说。<br>
上帝教 AI 怎么做。

</div>

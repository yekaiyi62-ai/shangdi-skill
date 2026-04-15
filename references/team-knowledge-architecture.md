# 团队知识库架构

> 团队Skill的三层知识架构设计规范。生成团队时，不只生成角色，还要生成知识库、记忆系统、读取规则和验证机制。

## 核心理念

**团队 = 角色 + 知识库 + 记忆系统 + 读取规则 + 验证机制**

不是生成一群会说话的空壳，而是生成一支带专业知识、能长期陪用户工作的 AI 团队。

---

## 一、三层知识架构

### 第一层：成员 SKILL.md（操作系统）

保存"这个角色怎么工作"，不塞满知识。

包含：
- 什么时候触发
- 接收什么输入
- 处理流程（Step by Step）
- 输出格式
- 什么时候读取哪些 reference
- 什么时候更新用户进度
- 能做什么，不能做什么

**原则**：SKILL.md 应该短而强，像角色的"操作系统"。

### 第二层：知识库（专业教材）

分两级存储：

#### 2a. 团队共享知识库 (`references/`)

所有成员都可能用到的通用知识：
- 考试/领域总体结构
- 官方评分标准/行业规范
- 通用方法论
- 常见错误分类
- 来源索引

#### 2b. 成员专属知识库 (`members/[role]/references/`)

只属于某个角色的专业知识：
- 角色专属的评分标准细则
- 角色专属的题型/任务分类
- 角色专属的训练方法
- 角色专属的案例库
- 角色专属的反馈语料

**原则**：共享知识放团队级，专属知识放成员级。避免重复，避免标准不一致。

### 第三层：用户记忆库 (`shared/`) — V2 长期记忆

动态变化的用户状态、短期记录和长期归档：

**核心文件**（所有团队必须有）：
- `[主体]-profile.md` — 核心对象档案（用户/宠物/产品/项目）
- `progress.md` 或 `[核心动作]-log.md` — 主要活动记录
- `session-log.md` — 每次会话摘要（保留最近 7 天）

**长期记忆文件**（推荐）：
- `weak-points.md` — 弱点状态追踪（有状态机：发现→训练中→待复查→已改善→已稳定→复发）
- `weekly-reviews.md` — 周复盘（保留最近 4 周）
- `monthly-summary.md` — 月度总结
- `archive/` — 历史归档目录

**领域特定文件**：
- 不同领域生成不同的 shared/ 文件。详见 `references/domain-patterns.md`。

**原则**：
- shared/ 只放用户状态，不放静态知识
- session-log 超过 7 天的记录归档到 `archive/week-XX.md`
- weekly-reviews 超过 4 周的归档
- 启动时不读 archive/，除非用户要求追溯历史

---

## 二、完整目录结构

```
[team-name]/
├── SKILL.md                              # 团队协调器（入口）
├── README.md                             # 团队说明
├── references/                           # 团队共享知识库
│   ├── knowledge-index.md                # 知识索引：什么问题读什么文件
│   ├── domain-overview.md                # 领域/考试总体结构
│   ├── official-standards.md             # 官方评分标准/行业规范
│   ├── common-errors.md                  # 通用常见错误分类
│   ├── source-index.md                   # 所有资料来源索引
│   └── research/                         # 调研原始数据（Phase 2产出）
│       ├── 01-xxx.md
│       └── 02-xxx.md
├── members/                              # 团队成员
│   ├── [role-1]/
│   │   ├── SKILL.md                      # 角色工作流
│   │   └── references/                   # 角色专属知识库
│   │       ├── [role]-rubric.md          # 专属评分标准/规则
│   │       ├── [role]-patterns.md        # 专属题型/任务模式
│   │       ├── [role]-methods.md         # 专属训练/处理方法
│   │       └── [role]-feedback-bank.md   # 专属反馈语料/案例
│   ├── [role-2]/
│   │   ├── SKILL.md
│   │   └── references/
│   └── ...
├── shared/                               # 用户状态和团队记忆（V2 长期记忆）
│   ├── user-profile.md                   # 用户档案（或 pet-profile.md 等）
│   ├── progress.md                       # 练习记录和分数趋势
│   ├── weak-points.md                    # 弱点状态追踪（含状态机）
│   ├── session-log.md                    # 会话摘要（保留最近 7 天）
│   ├── weekly-reviews.md                 # 周复盘（保留最近 4 周）
│   ├── monthly-summary.md               # 月度总结
│   └── archive/                          # 历史归档
│       ├── week-01.md
│       └── week-02.md
└── scripts/                              # 自动化工具（可选）
    └── quality_check.py
```

---

## 三、知识索引 (knowledge-index.md)

知识索引是团队的"导航系统"，告诉模型什么问题该读哪个文件。

### 格式规范

```markdown
# Knowledge Index

> 协调器和成员根据此索引按需读取知识文件。不要一次性读取所有资料。

## 按任务类型索引

| 任务类型 | 应读取文件 |
|---------|-----------|
| [任务1] | `references/xxx.md` + `members/[role]/references/xxx.md` |
| [任务2] | `references/xxx.md` + `shared/user-profile.md` |
| [任务3] | `members/[role]/references/xxx.md` + `shared/progress.md` |

## 按角色索引

| 角色 | 启动时必读 | 按需读取 |
|------|-----------|---------|
| [角色1] | `shared/user-profile.md`, `members/[role-1]/references/xxx.md` | `references/official-standards.md` |
| [角色2] | `shared/user-profile.md`, `members/[role-2]/references/xxx.md` | `shared/progress.md` |

## 按知识文件索引

| 文件 | 内容摘要 | 谁会用到 |
|------|---------|---------|
| `references/official-standards.md` | 官方评分标准 | 所有评分类角色 |
| `members/writing-coach/references/writing-rubric.md` | 写作专属评分细则 | 写作教练 |
| `shared/progress.md` | 用户练习历史 | 协调器、规划师 |
```

### 设计原则

1. 知识索引不存全部内容，只存"什么问题该读哪个文件"
2. 每个角色启动时读知识索引，按需加载知识
3. 协调器转发任务时，附带需要读取的知识文件列表
4. 避免一次性加载所有资料浪费上下文

---

## 四、知识读取规则

### 协调器的读取规则

```markdown
## 知识读取规则

收到用户请求后：

1. 读取 `references/knowledge-index.md`，判断需要哪些知识文件
2. 读取 `shared/user-profile.md`，了解用户当前状态
3. 根据任务类型：
   - 如果自己处理（查进度/做计划）→ 读取对应知识文件
   - 如果转发给成员 → 告诉成员需要读取哪些文件
4. 不要一次性读取所有资料，只读取当前任务需要的文件
```

### 成员的读取规则

```markdown
## 知识读取规则

收到任务后：

1. 读取自己的 `references/` 目录下的专属知识
2. 按需读取团队共享的 `references/` 下的通用知识
3. 读取 `shared/user-profile.md` 了解用户情况
4. 按需读取 `shared/progress.md` 了解历史记录

### 具体场景的读取路径

| 场景 | 读取文件 |
|------|---------|
| [场景1] | `members/[self]/references/xxx.md` + `references/official-standards.md` |
| [场景2] | `members/[self]/references/xxx.md` + `shared/progress.md` |
| [场景3] | `references/domain-overview.md` + `shared/user-profile.md` |
```

### 写入规则

```markdown
## 写入规则

完成任务后：

1. 将本次练习/评估结果追加到 `shared/progress.md`
2. 如果发现用户水平有显著变化 → 更新 `shared/user-profile.md`
3. 如果发现新的弱点 → 更新 `shared/weak-points.md`
4. 知识库文件（`references/`）不在日常使用中修改
```

---

## 五、知识库内容规范

### 静态知识库的内容标准

每个知识库文件必须包含：

```markdown
# [知识主题]

> 一句话说明这个文件的用途和适用范围

## 来源

- 来源类型：[官方标准/行业规范/专家共识/调研总结]
- 来源链接：[URL 或文件路径]
- 最后更新：[日期]

## 内容

[具体的可操作知识，不是泛泛概述]
```

### 文件格式选择

| 内容类型 | 推荐格式 | 原因 |
|---------|---------|------|
| 评分标准、方法论、流程 | `.md` | 模型读取最自然，人也能直接看 |
| 练习记录、分数趋势、统计 | `.md`（第一阶段） / `.json`（第二阶段） | 先用 md 快速迭代，数据量大后迁移 json |
| 题库、词汇表 | `.md`（小量） / `.json`（大量） | 结构化数据量大时 json 更高效 |
| 错题集、案例库 | `.md` | 需要上下文说明，md 更合适 |

### 第一阶段 vs 第二阶段

**第一阶段**（当前）：全部用 `.md` 保存。
- 包括专业知识、提炼结果、评分标准、题型库、常见错误、使用规则
- 优点：人能看懂、GitHub 展示好、模型读取自然、不需要额外环境

**第二阶段**（数据量增长后）：结构化数据用 `.json` 或 `.yaml` 补充。
- `shared/progress.json` — 练习记录
- `shared/score-history.json` — 分数趋势
- `members/[role]/references/question-bank.json` — 题库
- 优点：结构化查询更高效、支持数据分析脚本

---

## 六、知识蒸馏流程

生成团队时，对每个成员角色执行知识蒸馏：

### Step 1: 识别知识需求

根据角色的能力矩阵，列出需要的知识维度：

```yaml
role: writing-coach
knowledge_needs:
  - 写作评分标准（官方 + 细化）
  - 写作题型分类和结构
  - 高分范文模式
  - 常见错误和反馈语料
  - 训练方法和进阶路径
```

### Step 2: 区分共享 vs 专属

| 知识维度 | 归属 | 文件位置 |
|---------|------|---------|
| 全局评分标准 | 团队共享 | `references/official-standards.md` |
| 写作评分细则 | 写作教练专属 | `members/writing-coach/references/writing-rubric.md` |
| 考试总结构 | 团队共享 | `references/domain-overview.md` |
| 写作题型 | 写作教练专属 | `members/writing-coach/references/writing-patterns.md` |
| 常见错误总分类 | 团队共享 | `references/common-errors.md` |
| 写作专属反馈 | 写作教练专属 | `members/writing-coach/references/feedback-bank.md` |

### Step 3: 调研与填充

- 团队共享知识：Phase 2 调研时统一处理
- 成员专属知识：Phase 2 为每个角色分配专属调研 Agent
- 用户提供的本地语料：按上述分类拆入对应文件

### Step 4: 生成知识索引

调研完成后，自动生成 `references/knowledge-index.md`，建立任务→文件的映射。

### Step 5: 验证知识覆盖

```
┌──────────┬────────────┬──────────┬──────────┐
│ 角色      │ 知识需求    │ 已覆盖    │ 缺失     │
├──────────┼────────────┼──────────┼──────────┤
│ [角色1]  │ [N]个维度   │ [M]个    │ [列表]   │
│ [角色2]  │ [N]个维度   │ [M]个    │ [列表]   │
└──────────┴────────────┴──────────┴──────────┘
```

缺失的知识维度要么补充调研，要么在诚实边界中标注。

---

## 七、长期记忆规范（V2）

### 记忆写入规则

每次任务完成后：
1. 更新 `progress.md`（或领域对应的 log 文件）
2. 追加 `session-log.md`
3. 如发现新弱点 → 写入 `weak-points.md`，必须包含证据和来源
4. 如旧弱点连续 2 次通过 → 更新状态为"待复查"
5. 如已改善弱点复发 → 标记为"复发"

### 弱点状态机

```
发现 → 训练中 → 待复查 → 已改善 → 已稳定
                    ↑          ↓         ↓
                    └── 复发 ←─┴─────────┘
```

每个弱点必须包含：名称、状态、首次发现日期、来源/证据、最近复查结果、下一步动作。

### 周复盘规则

1. 汇总本周 session-log 中的所有任务
2. 统计各模块练习次数和进度变化
3. 评估弱点状态变化
4. 生成下周重点建议
5. 将本周 session-log 归档到 `archive/week-XX.md`
6. 保留 session-log 最近 7 天内容

### 月度总结规则

1. 汇总月度 weekly-reviews
2. 重新评估目标可达性
3. 调整策略和资源分配
4. 生成下月计划

### 启动读取规则

每次启动团队时默认读取：
1. `shared/[主体]-profile.md`
2. `shared/weak-points.md`（如有）
3. `shared/progress.md` 最近 5-10 条
4. `shared/weekly-reviews.md` 最近 2 周
5. **不默认读取 `archive/`**，除非用户要求追溯历史

### 归档规则

| 文件 | 保留窗口 | 归档位置 |
|------|---------|---------|
| session-log.md | 最近 7 天 | `archive/week-XX.md` |
| weekly-reviews.md | 最近 4 周 | `archive/month-XX.md` |
| weak-points.md 已稳定项 | 稳定超 1 个月 | 移入"已稳定弱点（归档）"区块 |

---

## 八、团队生成清单

生成团队时，必须产出以下所有文件：

### 必须生成

- [ ] `SKILL.md` — 协调器，含知识读取规则和路由
- [ ] `references/knowledge-index.md` — 知识索引
- [ ] `references/domain-overview.md` — 领域总览
- [ ] `references/official-standards.md` — 官方标准/规范
- [ ] 每个成员的 `members/[role]/SKILL.md` — 含知识读取规则
- [ ] 每个成员的 `members/[role]/references/` — 至少一个专属知识文件
- [ ] `shared/[主体]-profile.md` — 核心对象档案
- [ ] `shared/progress.md` 或 `shared/[核心动作]-log.md` — 活动记录
- [ ] `shared/session-log.md` — 会话摘要
- [ ] `README.md` — 团队使用说明

### 推荐生成

- [ ] `references/common-errors.md` — 常见错误分类
- [ ] `references/source-index.md` — 资料来源索引
- [ ] `shared/weak-points.md` — 弱点状态追踪（能力提升类团队必须有）
- [ ] `shared/weekly-reviews.md` — 周复盘
- [ ] `shared/monthly-summary.md` — 月度总结
- [ ] `shared/archive/` — 历史归档

### 可选生成

- [ ] `scripts/quality_check.py` — 团队质量检查脚本
- [ ] `tests/` — 样本测试目录

---

## 八、常见领域的知识库模板

### 考试备考类团队

```
references/
├── knowledge-index.md
├── exam-overview.md          # 考试结构、时间、题型
├── official-rubrics.md       # 官方评分标准
├── score-conversion.md       # 分数换算、目标拆解
├── common-errors.md          # 学生常见错误分类
└── source-index.md

members/[科目]-coach/references/
├── [科目]-rubric.md          # 该科专属评分细则
├── [科目]-question-types.md  # 题型分类和应对策略
├── [科目]-methods.md         # 训练方法
└── [科目]-feedback-bank.md   # 常见反馈语料
```

### 产品/业务类团队

```
references/
├── knowledge-index.md
├── industry-overview.md      # 行业概览
├── best-practices.md         # 行业最佳实践
├── metrics-standards.md      # 关键指标和标准
└── source-index.md

members/[角色]/references/
├── [角色]-methodology.md     # 角色专属方法论
├── [角色]-templates.md       # 角色专属输出模板
└── [角色]-cases.md           # 角色专属案例库
```

### 代码开发类团队

```
references/
├── knowledge-index.md
├── architecture.md           # 项目架构概览
├── coding-standards.md       # 编码规范
├── tech-stack.md             # 技术栈说明
└── source-index.md

members/[角色]/references/
├── [角色]-checklist.md       # 角色专属检查清单
├── [角色]-patterns.md        # 角色专属模式/反模式
└── [角色]-tools.md           # 角色专属工具使用指南
```

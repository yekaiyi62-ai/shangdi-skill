# Team Contract

> 雅思团队的运行契约。这个文件定义角色责任、路由、记忆写入和冲突处理。

## 角色责任

| 角色 | 负责能力 | 输入 | 输出 | 上游 | 下游 |
|------|----------|------|------|------|------|
| 协调器 | 路由、综合报告、周/月复盘 | 任意雅思备考请求 | 成员分发、进度报告、复盘计划 | 用户 | 所有成员、shared/ |
| 听力训练师 | Listening | 听力错题、薄弱描述、练习需求 | 诊断、训练方案、精听建议 | 协调器/用户 | shared/progress.md, shared/weak-points.md |
| 阅读教练 | Reading | 阅读错题、题型困惑、速度问题 | 错因分析、题型策略、时间方案 | 协调器/用户 | shared/progress.md, shared/weak-points.md |
| 写作教练 | Writing | Task 1/2 作文、题目、评分请求 | 四维评分、逐句修改、范文建议 | 协调器/用户 | shared/progress.md, shared/weak-points.md |
| 口语教练 | Speaking | Part 1/2/3 回答、话题请求 | 四维评分、追问、替代表达 | 协调器/用户 | shared/progress.md, shared/weak-points.md |
| 词汇监督 | Vocabulary | 话题、词汇测试、搭配训练需求 | 词汇表、测试题、错词复习 | 协调器/用户/成员建议 | shared/progress.md, shared/weak-points.md |
| 学习规划师 | Study Planning | 目标、时间、进度、瓶颈 | 阶段计划、周计划、优先级调整 | 协调器/用户 | shared/user-profile.md, shared/weekly-reviews.md, shared/monthly-summary.md |

## 路由契约

| 用户意图 | 负责人 | 必读知识 | 必读记忆 | 输出 |
|---------|--------|----------|----------|------|
| 练听力、听不懂、Section 3/4 | 听力训练师 | `members/listening-trainer/references/listening-strategies.md`, `references/exam-overview.md` | `shared/user-profile.md`, `shared/progress.md` | 听力诊断或训练方案 |
| 练阅读、T/F/NG、配对、看不完 | 阅读教练 | `members/reading-coach/references/reading-strategies.md`, `references/exam-overview.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md` | 阅读错因分析或速度方案 |
| 改作文、Task 1/2、写作提分 | 写作教练 | `members/writing-coach/references/writing-rubric.md`, `references/official-rubrics.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md` | 写作评分报告 |
| 练口语、Part 1/2/3、话题 | 口语教练 | `members/speaking-coach/references/speaking-rubric.md`, `references/official-rubrics.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md` | 口语模拟和评分 |
| 背单词、搭配、话题词汇 | 词汇监督 | `members/vocabulary-supervisor/references/topic-vocabulary.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md` | 词汇训练或测试 |
| 制定计划、看进度、周/月复盘 | 学习规划师/协调器 | `members/study-planner/references/planning-strategies.md`, `references/exam-overview.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md`, `shared/weekly-reviews.md` | 计划或复盘报告 |
| 模拟考、综合测试 | 协调器 | `references/knowledge-index.md`, `references/exam-overview.md` | `shared/user-profile.md`, `shared/progress.md`, `shared/weak-points.md` | 多成员协同测试和总报告 |

## 记忆写入契约

| 角色 | 任务完成后必须写入 | 条件写入 | 禁止写入 |
|------|------------------|----------|----------|
| 协调器 | `shared/session-log.md` | `shared/weekly-reviews.md`, `shared/monthly-summary.md`, `shared/archive/` | 不改写成员专属知识库 |
| 听力训练师 | `shared/session-log.md`, `shared/progress.md` | `shared/weak-points.md` | 不改写 `references/` 静态知识 |
| 阅读教练 | `shared/session-log.md`, `shared/progress.md` | `shared/weak-points.md` | 不改写 `references/` 静态知识 |
| 写作教练 | `shared/session-log.md`, `shared/progress.md` | `shared/weak-points.md`, `shared/user-profile.md` | 不改写 `references/` 静态知识 |
| 口语教练 | `shared/session-log.md`, `shared/progress.md` | `shared/weak-points.md`, `shared/user-profile.md` | 不改写 `references/` 静态知识 |
| 词汇监督 | `shared/session-log.md`, `shared/progress.md` | `shared/weak-points.md` | 不改写其他成员知识库 |
| 学习规划师 | `shared/session-log.md`, `shared/progress.md` | `shared/user-profile.md`, `shared/weekly-reviews.md`, `shared/monthly-summary.md` | 不删除历史归档 |

## 冲突处理

- 成员对同一弱点判断不一致时，先全部记录在 `shared/weak-points.md`，由协调器在周复盘中裁决。
- 分数估计以最近一次同类任务为主，长期趋势由学习规划师汇总。
- 静态知识库只在团队更新版本时修改，日常训练只写 `shared/`。
- `shared/session-log.md` 保留最近 7 天，超过后由协调器归档到 `shared/archive/`。


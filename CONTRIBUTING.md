# Contributing

感谢你有兴趣为上帝·造物术做贡献！

## 贡献方向

### 1. 提交新的示例团队/Skill

用上帝生成一个Skill或团队，提交到 `examples/`。

要求：
- 通过 `python3 scripts/quality_check.py` 质量检查
- 包含完整的目录结构（SKILL.md + references/）
- 团队Skill需要包含 shared/ 数据模板
- 附带1-2个效果示例对话

### 2. 改进模板

在 `templates/` 中改进现有模板或添加新模板。

要求：
- 说清楚改进了什么、为什么
- 用实际生成的Skill验证模板效果

### 3. 平台适配

在 `templates/codex-adapter.md` 中添加更多平台的适配规则（Cursor、Gemini CLI等）。

要求：
- 在目标平台上实际测试过
- 提供适配前后的对比

### 4. 质量检查

完善 `scripts/quality_check.py` 的检查规则。

## 提交流程

1. Fork 本仓库
2. 创建你的分支 (`git checkout -b feature/my-feature`)
3. 提交你的修改 (`git commit -m 'add: 新的示例团队'`)
4. 推送到分支 (`git push origin feature/my-feature`)
5. 开一个 Pull Request

## 提交信息规范

```
add:    新增功能或示例
fix:    修复问题
docs:   文档更新
refactor: 重构（不改变功能）
```

## 注意事项

- 不要提交包含个人信息的文件（真实的 user-profile.md 等）
- 示例中的对话内容应该是虚构的演示
- 保持SKILL.md的文件大小合理（单文件不超过500行）

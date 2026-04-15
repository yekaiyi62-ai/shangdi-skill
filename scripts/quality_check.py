#!/usr/bin/env python3
"""
检查生成的Skill是否通过质量标准。
支持功能Skill、人物Skill和团队Skill。
V2: 增加知识库、长期记忆、弱点状态机、文件路径验证。

用法:
    python3 quality_check.py <SKILL.md路径>
    python3 quality_check.py <团队目录路径> --team
"""

import sys
import re
from pathlib import Path


def check_routing(content: str) -> tuple[bool, str]:
    """检查是否有问题路由"""
    has_routing = bool(re.search(r'问题路由|路由|场景[A-Z]|场景\d|问题分类', content))
    return has_routing, "有问题路由 ✅" if has_routing else "❌ 未找到问题路由"


def check_workflow(content: str) -> tuple[bool, str]:
    """检查是否有完整工作流（Step定义）"""
    steps = re.findall(r'Step\s*\d|步骤\s*\d', content, re.IGNORECASE)
    count = len(steps)
    passed = count >= 2
    return passed, f"工作流步骤: {count}个 {'✅' if passed else '❌ (应≥2个)'}"


def check_io_definition(content: str) -> tuple[bool, str]:
    """检查是否有输入输出定义"""
    has_input = bool(re.search(r'输入|input|接收|收到', content, re.IGNORECASE))
    has_output = bool(re.search(r'输出|output|产出|格式规范|输出格式', content, re.IGNORECASE))
    passed = has_input and has_output
    detail = f"输入{'✅' if has_input else '❌'} 输出{'✅' if has_output else '❌'}"
    return passed, detail


def check_capability_boundary(content: str) -> tuple[bool, str]:
    """检查是否有能力边界说明"""
    has_can = bool(re.search(r'能做|能力范围|擅长|可以', content))
    has_cannot = bool(re.search(r'不能|不擅长|局限|边界|做不到', content))
    passed = has_can and has_cannot
    detail = f"能做{'✅' if has_can else '❌'} 不能做{'✅' if has_cannot else '❌'}"
    return passed, detail


def check_checkpoints(content: str) -> tuple[bool, str]:
    """检查是否有用户确认检查点"""
    has_checkpoint = bool(re.search(r'检查点|确认|checkpoint|用户选|用户确认', content, re.IGNORECASE))
    return has_checkpoint, "有检查点 ✅" if has_checkpoint else "⚠️ 未找到检查点（建议添加）"


def check_output_format(content: str) -> tuple[bool, str]:
    """检查是否有输出格式规范"""
    has_format = bool(re.search(r'输出格式|格式规范|报告格式|模板|format', content, re.IGNORECASE))
    return has_format, "有输出格式规范 ✅" if has_format else "❌ 未找到输出格式规范"


def check_domain_knowledge(content: str) -> tuple[bool, str]:
    """检查是否有领域知识"""
    has_knowledge = bool(re.search(r'领域知识|评分标准|方法论|行业|专业|标准|策略|规律|规则', content))
    return has_knowledge, "有领域知识 ✅" if has_knowledge else "⚠️ 未找到领域知识section"


def check_frontmatter(content: str) -> tuple[bool, str]:
    """检查是否有正确的frontmatter"""
    has_fm = content.strip().startswith('---')
    if has_fm:
        has_name = bool(re.search(r'^name:', content, re.MULTILINE))
        has_desc = bool(re.search(r'^description:', content, re.MULTILINE))
        passed = has_name and has_desc
        return passed, f"frontmatter: name{'✅' if has_name else '❌'} description{'✅' if has_desc else '❌'}"
    return False, "❌ 缺少frontmatter"


def check_knowledge_reading_rules(content: str) -> tuple[bool, str]:
    """检查是否有知识读取规则"""
    has_rules = bool(re.search(r'知识读取规则|启动时必读|按场景读取|启动时', content))
    return has_rules, "有知识读取规则 ✅" if has_rules else "⚠️ 未找到知识读取规则"


def check_session_log_writing(content: str) -> tuple[bool, str]:
    """检查是否有session-log写入规则"""
    has_session = bool(re.search(r'session-log|会话摘要|会话记录', content))
    return has_session, "有session-log写入 ✅" if has_session else "⚠️ 未找到session-log写入规则"


def check_weak_point_rules(content: str) -> tuple[bool, str]:
    """检查是否有弱点追踪规则"""
    has_weak = bool(re.search(r'weak-points|弱点|薄弱', content))
    return has_weak, "有弱点追踪规则 ✅" if has_weak else "⚠️ 未找到弱点追踪规则"


# === 团队级检查 ===

def check_knowledge_index(team_dir: Path) -> tuple[bool, str]:
    """检查是否有知识索引文件"""
    ki = team_dir / "references" / "knowledge-index.md"
    if ki.exists():
        content = ki.read_text(encoding='utf-8')
        has_table = bool(re.search(r'\|.*\|.*\|', content))
        return has_table, f"knowledge-index.md 存在且有路由表 ✅" if has_table else "knowledge-index.md 存在但缺少路由表 ⚠️"
    return False, "❌ 缺少 references/knowledge-index.md"


def check_shared_memory_files(team_dir: Path) -> tuple[bool, str]:
    """检查shared/下的长期记忆文件是否完整"""
    shared = team_dir / "shared"
    required = ['user-profile.md', 'progress.md', 'weak-points.md',
                'session-log.md', 'weekly-reviews.md', 'monthly-summary.md']
    missing = [f for f in required if not (shared / f).exists()]
    archive = shared / "archive"

    if not shared.exists():
        return False, "❌ 缺少 shared/ 目录"

    details = []
    if missing:
        details.append(f"缺少: {', '.join(missing)}")
    if not archive.exists():
        details.append("缺少 archive/ 目录")

    passed = len(missing) == 0 and archive.exists()
    if passed:
        return True, f"shared/ 完整 ({len(required)}个文件 + archive/) ✅"
    return False, f"❌ shared/ 不完整: {'; '.join(details)}"


def check_member_references(team_dir: Path) -> tuple[bool, str]:
    """检查每个成员是否有专属知识库"""
    members_dir = team_dir / "members"
    if not members_dir.exists():
        return False, "❌ 缺少 members/ 目录"

    results = []
    all_have_refs = True
    for member_dir in sorted(members_dir.iterdir()):
        if not member_dir.is_dir():
            continue
        refs = member_dir / "references"
        if refs.exists() and any(refs.iterdir()):
            results.append(f"{member_dir.name}✅")
        else:
            results.append(f"{member_dir.name}❌")
            all_have_refs = False

    detail = f"成员知识库: {' '.join(results)}"
    return all_have_refs, detail


def check_weak_points_state_machine(team_dir: Path) -> tuple[bool, str]:
    """检查weak-points.md是否包含状态机"""
    wp = team_dir / "shared" / "weak-points.md"
    if not wp.exists():
        return False, "❌ weak-points.md 不存在"
    content = wp.read_text(encoding='utf-8')
    states = ['发现', '训练中', '待复查', '已改善', '已稳定', '复发']
    found = [s for s in states if s in content]
    passed = len(found) >= 4
    return passed, f"弱点状态机: {len(found)}/{len(states)}个状态 {'✅' if passed else '⚠️'}"


def check_file_paths_in_skill(content: str, skill_dir: Path, member_dir=None) -> tuple[bool, str]:
    """检查SKILL.md中引用的文件路径是否存在。

    - shared/ 和 members/ 路径：相对于 skill_dir（团队根目录）
    - references/ 路径：优先在 member_dir 下查找，其次在 skill_dir 下查找
    """
    refs = re.findall(r'`((?:members|shared|references)/[^`]+\.md)`', content)
    if not refs:
        return True, "无文件引用（跳过）"

    missing = []
    checked = set()
    for ref in refs:
        if ref in checked:
            continue
        checked.add(ref)
        if ref.startswith('references/') and member_dir:
            # Try member's own references dir first
            if (member_dir / ref).exists():
                continue
        full_path = skill_dir / ref
        if not full_path.exists():
            missing.append(ref)

    if missing:
        return False, f"❌ 引用文件不存在: {', '.join(missing[:5])}"
    return True, f"文件引用验证: {len(checked)}个路径全部存在 ✅"


def check_semantic_coverage(team_dir: Path) -> tuple[bool, str]:
    """语义覆盖检查：协调器/knowledge-index/progress中提到的核心模块，是否都有对应成员。

    从协调器SKILL.md和knowledge-index.md中提取核心能力词，
    然后检查members/下是否有对应角色目录。
    """
    # 从协调器和知识索引中提取关键能力词
    ability_texts = []
    coord = team_dir / "SKILL.md"
    ki = team_dir / "references" / "knowledge-index.md"
    for f in [coord, ki]:
        if f.exists():
            ability_texts.append(f.read_text(encoding='utf-8'))
    combined = '\n'.join(ability_texts).lower()

    # 获取实际成员目录
    members_dir = team_dir / "members"
    if not members_dir.exists():
        return False, "❌ 缺少 members/ 目录，无法做语义覆盖检查"
    member_names = [d.name.lower() for d in members_dir.iterdir() if d.is_dir()]

    # 定义能力信号词 → 期望的成员名关键字
    # 每项：(能力描述, [文档中可能出现的信号词], [成员名中应包含的词之一])
    ability_signals = [
        ("阅读/Reading", ['阅读', 'reading', 'r/w'],
         ['reading', 'read']),
        ("写作/Writing", ['写作', 'writing', 'task 1', 'task 2', '作文'],
         ['writing', 'write', 'essay']),
        ("听力/Listening", ['听力', 'listening', '精听', 'section'],
         ['listening', 'listen']),
        ("口语/Speaking", ['口语', 'speaking', 'part 1', 'part 2', 'part 3'],
         ['speaking', 'speak']),
    ]

    gaps = []
    covered = []
    for ability_name, signals, member_keywords in ability_signals:
        # 检查文档中是否出现这个能力的信号词
        mentioned = any(s.lower() in combined for s in signals)
        if not mentioned:
            continue  # 文档没提到这个能力，跳过
        # 检查是否有对应成员
        has_member = any(
            any(kw in mname for kw in member_keywords)
            for mname in member_names
        )
        if has_member:
            covered.append(ability_name)
        else:
            gaps.append(ability_name)

    if gaps:
        return False, (
            f"❌ 语义覆盖缺口: 文档提到 {gaps}，但 members/ 下没有对应角色\n"
            f"   已覆盖: {covered}"
        )
    if covered:
        return True, f"语义覆盖完整: {covered} 均有对应成员 ✅"
    return True, "语义覆盖检查：无特定能力信号词（跳过）"


def check_routing_completeness(team_dir: Path) -> tuple[bool, str]:
    """路由完整性检查：协调器路由中出现的意图，必须有对应成员或明确说明由谁处理。"""
    coord = team_dir / "SKILL.md"
    if not coord.exists():
        return False, "❌ 缺少协调器 SKILL.md"

    content = coord.read_text(encoding='utf-8')
    members_dir = team_dir / "members"
    if not members_dir.exists():
        return True, "无 members/ 目录（跳过路由检查）"

    member_names = [d.name.lower() for d in members_dir.iterdir() if d.is_dir()]

    # 从路由表中提取「转发给」的角色名
    routed_to = re.findall(r'转发给.*?([^\s|]+coach|[^\s|]+trainer|[^\s|]+师|[^\s|]+员|[^\s|]+官|[^\s|]+planner)',
                           content)

    # 检查「协调器自己处理」的情况下有没有对应工作流
    self_handled = re.findall(r'协调器自己处理|协调器.*?处理', content)

    issues = []
    # 简单检查：路由表有几个意图，成员数量是否能覆盖
    routing_rows = re.findall(r'\|[^|]+\|[^|]+\|[^|]+\|', content)
    routing_count = len([r for r in routing_rows if '触发词' not in r and '意图' not in r and '用户意图' not in r])

    if routing_count < len(member_names):
        issues.append(f"路由项（{routing_count}个）少于成员数（{len(member_names)}个），可能有成员未被路由覆盖")

    if issues:
        return False, f"⚠️ 路由完整性问题: {'; '.join(issues)}"
    return True, f"路由完整性: {routing_count}个路由意图，{len(member_names)}个成员 ✅"


def check_team(team_dir: Path) -> None:
    """检查团队Skill"""
    print(f"团队检查: {team_dir.name}")
    print("=" * 60)

    # === 团队级检查 ===
    print("\n🏗️  团队结构检查:")
    team_checks = [
        ("知识索引", lambda: check_knowledge_index(team_dir)),
        ("长期记忆", lambda: check_shared_memory_files(team_dir)),
        ("成员知识库", lambda: check_member_references(team_dir)),
        ("弱点状态机", lambda: check_weak_points_state_machine(team_dir)),
        ("语义覆盖", lambda: check_semantic_coverage(team_dir)),
        ("路由完整性", lambda: check_routing_completeness(team_dir)),
    ]

    team_passed = 0
    for name, check_fn in team_checks:
        passed, detail = check_fn()
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<12} {status}  {detail}")
        if passed:
            team_passed += 1

    print(f"  {'─' * 50}")
    print(f"  团队结构: {team_passed}/{len(team_checks)} 通过")

    # === 协调器检查 ===
    coord = team_dir / "SKILL.md"
    if coord.exists():
        print(f"\n📋 协调器: {coord.name}")
        content = coord.read_text(encoding='utf-8')
        run_checks(content, is_coordinator=True, skill_dir=team_dir)
    else:
        print("\n❌ 缺少协调器 SKILL.md")

    # === 成员检查 ===
    members_dir = team_dir / "members"
    if members_dir.exists():
        for member_dir in sorted(members_dir.iterdir()):
            if not member_dir.is_dir():
                continue
            skill_file = member_dir / "SKILL.md"
            if skill_file.exists():
                print(f"\n👤 成员: {member_dir.name}")
                content = skill_file.read_text(encoding='utf-8')
                # Members resolve `references/` paths relative to their own dir,
                # but `shared/` and `members/` paths relative to team dir.
                run_checks(content, skill_dir=team_dir, member_dir=member_dir)
    else:
        print("\n⚠️ 无 members/ 目录")


def run_checks(content: str, is_coordinator: bool = False, skill_dir=None, member_dir=None) -> int:
    checks = [
        ("frontmatter", check_frontmatter),
        ("问题路由", check_routing),
        ("工作流", check_workflow),
        ("检查点", check_checkpoints),
        ("输出格式", check_output_format),
    ]

    # 协调器是路由层，不要求输入输出定义和能力边界
    if not is_coordinator:
        checks.insert(3, ("输入输出", check_io_definition))
        checks.insert(4, ("能力边界", check_capability_boundary))
        checks.append(("领域知识", check_domain_knowledge))

    # V2: 团队成员额外检查
    checks.append(("知识读取规则", check_knowledge_reading_rules))
    checks.append(("会话日志写入", check_session_log_writing))
    checks.append(("弱点追踪", check_weak_point_rules))

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<12} {status}  {detail}")
        if passed:
            passed_count += 1

    # V2: 文件路径验证（members的references/相对于member_dir，shared/和members/相对于team_dir）
    if skill_dir:
        passed, detail = check_file_paths_in_skill(content, skill_dir, member_dir)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {'文件路径':<12} {status}  {detail}")
        total += 1
        if passed:
            passed_count += 1

    print(f"  {'─' * 50}")
    print(f"  结果: {passed_count}/{total} 通过")
    return passed_count


def main():
    if len(sys.argv) < 2:
        print("用法: python3 quality_check.py <SKILL.md路径>")
        print("      python3 quality_check.py <团队目录> --team")
        sys.exit(1)

    path = Path(sys.argv[1])
    is_team = '--team' in sys.argv

    if is_team:
        if not path.is_dir():
            print(f"❌ 不是目录: {path}")
            sys.exit(1)
        check_team(path)
    else:
        if not path.exists():
            print(f"❌ 文件不存在: {path}")
            sys.exit(1)
        content = path.read_text(encoding='utf-8')
        print(f"质量检查: {path.name}")
        print("=" * 60)
        run_checks(content)


if __name__ == '__main__':
    main()

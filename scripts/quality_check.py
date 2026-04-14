#!/usr/bin/env python3
"""
检查生成的Skill是否通过质量标准。
支持功能Skill、人物Skill和团队Skill。

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
    has_knowledge = bool(re.search(r'领域知识|评分标准|方法论|行业|专业|标准', content))
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


def check_team(team_dir: Path) -> None:
    """检查团队Skill"""
    print(f"团队检查: {team_dir.name}")
    print("=" * 50)

    # 检查协调器
    coord = team_dir / "SKILL.md"
    if coord.exists():
        print(f"\n📋 协调器: {coord}")
        run_checks(coord.read_text(encoding='utf-8'), is_coordinator=True)
    else:
        print("❌ 缺少协调器 SKILL.md")

    # 检查成员
    members_dir = team_dir / "members"
    if members_dir.exists():
        for member_dir in sorted(members_dir.iterdir()):
            skill_file = member_dir / "SKILL.md"
            if skill_file.exists():
                print(f"\n👤 成员: {member_dir.name}")
                run_checks(skill_file.read_text(encoding='utf-8'))
    else:
        print("⚠️ 无 members/ 目录")

    # 检查共享数据
    shared_dir = team_dir / "shared"
    if shared_dir.exists():
        files = list(shared_dir.iterdir())
        print(f"\n📁 共享数据: {len(files)}个文件 ✅")
    else:
        print("\n⚠️ 无 shared/ 目录")


def run_checks(content: str, is_coordinator: bool = False) -> int:
    checks = [
        ("frontmatter", check_frontmatter),
        ("问题路由", check_routing),
        ("工作流", check_workflow),
        ("输入输出", check_io_definition),
        ("能力边界", check_capability_boundary),
        ("检查点", check_checkpoints),
        ("输出格式", check_output_format),
    ]

    if not is_coordinator:
        checks.append(("领域知识", check_domain_knowledge))

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<12} {status}  {detail}")
        if passed:
            passed_count += 1

    print(f"  {'─' * 40}")
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
        print("=" * 50)
        run_checks(content)


if __name__ == '__main__':
    main()

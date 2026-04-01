from pathlib import Path
import subprocess
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
ROOT_LOCAL_GUIDES = (
    ".agents/AGENTS.md",
    ".agents/skills/AGENTS.md",
    "docs/AGENTS.md",
    "docs/live/AGENTS.md",
    "docs/reference/AGENTS.md",
)
TEMPLATE_LOCAL_GUIDES = (
    "templates/base/.agents/AGENTS.md",
    "templates/base/.agents/skills/AGENTS.md",
    "templates/base/.agents/skills-optional/AGENTS.md",
    "templates/base/docs/AGENTS.md",
    "templates/base/docs/live/AGENTS.md",
    "templates/base/docs/reference/AGENTS.md",
)
BOUNDARY_HEADINGS = (
    "## Local Scope",
    "## Owns",
    "## Does Not Own",
    "## Required Reads",
    "## Local Update Rules",
    "## Failure Modes to Avoid",
)
ROOT_ROUTER_SNIPPETS = (
    "## Startup Minimum",
    "repo work",
    "template work",
    "## Decision Order",
    "## Escalation Rules",
    "## Failure Modes to Avoid",
    "## Discovery Index",
    ".agents/AGENTS.md",
    "docs/AGENTS.md",
    "templates/base/AGENTS.md",
    "python3 scripts/validate_agents_router.py",
)


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


class AgentsRouterTests(unittest.TestCase):
    def test_root_guide_behaves_like_router(self) -> None:
        root = read("AGENTS.md")
        for snippet in ROOT_ROUTER_SNIPPETS:
            self.assertIn(snippet, root)

    def test_repo_local_guides_exist_and_use_boundary_contract_shape(self) -> None:
        for relative in ROOT_LOCAL_GUIDES:
            path = REPO_ROOT / relative
            self.assertTrue(path.exists(), relative)
            content = path.read_text(encoding="utf-8")
            for heading in BOUNDARY_HEADINGS:
                self.assertIn(heading, content, f"{relative} missing {heading!r}")

    def test_template_local_guides_use_boundary_contract_shape(self) -> None:
        for relative in TEMPLATE_LOCAL_GUIDES:
            content = read(relative)
            for heading in BOUNDARY_HEADINGS:
                self.assertIn(heading, content, f"{relative} missing {heading!r}")

    def test_router_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_agents_router.py"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

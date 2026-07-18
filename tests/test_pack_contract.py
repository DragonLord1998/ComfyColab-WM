from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WorldModelContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            (ROOT / "comfycolab-pack.json").read_text(encoding="utf-8")
        )

    def test_manifest_is_explicitly_zero_capability(self) -> None:
        self.assertEqual(self.manifest["schema"], 1)
        self.assertEqual(self.manifest["id"], "world")
        for key in (
            "node_roots",
            "dependencies",
            "patches",
            "environments",
            "workflows",
            "probes",
            "accelerators",
            "licenses",
        ):
            self.assertEqual(self.manifest[key], [], key)
        self.assertEqual(self.manifest["health_checks"]["node_ids"], [])

    def test_release_hygiene_is_explicitly_prerelease(self) -> None:
        version = self.manifest["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+-dev\.\d+$")
        project = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn(f'version = "{version}"', project)
        self.assertTrue((ROOT / "CHANGELOG.md").is_file())
        self.assertTrue((ROOT / "CONTRIBUTING.md").is_file())

    def test_hooks_are_offline_noops(self) -> None:
        for hook in self.manifest["hooks"].values():
            self.assertEqual(hook["network"], "none")
            self.assertEqual(hook["write_roots"], [])
            self.assertTrue((ROOT / hook["path"]).is_file())

    def test_repository_contains_no_custom_node_or_model_payload(self) -> None:
        self.assertFalse((ROOT / "custom_nodes").exists())
        self.assertFalse((ROOT / "models").exists())
        self.assertEqual(list((ROOT / "workflows").glob("*.json")), [])


if __name__ == "__main__":
    unittest.main()

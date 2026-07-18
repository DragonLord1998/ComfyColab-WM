# ComfyColab World Model

This repository is a contract-only placeholder for a future, real world-model
capability. It currently installs no dependencies, registers no ComfyUI node
root, downloads no model, exposes no public node, ships no workflow, and makes
no inference or quality claim.

The first real implementation must define its model, license, runtime,
state/temporal semantics, native boundary types, workflows, live validation,
and accelerator requirements in an independently reviewed release. Until then,
the manifest intentionally remains zero-dependency and zero-capability.

## Development status

The current version is `0.0.0-dev.0`. It marks a contract skeleton, not an
installable world-model capability or a release candidate.

## Validation tiers

Local validation confirms that the repository remains an honest,
zero-capability placeholder:

```bash
PYTHON=/path/to/python3 bash scripts/check.sh
```

There is currently no live inference validation because there is no model,
node, workflow, or runtime to execute. Any future capability must introduce a
separate live Colab/GPU validation plan and must not reinterpret this local
placeholder check as inference proof.

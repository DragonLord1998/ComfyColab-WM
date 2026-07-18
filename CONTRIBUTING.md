# Contributing to ComfyColab World Model

## Current boundary

This repository is intentionally zero-capability. Documentation and contract
maintenance are welcome, but adding a model, dependency, node, workflow,
runtime, or accelerator requirement is a capability proposal and requires
independent architecture, license, and validation review.

Generic Colab installation belongs in ComfyColab core. Image, video, mesh, and
Gaussian-splat capabilities belong in their respective domain packs.

## Local validation

Run:

```bash
PYTHON=/path/to/python3 bash scripts/check.sh
```

The suite verifies that the manifest, hooks, and repository payload remain
empty and honest. It is not an inference test.

## Introducing the first capability

A future implementation must define:

- model and source revisions, licenses, and artifact integrity;
- state, temporal, and native boundary semantics;
- node IDs, workflows, runtime isolation, and accelerator requirements;
- deterministic local contract tests;
- a separate live Colab/GPU plan with real artifact and quality evidence.

Update the version, changelog, manifest, notices, and validation documentation
together. Never describe a local contract pass as live inference proof.

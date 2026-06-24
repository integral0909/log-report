# dynamo/log-report

A Terminal-Bench 2 (Harbor) task. The agent parses an Apache-style access log at
`/app/access.log` and writes a small JSON summary to `/app/report.json` with three
keys: `total_requests`, `unique_ips`, and `top_path`.

## Layout
- `instruction.md` — the prompt the agent sees (absolute paths, numbered success criteria).
- `solution/solve.sh` → `solution/solve.py` — reference (oracle) solution; writes `/app/report.json`.
- `environment/Dockerfile` — single image (digest-pinned base, pinned pytest/pytest-json-ctrf); `environment/access.log` is the seed input.
- `tests/test.sh` + `tests/test_outputs.py` — verifier; asserts the real values and writes `reward.txt` + `ctrf.json` to `/logs/verifier/`.
- `task.toml` — manifest; `artifacts = ["/app/report.json"]`.

## Verification
```
harbor run -p . --agent oracle   # reward 1.0
harbor run -p . --agent nop       # reward 0.0
```

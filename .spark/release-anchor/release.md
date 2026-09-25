# Release: release-anchor

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `handed-off` |
| **Version** | vX.Y.Z |
| **Date** | 2026-09-24 |
| **Commit** | pending — filled by Andreas's merge |
| **PR** | pending — this PR |

## 2. Changelog

### Added

- Releases of aSPARK-driven projects now carry a traceable git anchor:
  Commit and PR rows in the `release.md` header, filled with executed
  results, plus an append-only project-level `.spark/releases.md` index.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | proposed only (pr mode) |
| PR / merge | this PR |
| Deploy | N/A — prompt material |
| Post-release smoke check | N/A — prompt material |

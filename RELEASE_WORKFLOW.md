# Release Workflow

This repository uses Git tags and GitHub releases as the source of truth for release versions.

Do not update per-file version or date headers for each release. Release information belongs in Git tags, GitHub releases, and release notes.

## Recommended workflow

### 1. Track work with issues

Create an issue for fixes, features, or cleanup work:

```bash
gh issue create \
  --title "Fix WebContainerSec.py header setting from menu execution" \
  --body "Describe the problem, expected behavior, and suspected cause."
```

Reference or close the issue in the commit message when appropriate:

```text
Fix WebContainerSec appServer import

Closes #17
```

### 2. Make and verify changes

Before release, review the changed files:

```bash
git status
git diff --check
git diff --stat
```

For this Jython codebase, local Python 3 syntax checks are not generally useful because many scripts use Jython/Python 2 syntax and WebSphere globals such as `AdminConfig`, `AdminTask`, and `AdminApp`.

### 3. Commit changes

Use a clear commit message:

```bash
git add <files>
git commit -m "Fix WebContainerSec appServer import" -m "Closes #17"
```

Push the branch:

```bash
git push origin master
```

### 4. Choose the release version

Use the IBM Connections CR level as the base version. For fixes after that release, append a patch suffix.

Examples:

- `8.0.14` — release for IBM Connections 8.0 CR14
- `8.0.14.1` — first fix release for CR14 scripts
- `8.0.14.2` — second fix release for CR14 scripts

### 5. Create and push an annotated tag

```bash
git tag -a 8.0.14.2 -m "Release 8.0.14.2"
git push origin 8.0.14.2
```

### 6. Create a GitHub release

Preferred: let GitHub generate release notes automatically:

```bash
gh release create 8.0.14.2 \
  --title "Release 8.0.14.2" \
  --generate-notes
```

Manual notes are also possible:

```bash
gh release create 8.0.14.2 \
  --title "Release 8.0.14.2" \
  --notes "Bugfix release for IBM Connections 8.0 CR14 scripts."
```

## Changelog options

### Automatic GitHub release notes

Use this for normal releases:

```bash
gh release create <tag> --title "Release <tag>" --generate-notes
```

This works best when commits and pull requests reference issues and use clear titles.

### Simple changelog from commits

Preview changes since the previous release:

```bash
git log --oneline <previous-tag>..HEAD
```

Create release notes from commit subjects:

```bash
gh release create <tag> \
  --title "Release <tag>" \
  --notes "$(git log --pretty='- %s' <previous-tag>..HEAD)"
```

### Dedicated changelog tools

If the project later needs a maintained `CHANGELOG.md`, consider using one of these tools:

- `git-cliff`
- `release-please`

For now, GitHub generated release notes are sufficient.

## Full example

```bash
git status
git diff --check

git add ibmcnx/config/WebContainerSec.py
git commit -m "Fix WebContainerSec appServer import" -m "Closes #17"

git push origin master

git tag -a 8.0.14.2 -m "Release 8.0.14.2"
git push origin 8.0.14.2

gh release create 8.0.14.2 \
  --title "Release 8.0.14.2" \
  --generate-notes
```

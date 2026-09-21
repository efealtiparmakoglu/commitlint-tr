"""commitlint-tr: conventional commit message linter."""
import sys, re

TYPES = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"}
MAX_LEN = 72

def lint(msg):
    issues = []
    if not msg.strip():
        return ["message is empty"]
    lines = msg.splitlines()
    subject = lines[0]
    if len(subject) > MAX_LEN:
        issues.append(f"subject exceeds {MAX_LEN} chars ({len(subject)})")
    m = re.match(r"^(\w+)(\([^)]*\))?(!?):\s*(.+)$", subject)
    if not m:
        issues.append("subject must match: type(scope)?: description")
    else:
        t, scope, bang, desc = m.groups()
        if t not in TYPES:
            issues.append(f"unknown type '{t}'")
        if desc and desc[0].isupper():
            issues.append("description should not start with a capital letter")
        if desc and desc.endswith("."):
            issues.append("description should not end with a period")
    return issues

def main():
    msg = sys.stdin.read() if not sys.stdin.isatty() else " ".join(sys.argv[1:])
    if not msg.strip():
        print("commitlint-tr: no message", file=sys.stderr)
        return 2
    issues = lint(msg.strip())
    if issues:
        for i in issues: print(f"\u2717 {i}", file=sys.stderr)
        return 1
    print("\u2713 OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())

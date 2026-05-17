# Mindmap-Driven Test Case Generation using Copilot

> A team-wide process established to use XMind mindmaps as living functional
> knowledge documents — and generate structured test cases from them automatically
> using AI Copilot.

---

## The problem it solves

Traditional test case creation in QA teams suffers from two persistent issues:

**Knowledge is siloed** — functional understanding of a product lives in people's
heads, old documents, or scattered wikis. When someone leaves or a sprint moves fast,
that knowledge is lost or ignored.

**Test case writing is slow and inconsistent** — different QA engineers write test
cases differently. Coverage is uneven. Style varies. Review cycles are long.

This process solves both — by making the mindmap the single source of functional
truth, and using Copilot to generate consistent, structured test cases from it.

---

## How it works


```
XMind Mindmap (functional knowledge)
        │
        ▼
xmindparser (extract structured content)
        │
        ▼
Parsed mindmap content (text / JSON)
        │
        ▼
Copilot (AI-assisted test case generation)
        │
        ├── Gherkin format (BDD-style)
        └── Jira-style format (step + expected result)
        │
        ▼
Test cases ready for review + upload
```



---

## The mindmap knowledge repository

At the core of this process is a structured XMind mindmap repository — one mindmap
per product module — built and maintained by the QA team.

Each mindmap captures:
- **Functional flows** — how the feature is supposed to work end to end
- **Business rules** — conditions, constraints, validations
- **Edge cases** — known boundary conditions and exception paths
- **Dependencies** — related modules and integration points

This turns the mindmap into a living functional document — not just a diagram,
but a machine-readable knowledge base that improves with every sprint.

---

## Parsing with xmindparser

XMind files are parsed using `xmindparser` — a Python library that extracts the
mindmap's hierarchical structure into a readable format that can be fed directly
to Copilot as context.

This was a key technical decision: rather than manually copying mindmap content
into prompts, the parser extracts it programmatically — making the process
repeatable, consistent, and scalable across all modules.

---

## Test case generation with Copilot

With the parsed mindmap content as context, Copilot generates test cases in two
formats depending on the team's needs:

### Gherkin format (BDD-style)

```gherkin
Feature: [Module name from mindmap]

  Scenario: [Flow from mindmap]
    Given [precondition]
    When  [action]
    Then  [expected result]
```


### Jira-style format
| Field | Content |
|---|---|
| Test case title | Derived from mindmap node |
| Steps | Numbered action steps |
| Expected result | Per-step expected outcome |
| Priority | Based on flow criticality |

---

## Team process established

This wasn't a personal tool — it was rolled out as a standard QA process for the team:

1. **Mindmap first** — before writing any test case, the relevant module mindmap is
   reviewed and updated to reflect the current user story
2. **Parse and generate** — xmindparser extracts the content, Copilot generates
   the test cases
3. **QA review** — engineer reviews generated test cases for accuracy and coverage
4. **Upload to Jira** — approved test cases are uploaded to the test execution
5. **Mindmap update** — any new knowledge from testing is fed back into the mindmap

This creates a feedback loop where the knowledge base and test coverage both improve
continuously.

---

## Key outcomes

- ✅ Consistent test case format across the team
- ✅ Faster test case creation — from hours to minutes per module
- ✅ Functional knowledge captured and reusable across sprints
- ✅ Dual format output — Gherkin for BDD workflows, Jira-style for execution tracking
- ✅ Reduced dependency on individual knowledge — anyone on the team can generate
  test cases for any module using the mindmap

---

## Tech stack

| Layer | Tool |
|---|---|
| Knowledge capture | XMind (mindmap) |
| Mindmap parsing | xmindparser (Python) |
| Test case generation | GitHub Copilot |
| Output formats | Gherkin · Jira-style |
| Test management | Jira |

---

## Status

- ✅ Process established and adopted by the team
- ✅ Mindmap repository built for multiple product modules
- 🔄 Exploring integration with agentic pipeline for fully automated generation
- 🔲 Evaluating SpecKit for AI-assisted specification alongside this process

---

## Related project

The mindmap knowledge repository built here is a core input into the
[Agentic In-Sprint QA Pipeline](../01_agentic-insprint-qa-pipeline/README.md) —
where the agent reads, cross-references, and updates the same mindmaps autonomously.

---

## Author

**Jagadeesh Thangavel** — QA Engineer | AI Automation Architect | PLM Testing Specialist
[LinkedIn](https://www.linkedin.com/in/jagadeesh-thangavel/)

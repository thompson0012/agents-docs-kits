---
name: using-documents
description: Use when a document-oriented request could plausibly fit more than one file-format skill and the agent must choose the narrowest child first.
---

# Using Documents

Use this router when the request is about creating, editing, converting, extracting, or quality-checking a document artifact and the right format skill is not obvious yet.

Do not perform the full child workflow here. Select the narrowest correct child, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no document child fits.
- Prefer the requested or implied output artifact over the source file when the two differ.
- Use `references/children.json` as the source of truth for child boundaries, install hints, and selection order.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong child.
- Do not route to multiple sibling document children in parallel for one request.

## Decision Order

| Document Need | Route | Examples |
|---|---|---|
| Spreadsheet or workbook work | `load_skill("using-documents/xlsx")` | Excel models, formula debugging, workbook automation, data tables, pivot workflows |
| Slide deck or presentation work | `load_skill("using-documents/pptx")` | Existing presentations, slide generation, deck templates, visual QA for slides |
| Editable word-processing document work | `load_skill("using-documents/docx")` | Word documents, tracked changes, contract edits, PDF-to-Word conversion, legacy `.doc` conversion |
| Fixed-layout PDF work | `load_skill("using-documents/pdf")` | Fill PDF forms, merge/split/encrypt PDFs, OCR scans, text/table extraction, render pages |

When a request starts from a PDF but the real deliverable is an editable Word document, route to `using-documents/docx` and let the PDF child remain a recommended companion rather than the primary target.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-documents/xlsx.`
- `Route to using-documents/pptx.`
- `Route to using-documents/docx.`
- `Route to using-documents/pdf.`
- `Install <child-path>, then route to <child-path>.`
- `No using-documents child fits; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Family Workflow Boundary

1. The router chooses the narrowest document-format child.
2. The selected child skill owns the implementation workflow and any format-specific tools.
3. Cross-child recommendations are allowed when the source format differs from the real output artifact, but the router still picks exactly one primary child.

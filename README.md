# HFE Notes

Human factors engineering course notes organized as a bilingual MkDocs site and deployed to GitHub Pages.

## Structure

- Top-level knowledge sources: `ENP111` and `ENP112`
- Source materials are read from sibling workspace folders:
  - `d:\Projects\xixi-知识点\ENP 111 Use-related Risks`
  - `d:\Projects\xixi-知识点\ENP112 Engineering Forensics`
- Legacy `HFE_*` paths are kept as compatibility entry pages and redirect to the new locations

## Local Build

```powershell
python -m pip install -r requirements.txt
python scripts/build_hfe_notes.py
python hooks/generate_dropdown.py
mkdocs build
```

## Repository

- GitHub Pages target: `https://jeffliulab.github.io/hfe-notes/`
- Source materials are read from the sibling workspace directory `d:\Projects\xixi-知识点`

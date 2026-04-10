# HFE Notes

Human factors engineering course notes organized as a bilingual MkDocs site and deployed to GitHub Pages.

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

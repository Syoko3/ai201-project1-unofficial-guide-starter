# Documents loader

Usage: run the loader from the `documents` folder to process the URLs listed in `.gitkeep`.

There are two modes:

- Manifest-only (no downloads):

```bash
python load_documents.py --manifest-only
```

This writes `downloaded/manifest.json` containing the list of URLs and suggested filenames, without fetching any remote content.

- Full download mode (default):

```bash
python load_documents.py
```

Notes:
- The script uses only Python standard library (`urllib.request`) so no extra packages required.
- `.gitkeep` is expected to contain one URL per line. Lines starting with `#` are ignored.

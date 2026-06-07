from pathlib import Path
import urllib.request
import urllib.parse
import json
import re
import time
import argparse

HERE = Path(__file__).parent
GITKEEP = HERE / '.gitkeep'
OUT_DIR = HERE / 'downloaded'
OUT_DIR.mkdir(exist_ok=True)

def sanitize_filename(s: str) -> str:
    s = re.sub(r"^https?://", "", s)
    s = re.sub(r"[^0-9A-Za-z._-]", "_", s)
    # collapse multiple underscores
    s = re.sub(r"_+", "_", s)
    return s.strip("_")

def choose_ext(url: str, content_type: str|None) -> str:
    if content_type:
        ct = content_type.lower()
        if 'html' in ct or 'htm' in ct:
            return '.html'
        if 'json' in ct:
            return '.json'
        if 'plain' in ct or 'text' in ct:
            return '.txt'
    # fallback: try extension from path
    path = urllib.parse.urlparse(url).path
    if '.' in Path(path).name:
        return Path(path).suffix
    return '.dat'

def download_url(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={
        'User-Agent': 'DocumentLoader/1.0 (+https://example.com)'
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            ctype = resp.getheader('Content-Type')
            ext = choose_ext(url, ctype)
            name = sanitize_filename(url)
            filename = OUT_DIR / (name + ext)
            with open(filename, 'wb') as f:
                f.write(data)
            return {
                'url': url,
                'ok': True,
                'path': str(filename.relative_to(HERE)),
                'content_type': ctype,
                'bytes': len(data),
            }
    except Exception as e:
        return {'url': url, 'ok': False, 'error': str(e)}

def load_from_gitkeep(path: Path) -> list:
    if not path.exists():
        raise FileNotFoundError(path)
    lines = [l.strip() for l in path.read_text(encoding='utf-8').splitlines()]
    # filter out empties and comments
    items = [l for l in lines if l and not l.startswith('#')]
    return items


def manifest_only(items: list) -> list:
    results = []
    for i, item in enumerate(items, start=1):
        name = sanitize_filename(item)
        parsed = urllib.parse.urlparse(item)
        path = Path(parsed.path).name
        ext = Path(path).suffix or '.dat'
        results.append({
            'url': item,
            'ok': None,
            'suggested_path': str((OUT_DIR / (name + ext)).relative_to(HERE)),
            'content_type': None,
        })
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest-only', '-m', action='store_true',
                        help='Do not download URLs; only produce manifest with URLs and suggested filenames')
    args = parser.parse_args()

    print('Loading documents listed in .gitkeep...')
    items = load_from_gitkeep(GITKEEP)

    if args.manifest_only:
        results = manifest_only(items)
        manifest = OUT_DIR / 'manifest.json'
        manifest.write_text(json.dumps(results, indent=2), encoding='utf-8')
        print(f'Manifest (no-download) saved to {manifest.relative_to(HERE)}')
        print(f'{len(results)} entries written.')
        return

    results = []
    for i, item in enumerate(items, start=1):
        print(f'[{i}/{len(items)}] Downloading: {item}')
        res = download_url(item)
        results.append(res)
        time.sleep(0.5)

    manifest = OUT_DIR / 'manifest.json'
    manifest.write_text(json.dumps(results, indent=2), encoding='utf-8')
    ok = sum(1 for r in results if r.get('ok'))
    fail = len(results) - ok
    print(f'Download complete: {ok} succeeded, {fail} failed.')
    print(f'Manifest saved to {manifest.relative_to(HERE)}')

if __name__ == '__main__':
    main()

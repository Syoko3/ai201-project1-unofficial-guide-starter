from __future__ import annotations

import argparse
import json
import re
import unicodedata
from html import unescape
from pathlib import Path

HERE = Path(__file__).parent
DATA_DIR = HERE / 'documents' / 'data'
CLEAN_DIR = DATA_DIR / 'cleaned'
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

BOILERPLATE_PATTERNS = [
    r'cookie', r'privacy policy', r'terms of use', r'terms and conditions',
    r'advertisement', r'all rights reserved', r'powered by', r'subscribe',
    r'follow us', r'share', r'read more', r'view more', r'search',
    r'login', r'sign in', r'sign up', r'menu', r'faq', r'help center',
    r'download app', r'app store', r'google play', r'comments?',
    r'related articles?', r'recent posts?', r'site map', r'contact us',
    r'cookie settings', r'javascript', r'function\(', r'window\.',
    r'copyright', r'powered by', r'\bads\b', r'\badvert\b', r'\bnewsletter\b',
    r'\bors\b', r'\bthis page\b', r'\bpage not found\b', r'\b404\b',
]

NOISE_PATTERNS = [
    r'^comments section$', r'^promoted$', r'^order now$', r'^clickable image$',
    r'^collapse video player$', r'^avatar$', r'^u/[a-z0-9_-]+$',
    r'^sort$', r'^profile photo(?: for)?', r'^upvoted by',
    r'author has .* answers? and .* answer views',
    r'\b(?:reddit|subreddit|comment count|upvote|downvote|promo|sponsored|author has|answer views)\b',
    r'^\d+\s*·\s*\d+$', r'^\d+$', r'^[·•]+$',
    r'^\d+[ym]? ago$', r'^hello uc merced students,$',
    r'^associate professor of computer science',
]

# Common ad / promoted patterns to drop entire blocks matching these
AD_PATTERNS = [
    r'\bpromoted\b', r'\bsponsored\b', r'\bshop now\b', r'\border now\b', r'\bsign up\b',
    r'\bthumbnail image\b', r'clickable image', r'\bthumbnail\b', r'\bsubscribe now\b',
    r'\badvertisement\b', r'\bshop\b', r'\border\b', r'\bcta\b', r'\bpromoted by\b',
    # short domain-like tokens often appear in ad blocks (e.g. "freestyle.abbott")
    r'\b[a-z0-9-]+\.(com|org|net|io|co|us|edu|biz|info)\b',
]


CATEGORY_KEYWORDS = {
    'short': ['ratemycourses', 'ratemyprofessors', 'rate my courses', 'rate my professors'],
    'medium': ['reddit', 'quora'],
    'long': ['catalog.ucmerced', 'engineering.ucmerced', 'engr-advising', 'course descriptions', 'faculty', 'advising'],
}

CHUNK_PARAMS = {
    'short': (100, 0),
    'medium': (250, 20),
    'long': (400, 50),
}


def normalize_paragraph(text: str) -> str:
    text = unescape(text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = text.replace('\r', ' ').replace('\xa0', ' ')
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\s*(&amp;|&lt;|&gt;|&quot;|&#39;)\s*', lambda m: {'&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'"}[m.group(1).lower()], text)
    text = text.strip()
    return text


def is_boilerplate_paragraph(text: str) -> bool:
    if not text or len(text) < 20:
        return False
    lowered = re.sub(r'[ \t\n]+', ' ', text).strip().lower()
    if re.fullmatch(r'[\W_]+', lowered):
        return True
    for pattern in BOILERPLATE_PATTERNS:
        if re.search(pattern, lowered):
            return True
    return False


def is_noise_paragraph(text: str) -> bool:
    if not text:
        return True
    lowered = text.strip().lower()
    if any(re.search(pattern, lowered) for pattern in NOISE_PATTERNS):
        return True
    if len(lowered) < 5 and not re.search(r'[a-z0-9]', lowered):
        return True
    return False


def load_source_files() -> list[Path]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted([p for p in DATA_DIR.glob('*.txt') if p.is_file()])
    return files


def normalize_text(text: str) -> str:
    blocks = [b.strip() for b in re.split(r'\n\s*\n+', text) if b.strip()]
    def is_ad_block(block: str) -> bool:
        b = block.lower()
        # If block contains any ad indicator, drop it
        for pat in AD_PATTERNS:
            if re.search(pat, b):
                return True
        # lines like "u/Name avatar" followed by short CTA lines are often ads
        lines = [l.strip().lower() for l in block.splitlines() if l.strip()]
        if len(lines) <= 6 and any(l in ('avatar', 'promoted', 'sponsored') for l in lines):
            return True
        # blocks that consist primarily of short lines with punctuation like "Sign Up" or a domain
        short_lines = sum(1 for l in lines if len(l) < 40)
        if lines and short_lines == len(lines) and len(lines) <= 6 and any(re.search(r"sign up|order now|shop now|promoted|thumbnail", l) for l in lines):
            return True
        return False
    paragraphs = []
    seen = set()
    # remove ad/promoted blocks early
    blocks = [b for b in blocks if not is_ad_block(b)]

    for block in blocks:
        cleaned = normalize_paragraph(block)
        if not cleaned or is_noise_paragraph(cleaned) or is_boilerplate_paragraph(cleaned):
            continue
        if cleaned in seen:
            continue
        seen.add(cleaned)
        paragraphs.append(cleaned)
    return '\n\n'.join(paragraphs)


def classify_source(path: Path) -> str:
    name = path.stem.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in name for keyword in keywords):
            return category
    return 'medium'


def get_chunk_params(category: str) -> tuple[int, int]:
    return CHUNK_PARAMS.get(category, CHUNK_PARAMS['medium'])


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    chunks: list[str] = []
    current = ''

    def add_chunk(chunk: str) -> None:
        chunk = chunk.strip()
        if chunk:
            chunks.append(chunk)

    for paragraph in paragraphs:
        if not current:
            current = paragraph
            continue
        if len(current) + 2 + len(paragraph) <= chunk_size:
            current = f'{current}\n\n{paragraph}'
            continue
        add_chunk(current)
        if overlap > 0:
            tail = current[-overlap:]
            if ' ' in tail:
                tail = tail[tail.find(' '):].strip()
            current = f'{tail}\n\n{paragraph}' if tail else paragraph
        else:
            current = paragraph
        while len(current) > chunk_size:
            add_chunk(current[:chunk_size].strip())
            current = current[chunk_size-overlap:].strip() if overlap > 0 else current[chunk_size:].strip()
    add_chunk(current)
    return chunks


def clean_documents() -> list[dict]:
    source_files = load_source_files()
    results = []
    for path in source_files:
        raw = path.read_text(encoding='utf-8', errors='replace')
        cleaned = normalize_text(raw)
        clean_path = CLEAN_DIR / path.name
        clean_path.write_text(cleaned, encoding='utf-8')
        results.append({
            'source_path': str(path.relative_to(HERE)),
            'clean_path': str(clean_path.relative_to(HERE)),
            'chars': len(cleaned),
        })
    return results


def chunk_documents() -> list[dict]:
    cleaned_files = sorted(CLEAN_DIR.glob('*.txt'))
    chunks = []
    for path in cleaned_files:
        text = path.read_text(encoding='utf-8', errors='replace').strip()
        if not text:
            continue
        category = classify_source(path)
        chunk_size, overlap = get_chunk_params(category)
        for index, chunk in enumerate(chunk_text(text, chunk_size, overlap), start=1):
            chunks.append({
                'source_path': str(path.relative_to(HERE)),
                'category': category,
                'chunk_index': index,
                'chunk_size': chunk_size,
                'overlap': overlap,
                'chunk_text': chunk,
            })
    return chunks


def save_chunks(chunks: list[dict]) -> Path:
    chunks_path = DATA_DIR / 'chunks.json'
    chunks_path.write_text(json.dumps(chunks, indent=2, ensure_ascii=False), encoding='utf-8')
    return chunks_path


def main() -> None:
    parser = argparse.ArgumentParser(description='Load, clean, and chunk local text documents from data/')
    parser.add_argument('--clean-only', action='store_true', help='Clean raw text files and write normalized text to data/cleaned/')
    parser.add_argument('--chunk-only', action='store_true', help='Chunk cleaned text files from data/cleaned/ into data/chunks.json')
    parser.add_argument('--all', action='store_true', help='Run both cleaning and chunking end to end')
    args = parser.parse_args()

    if not args.clean_only and not args.chunk_only and not args.all:
        args.all = True

    if args.clean_only or args.all:
        print(f'Loading raw .txt files from {DATA_DIR}...')
        cleaned = clean_documents()
        print(f'Cleaned {len(cleaned)} documents. Clean versions saved to {CLEAN_DIR}.')

    if args.chunk_only or args.all:
        print(f'Chunking cleaned documents from {CLEAN_DIR}...')
        chunks = chunk_documents()
        path = save_chunks(chunks)
        print(f'Saved {len(chunks)} chunks to {path}.')


if __name__ == '__main__':
    main()

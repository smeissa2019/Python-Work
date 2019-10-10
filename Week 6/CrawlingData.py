from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
text = strip_headers(load_etext(60457)).strip()
print(text)


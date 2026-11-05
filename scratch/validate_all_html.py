import glob
import html.parser

class SimpleHTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def error(self, message):
        self.errors.append(message)

files = glob.glob(r'd:\Sattvic Books\*.html')
total_errors = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    validator = SimpleHTMLValidator()
    try:
        validator.feed(content)
        if validator.errors:
            print(f"Errors in {fpath}: {validator.errors}")
            total_errors += len(validator.errors)
        else:
            print(f"OK: {fpath}")
    except Exception as e:
        print(f"Exception in {fpath}: {e}")
        total_errors += 1

print(f"Validation complete. Total errors: {total_errors}")


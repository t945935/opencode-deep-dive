.PHONY: manuscript check

manuscript:
	pandoc book/manuscript.md --metadata-file=book/metadata.yaml --css=book/style.css --toc --standalone -o OpenCode-深入解析.epub

check:
	python3 scripts/check_book.py
	unzip -t OpenCode-深入解析.epub >/dev/null

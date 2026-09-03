.PHONY: manuscript check

manuscript:
	python3 scripts/build_manuscript.py
	pandoc book/manuscript.md --metadata-file=book/metadata.yaml --css=book/style.css --epub-cover-image=book/cover.svg --toc --standalone -o OpenCode-深入解析.epub

check:
	python3 scripts/check_book.py
	unzip -t OpenCode-深入解析.epub >/dev/null

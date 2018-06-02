.PHONY: install get-all-boards get-board-by-id

install:
	@pip install -r requirements.txt

get-all-boards:
	@python crawler.py

get-board-by-id:
	@python crawler.py -i $(ARGS)

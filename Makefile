.PHONY: install get-all-boards get-board-by-id

install:
	@pip install -r requirements.txt

authorize:
	@python authorize.py

get-all-boards:
	@python crawler.py

get-board-by-id:
	@python crawler.py -i $(ARGS)

generate-burndown-chart:
	@python burndown-generator.py -l $(ARGS)

generate-burnup-chart:
	@python burnup-generator.py -l $(ARGS)

generate-cfd-chart:
	@python cfd-generator.py -i $(IDS) -l $(LABELS)

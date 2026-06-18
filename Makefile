icg-s-step1:
	poetry run python -m flows.image_content_generator.pipeline.main short step1

icg-s-step2:
	poetry run python -m flows.image_content_generator.pipeline.main short step2

icg-s-step3:
	poetry run python -m flows.image_content_generator.pipeline.main short step3

icg-s-step4:
	poetry run python -m flows.image_content_generator.pipeline.main short step4

icg-s-step5:
	poetry run python -m flows.image_content_generator.pipeline.main short step5

icg-s-step6:
	poetry run python -m flows.image_content_generator.pipeline.main short step6

icg-s-step7:
	poetry run python -m flows.image_content_generator.pipeline.main short step7

icg-s-all:
	poetry run python -m flows.image_content_generator.pipeline.main short all

icg-s-fixed:
	poetry run python -m flows.image_content_generator.pipeline.main short fixed


icg-l-step1:
	poetry run python -m flows.image_content_generator.pipeline.main long step1

icg-l-step2:
	poetry run python -m flows.image_content_generator.pipeline.main long step2

icg-l-step3:
	poetry run python -m flows.image_content_generator.pipeline.main long step3

icg-l-step4:
	poetry run python -m flows.image_content_generator.pipeline.main long step4

icg-l-step5:
	poetry run python -m flows.image_content_generator.pipeline.main long step5

icg-l-step6:
	poetry run python -m flows.image_content_generator.pipeline.main long step6

icg-l-step7:
	poetry run python -m flows.image_content_generator.pipeline.main long step7

icg-l-all:
	poetry run python -m flows.image_content_generator.pipeline.main long all

icg-l-fixed:
	poetry run python -m flows.image_content_generator.pipeline.main long fixed


icg-import-images:
	poetry run python import_images.py

icg-extract-scripts:
	poetry run python extract_scripts.py

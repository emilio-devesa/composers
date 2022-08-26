build: main.py
	@echo "Building..."
	pyinstaller --clean --onefile --windowed --osx-bundle-identifier com.emiliodevesa.composers --name composers main.py

clean:
	@echo "Cleaning"
	rm -rf ./build
	rm -rf __pycache__
	rm -rf ./dist
	rm -rf .temp.png composers.spec .DS_Store




install-app:
	python3 setup_app.py py2app -A
	sudo mv ./dist/Hue\ Controller.app /Applications/Hue_Controller.app
	
clean :
	rm -rf build/
	rm -rf dist/

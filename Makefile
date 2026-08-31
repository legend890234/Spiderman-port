all:
	@echo "Building Spider-Man 3D Native Engine Target..."
	@python3 build_pipeline.py
	@g++ main.cpp -o spiderman_engine -lGLESv2
	@echo "Engine compilation complete! Executable 'spiderman_engine' created."
clean:
	@rm -rf build_cache spiderman_engine

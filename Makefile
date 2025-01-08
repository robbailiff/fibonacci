SHELL := /bin/bash

build:
	@echo "Running maturin in dev mode"
	cd rust_fibonacci && poetry run maturin develop

build-release:
	@echo "Running maturin in release mode"
	cd rust_fibonacci && poetry run maturin develop --release

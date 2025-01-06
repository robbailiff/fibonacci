#!/bin/bash

cd rust_fibonacci/

if [[ $1 == "--release" ]]; then
    echo "Running maturin in release mode"
    poetry run maturin develop --release
else
    echo "Running maturin in dev mode"
    poetry run maturin develop
fi

cd ..
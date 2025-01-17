# Fibonacci Benchmark: Python vs Rust

This project benchmarks the performance of calculating Fibonacci numbers using Python and Rust. It demonstrates how to integrate a Rust library into a Python project using `PyO3` and  `maturin` and compares their execution speeds.

The code features:

- **Python Implementation**: A straightforward iterative, and recursive implementation in Python.
- **Rust Implementation**: A high-performance iterative, and recursive implementation in Rust, exposed to Python as a module.
- **Benchmarking**: A script to measure and compare the execution times of the Python and Rust implementations.


## Prerequisites

- **Python**: Version 3.8 or newer.
- **Rust**: Installed using [rustup](https://rustup.rs/).
- **PyO3**: For interfacing Rust with Python. 
- **Maturin**: For building the Rust library as a Python module.

### *Optional

- **Poetry**: For managing Python dependencies.
- **Make**: For automating the compilation and build process.


## Development

1. Create a new folder and initialise python python using `poetry init`
2. Make sure to add `maturin` to the project, either during creation or with `poetry add maturin`
3. Create a new subfolder for the rust code and inside create a new cargo project with `poetry run maturin new`
4. Be sure to include `[lib] crate-type = ["cdylib"]` in `Cargo.toml` to ensure that Cargo produces a C-compatible library that can be loaded by Python. By default, a `.rlib` file is created, which is a static file compiled for use in other Rust projects, and is not compatible with Python.
5. Write rust code and then use PyO3 crate to expose functions and define modules which can be imported into Python
6. Compile the rust code with the command `poetry run maturin build`
7. Import the rust module into Python by using the name of the library (not the filepath). This is because maturin creates single package based on the `name` in `Cargo.toml`, rather than a package structure. An `__init__.py` file could be added to any parent folders to achieve this if desired.
8. Run the main Python file with the Rust module imported with `poetry run python main.py`


## Resources

- **Rust and Python Integration**: [PyO3](https://pyo3.rs/).
- **Build Python Packages from Rust**: [Maturin](https://github.com/PyO3/maturin).
- **Dependency Management**: [Poetry](https://python-poetry.org/).

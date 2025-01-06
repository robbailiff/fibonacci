# Fibonacci Benchmark: Python vs Rust

This project benchmarks the performance of calculating Fibonacci numbers using Python and Rust. It demonstrates how to integrate a Rust library into a Python project using `maturin` and compares their execution speeds.

---

## Features

- **Python Implementation**: A straightforward recursive implementation in Python.
- **Rust Implementation**: A high-performance recursive implementation in Rust, exposed to Python as a module.
- **Benchmarking**: A script to measure and compare the execution times of the Python and Rust implementations.

---

## Prerequisites

- **Python**: Version 3.8 or newer.
- **Rust**: Installed using [rustup](https://rustup.rs/).
- **PyO3**: For interfacing Rust with Python. 
- **Maturin**: For building the Rust library as a Python module.

### Optional

- **Poetry**: For managing Python dependencies.

---

## Resources

- **Rust and Python Integration**: Powered by [PyO3](https://pyo3.rs/).
- **Dependency Management**: Managed with [Poetry](https://python-poetry.org/) and [Maturin](https://github.com/PyO3/maturin).

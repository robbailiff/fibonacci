use pyo3::prelude::*;

#[pyfunction]
fn rust_fibonacci_recursive(n: u64) -> u64 {
    match n {
        n if (n <= 1) => n,
        _ => rust_fibonacci_recursive(n - 1) + rust_fibonacci_recursive(n - 2)
    }
}

#[pyfunction]
fn rust_fibonacci_iterative(n: u64) -> u64 {
    let mut n1 = 0;
    let mut n2 = 1;
    for _ in 0..n {
        let temp = n1;
        n1 = n2;
        n2 = temp + n2;
    }
    return n1
}

#[pymodule]
fn rust_fibonacci<'py>(_py: Python<'py>, m: &Bound<'py, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_fibonacci_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(rust_fibonacci_iterative, m)?)?;
    Ok(())
}

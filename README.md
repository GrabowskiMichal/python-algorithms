# Python Algorithms Repository

This repository contains a collection of commonly used algorithms implemented in Python. The goal is to demonstrate and analyze the working of fundamental algorithms that are widely used in computer science and programming.

## Algorithms Included

### 1. **Quick Sort**
Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element and partitioning the array into two sub-arrays, where one contains elements less than the pivot and the other contains elements greater than the pivot. The sub-arrays are then sorted recursively.

- **Time Complexity:** O(n log(n)) on average, O(n²) in the worst case.
- **Space Complexity:** O(log(n))

### 2. **Selection Sort**
Selection Sort is an in-place comparison-based sorting algorithm. It works by repeatedly finding the smallest (or largest) element from the unsorted part of the list and swapping it with the first unsorted element.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### 3. **Merge Sort**
Merge Sort is a divide-and-conquer algorithm. It works by recursively dividing the array into two halves, sorting each half, and then merging the sorted halves back together.

- **Time Complexity:** O(n log(n))
- **Space Complexity:** O(n)

### 4. **Insertion Sort**
Insertion Sort is an in-place, comparison-based sorting algorithm. It builds the sorted array one item at a time, by taking each element from the unsorted portion and placing it in the correct position in the sorted portion.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### 5. **Bubble Sort**
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until no more swaps are needed.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### 6. **Sieve of Eratosthenes**
The Sieve of Eratosthenes is an efficient algorithm for finding all primes up to a given limit. It works by iteratively marking the multiples of each prime number starting from 2.

- **Time Complexity:** O(n log(log n))
- **Space Complexity:** O(n)

## Getting Started

To get started with the algorithms, clone the repository and run the Python scripts for each algorithm.

### Clone the Repository

```bash
  git clone https://github.com/yourusername/python-algorithms.git
  cd python-algorithms
```

Running an Algorithm

To run a specific algorithm, simply execute the corresponding Python file. For example:

```bash
  python quick_sort.py  
```

Requirements

- Python 3.12

No external libraries are required for these algorithms as they are implemented using standard Python features.
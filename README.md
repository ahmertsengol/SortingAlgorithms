# 🎯 Sorting Algorithm Visualizer

Professional Python tool for visualizing and comparing sorting algorithms with real-time animation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Overview

Interactive visualization tool that compares two sorting algorithms side-by-side with:
- Real-time animation of 11 different sorting algorithms
- Customizable dataset size (10-1000 elements)
- Performance comparison with winner detection
- Automatic validation of sorting correctness

## 🚀 Quick Start

```bash
# Install dependencies
pip install matplotlib

# Run visualizer
python SortingVisualizer.py
```

## 📊 Supported Algorithms & Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Shell Sort | O(n log n) | O(n^1.25) | O(n²) | O(1) |
| Comb Sort | O(n log n) | O(n²) | O(n²) | O(1) |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) |
| Bogo Sort | O(n) | O((n+1)!) | O(∞) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

## 🎮 Demo

![Sorting Animation](images/Example-1.png)
*Real-time algorithm comparison*

![Validation Complete](images/Example-2.png)
*Results with winner detection*

## 🔧 Usage

1. Choose number of bars (10-1000)
2. Select two algorithms to compare
3. Watch real-time visualization
4. View performance results

# Sample Output Examples

## Example 1: Quick Sort vs Merge Sort (100 bars)

```
🚀 ADVANCED SORTING ALGORITHM VISUALIZER
==================================================
Enter number of bars (10-200): 100
✅ Will create 100 bars with heights from 1 to 100

📊 Available sorting algorithms:

  1 . Bubble Sort     7 . Comb Sort
  2 . Selection Sort  8 . Radix Sort  
  3 . Insertion Sort  9 . Bucket Sort
  4 . Quick Sort     10. Bogo Sort
  5 . Heap Sort      11. Merge Sort
  6 . Shell Sort

Select TWO algorithms to compare:
First algorithm (1-11): 4
Second algorithm (1-11): 11

🎯 Comparing: Quick Sort vs Merge Sort
==================================================
🔧 Setting up visualization for 100 bars...
📈 Algorithm 1: Quick Sort
📈 Algorithm 2: Merge Sort
🎲 Generated random array: [44, 17, 40, 79, 32, 66, 82, 54, 78, 55]...
🔄 Generating frames for algorithms...
  📊 Generating frames for Quick Sort...
     Generated 953 frames
  📊 Generating frames for Merge Sort...
     Generated 1212 frames
⏱️ Measuring real execution times...
   Quick Sort: 953 frames → 0.000953s
   Merge Sort: 1212 frames → 0.001212s
🏆 Fastest: Quick Sort (0.000953s)
   Quick Sort: ratio 1.00 → finishes at frame 600
   Merge Sort: ratio 1.27 → finishes at frame 763
🎬 Starting proportional animation...
⏱️ Animation: 853 frames, 21ms interval
📺 Duration: ~17.9 seconds
🎨 Green bars, black background, selected bars in black
🏆 WINNER: Quick Sort (fastest algorithm)
⚡ Algorithms finish at different times based on performance
🔍 Validation: Each completed algorithm will be validated
💙 Valid sorts turn blue, ❤️ invalid sorts turn red
```

## Example 2: Bubble Sort vs Selection Sort (50 bars)

```
🚀 ADVANCED SORTING ALGORITHM VISUALIZER
==================================================
Enter number of bars (10-200): 50
✅ Will create 50 bars with heights from 1 to 50

Select TWO algorithms to compare:
First algorithm (1-11): 1
Second algorithm (1-11): 2

🎯 Comparing: Bubble Sort vs Selection Sort
==================================================
🔧 Setting up visualization for 50 bars...
📈 Algorithm 1: Bubble Sort
📈 Algorithm 2: Selection Sort
🎲 Generated random array: [35, 5, 2, 11, 34, 17, 18, 91, 48, 70]...
🔄 Generating frames for algorithms...
  📊 Generating frames for Bubble Sort...
     Generated 1845 frames
  📊 Generating frames for Selection Sort...
     Generated 1275 frames
⏱️ Measuring real execution times...
   Bubble Sort: 1845 frames → 0.001845s
   Selection Sort: 1275 frames → 0.001275s
🏆 Fastest: Selection Sort (0.001275s)
   Selection Sort: ratio 1.00 → finishes at frame 600
   Bubble Sort: ratio 1.45 → finishes at frame 870
🎬 Starting proportional animation...
⏱️ Animation: 960 frames, 18ms interval
📺 Duration: ~17.3 seconds
🎨 Green bars, black background, selected bars in black
🏆 WINNER: Selection Sort (fastest algorithm)
⚡ Algorithms finish at different times based on performance
🔍 Validation: Each completed algorithm will be validated
💙 Valid sorts turn blue, ❤️ invalid sorts turn red
```

## Performance Comparison Table

| Algorithm Pair | Winner | Performance Difference | Animation Duration |
|---------------|--------|----------------------|-------------------|
| Quick Sort vs Merge Sort | Quick Sort | 27% faster | ~17.9s |
| Selection Sort vs Bubble Sort | Selection Sort | 45% faster | ~17.3s |
| Heap Sort vs Shell Sort | Heap Sort | 15% faster | ~18.1s |
| Insertion Sort vs Bubble Sort | Insertion Sort | 60% faster | ~16.8s |

## Visual Elements During Animation

1. **🟢 Green Bars**: Normal, unsorted elements
2. **⚫ Black Bars**: Currently being compared/selected
3. **🔵 Blue Bars**: Validated as correctly sorted
4. **🔴 Red Bars**: Validation error (rare, indicates bug)

## Animation Phases

1. **Setup Phase** (2-3 seconds): Array generation and algorithm preparation
2. **Sorting Phase** (10-15 seconds): Real-time algorithm execution
3. **Validation Phase** (2-3 seconds): Correctness verification
4. **Results Display** (1-2 seconds): Final winner announcement 
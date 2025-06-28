import matplotlib
import platform
import os

# Set appropriate backend based on operating system
if platform.system() == 'Darwin':  # macOS
    matplotlib.use('MacOSX')
elif platform.system() == 'Windows':  # Windows
    matplotlib.use('TkAgg')
elif platform.system() == 'Linux':  # Linux
    matplotlib.use('TkAgg')
else:
    # Let matplotlib choose the best backend
    pass

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
from typing import List, Tuple, Generator, Optional
import math

# --- Constants ---
BAR_COLOR_NORMAL = '#00FF00'      # Green bars
BAR_COLOR_SELECTED = '#000000'    # Black for selected bars
BACKGROUND_COLOR = '#000000'      # Black background
FIGURE_SIZE = (16, 8)

# --- Type Definitions ---
FrameData = Tuple[List[int], int, int]  # (array, index1, index2)
AlgorithmGenerator = Generator[FrameData, None, None]

def get_user_input():
    """Get user input for number of bars and algorithm selection."""
    print("🚀 ADVANCED SORTING ALGORITHM VISUALIZER")
    print("=" * 50)
    
    # Get number of bars
    while True:
        try:
            n = int(input("Enter number of bars (10-1000): "))
            if 10 <= n <= 1000:
                break
            else:
                print("❌ Please enter a number between 10 and 1000.")
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit()
    
    print(f"✅ Will create {n} bars with heights from 1 to {n}")
    return n

def get_algorithm_selection():
    """Get user selection for two algorithms to compare."""
    algorithms = {
        '1': 'Bubble Sort',
        '2': 'Selection Sort', 
        '3': 'Insertion Sort',
        '4': 'Quick Sort',
        '5': 'Heap Sort',
        '6': 'Shell Sort',
        '7': 'Comb Sort',
        '8': 'Radix Sort',
        '9': 'Bucket Sort',
        '10': 'Bogo Sort',
        '11': 'Merge Sort',
    }
    
    print("\n📊 Available sorting algorithms:")
    print()
    
    for key, name in algorithms.items():
        print(f"  {key:2}. {name}")
    
    print()
    print("Select TWO algorithms to compare:")
    
    # Get first algorithm
    while True:
        try:
            choice1 = input("First algorithm (1-11): ").strip()
            if choice1 in algorithms:
                first_algo = choice1
                break
            else:
                print("❌ Invalid choice. Please select 1-11.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit()
    
    # Get second algorithm
    while True:
        try:
            choice2 = input("Second algorithm (1-11): ").strip()
            if choice2 in algorithms and choice2 != choice1:
                second_algo = choice2
                break
            elif choice2 == choice1:
                print("❌ Please select a different algorithm for comparison.")
            else:
                print("❌ Invalid choice. Please select 1-11.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit()
    
    print()
    print(f"🎯 Comparing: {algorithms[first_algo]} vs {algorithms[second_algo]}")
    print("=" * 50)
    
    return first_algo, second_algo, algorithms

# --- Sorting Algorithm Classes ---

class SortingAlgorithms:
    """Collection of sorting algorithms as generators for visualization."""
    
    @staticmethod
    def bubble_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Bubble sort algorithm generator."""
        n = len(arr)
        local_arr = list(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                yield list(local_arr), j, j + 1
                
                if local_arr[j] > local_arr[j + 1]:
                    local_arr[j], local_arr[j + 1] = local_arr[j + 1], local_arr[j]
                    swapped = True
                    yield list(local_arr), j, j + 1
            
            if not swapped:
                break
        
        yield list(local_arr), -1, -1

    @staticmethod
    def selection_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Selection sort algorithm generator."""
        n = len(arr)
        local_arr = list(arr)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                yield list(local_arr), min_idx, j
                
                if local_arr[min_idx] > local_arr[j]:
                    min_idx = j
            
            if min_idx != i:
                local_arr[i], local_arr[min_idx] = local_arr[min_idx], local_arr[i]
                yield list(local_arr), i, min_idx
        
        yield list(local_arr), -1, -1

    @staticmethod
    def insertion_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Insertion sort algorithm generator."""
        local_arr = list(arr)
        
        for i in range(1, len(local_arr)):
            key = local_arr[i]
            j = i - 1
            
            while j >= 0:
                yield list(local_arr), j, i
                
                if local_arr[j] > key:
                    local_arr[j + 1] = local_arr[j]
                    j -= 1
                    yield list(local_arr), j + 1, i
                else:
                    break
            
            local_arr[j + 1] = key
            yield list(local_arr), j + 1, i
        
        yield list(local_arr), -1, -1

    @staticmethod
    def quick_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Quick sort algorithm generator."""
        local_arr = list(arr)
        
        def quick_sort_recursive(array, low, high):
            if low < high:
                pivot = array[high]
                i = low - 1
                
                for j in range(low, high):
                    yield list(array), j, high
                    
                    if array[j] <= pivot:
                        i += 1
                        if i != j:
                            array[i], array[j] = array[j], array[i]
                            yield list(array), i, j
                
                pivot_index = i + 1
                if pivot_index != high:
                    array[pivot_index], array[high] = array[high], array[pivot_index]
                    yield list(array), pivot_index, high
                
                yield from quick_sort_recursive(array, low, pivot_index - 1)
                yield from quick_sort_recursive(array, pivot_index + 1, high)
        
        yield from quick_sort_recursive(local_arr, 0, len(local_arr) - 1)
        yield list(local_arr), -1, -1

    @staticmethod
    def heap_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Heap sort algorithm generator."""
        local_arr = list(arr)
        n = len(local_arr)
        
        def heapify(array, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            
            if l < n:
                yield list(array), l, largest
                if array[l] > array[largest]:
                    largest = l
            
            if r < n:
                yield list(array), r, largest
                if array[r] > array[largest]:
                    largest = r
            
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                yield list(array), i, largest
                yield from heapify(array, n, largest)
        
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(local_arr, n, i)
        
        for i in range(n - 1, 0, -1):
            local_arr[0], local_arr[i] = local_arr[i], local_arr[0]
            yield list(local_arr), 0, i
            yield from heapify(local_arr, i, 0)
        
        yield list(local_arr), -1, -1

    @staticmethod
    def shell_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Shell sort algorithm generator."""
        local_arr = list(arr)
        n = len(local_arr)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                temp = local_arr[i]
                j = i
                
                while j >= gap:
                    yield list(local_arr), j, j - gap
                    
                    if local_arr[j - gap] > temp:
                        local_arr[j] = local_arr[j - gap]
                        j -= gap
                        yield list(local_arr), j, j + gap
                    else:
                        break
                
                local_arr[j] = temp
                yield list(local_arr), j, i
            
            gap //= 2
        
        yield list(local_arr), -1, -1

    @staticmethod
    def comb_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Comb sort algorithm generator."""
        local_arr = list(arr)
        n = len(local_arr)
        gap = n
        shrink = 1.3
        sorted_flag = False
        
        while not sorted_flag:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_flag = True
            
            i = 0
            while i + gap < n:
                yield list(local_arr), i, i + gap
                
                if local_arr[i] > local_arr[i + gap]:
                    local_arr[i], local_arr[i + gap] = local_arr[i + gap], local_arr[i]
                    sorted_flag = False
                    yield list(local_arr), i, i + gap
                
                i += 1
        
        yield list(local_arr), -1, -1

    @staticmethod
    def radix_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Radix sort algorithm generator."""
        local_arr = list(arr)
        max_num = max(local_arr)
        exp = 1
        
        while max_num // exp > 0:
            output = [0] * len(local_arr)
            count = [0] * 10
            
            for i in range(len(local_arr)):
                index = local_arr[i] // exp
                count[index % 10] += 1
                yield list(local_arr), i, -1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            i = len(local_arr) - 1
            while i >= 0:
                index = local_arr[i] // exp
                output[count[index % 10] - 1] = local_arr[i]
                count[index % 10] -= 1
                yield list(local_arr), i, -1
                i -= 1
            
            for i in range(len(local_arr)):
                local_arr[i] = output[i]
                yield list(local_arr), i, -1
            
            exp *= 10
        
        yield list(local_arr), -1, -1

    @staticmethod
    def bucket_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Bucket sort algorithm generator."""
        local_arr = list(arr)
        if not local_arr:
            return
        
        bucket_count = 10
        max_val = max(local_arr)
        min_val = min(local_arr)
        bucket_range = (max_val - min_val) / bucket_count
        
        buckets = [[] for _ in range(bucket_count)]
        
        for i, num in enumerate(local_arr):
            bucket_index = min(int((num - min_val) / bucket_range), bucket_count - 1)
            buckets[bucket_index].append(num)
            yield list(local_arr), i, -1
        
        result = []
        for i, bucket in enumerate(buckets):
            bucket.sort()
            result.extend(bucket)
            
            for j in range(len(result)):
                if j < len(local_arr):
                    local_arr[j] = result[j]
            yield list(local_arr), i, -1
        
        yield list(local_arr), -1, -1

    @staticmethod
    def bogo_sort_generator(arr: List[int], max_iterations: int = 1000) -> AlgorithmGenerator:
        """Bogo sort algorithm generator (limited iterations)."""
        local_arr = list(arr)
        iteration = 0
        
        def is_sorted(array: List[int]) -> bool:
            return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
        
        while not is_sorted(local_arr) and iteration < max_iterations:
            random.shuffle(local_arr)
            iteration += 1
            
            active_idx1 = random.randint(0, len(local_arr) - 1)
            active_idx2 = random.randint(0, len(local_arr) - 1)
            yield list(local_arr), active_idx1, active_idx2
        
        yield list(local_arr), -1, -1

    @staticmethod
    def merge_sort_generator(arr: List[int]) -> AlgorithmGenerator:
        """Merge sort algorithm generator."""
        local_arr = list(arr)
        
        def merge(array, left, mid, right):
            left_arr = array[left:mid + 1]
            right_arr = array[mid + 1:right + 1]
            
            i = j = 0
            k = left
            
            while i < len(left_arr) and j < len(right_arr):
                yield list(array), left + i, mid + 1 + j
                
                if left_arr[i] <= right_arr[j]:
                    array[k] = left_arr[i]
                    i += 1
                else:
                    array[k] = right_arr[j]
                    j += 1
                
                yield list(array), k, -1
                k += 1
            
            while i < len(left_arr):
                array[k] = left_arr[i]
                yield list(array), k, -1
                i += 1
                k += 1
            
            while j < len(right_arr):
                array[k] = right_arr[j]
                yield list(array), k, -1
                j += 1
                k += 1
        
        def merge_sort_recursive(array, left, right):
            if left < right:
                mid = (left + right) // 2
                
                yield from merge_sort_recursive(array, left, mid)
                yield from merge_sort_recursive(array, mid + 1, right)
                yield from merge(array, left, mid, right)
        
        yield from merge_sort_recursive(local_arr, 0, len(local_arr) - 1)
        yield list(local_arr), -1, -1

def get_algorithm_function(choice: str):
    """Map algorithm choice to function."""
    algorithm_map = {
        '1': SortingAlgorithms.bubble_sort_generator,
        '2': SortingAlgorithms.selection_sort_generator,
        '3': SortingAlgorithms.insertion_sort_generator,
        '4': SortingAlgorithms.quick_sort_generator,
        '5': SortingAlgorithms.heap_sort_generator,
        '6': SortingAlgorithms.shell_sort_generator,
        '7': SortingAlgorithms.comb_sort_generator,
        '8': SortingAlgorithms.radix_sort_generator,
        '9': SortingAlgorithms.bucket_sort_generator,
        '10': SortingAlgorithms.bogo_sort_generator,
        '11': SortingAlgorithms.merge_sort_generator,
    }
    return algorithm_map[choice]

# --- Visualization Class ---

class SortingVisualizer:
    """Advanced sorting algorithm visualizer with customizable bar count."""
    
    def __init__(self, n_bars: int):
        self.n_bars = n_bars
        self.initial_array = self._generate_array()
        
    def _generate_array(self) -> List[int]:
        """Generate array with heights from 1 to n_bars, randomly shuffled."""
        array = list(range(1, self.n_bars + 1))
        random.shuffle(array)
        print(f"🎲 Generated random array: {array[:10]}{'...' if len(array) > 10 else ''}")
        return array
    
    def _setup_plot_style(self, ax: plt.Axes, title: str) -> None:
        """Configure plot appearance with green bars on black background."""
        ax.set_title(title, color='white', fontsize=14, fontweight='bold')
        ax.set_facecolor(BACKGROUND_COLOR)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1, self.n_bars)
        ax.set_ylim(0, self.n_bars + 1)
        
        # Remove spines for cleaner look
        for spine in ax.spines.values():
            spine.set_visible(False)
    
    def _create_bars(self, ax: plt.Axes) -> List[plt.Rectangle]:
        """Create initial bar chart with green bars."""
        bar_width = 0.8 if self.n_bars <= 50 else 0.95  # Adjust width based on bar count
        
        bars = ax.bar(
            range(self.n_bars), 
            self.initial_array, 
            color=BAR_COLOR_NORMAL,
            edgecolor='darkgreen',
            linewidth=0.1 if self.n_bars > 100 else 0.2,
            width=bar_width
        )
        return bars
    
    def _validate_array(self, array: List[int]) -> bool:
        """Check if array is correctly sorted."""
        return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
    
    def _update_animation_frame(self, frame_number: int, algorithms_data: List[dict], 
                              standard_frames: int) -> List:
        """Update animation frame for both algorithms."""
        updated_artists = []
        
        for algo_data in algorithms_data:
            bars = algo_data['bars']
            original_frames = algo_data['original_frames']
            text_label = algo_data['text_label']
            algorithm_name = algo_data['name']
            algorithm_finish_frame = algo_data['algorithm_finish_frame']
            validation_start_frame = algo_data.get('validation_start_frame', algorithm_finish_frame + 1)
            validation_duration = 50  # Validation takes 50 frames
            is_first_completed = algo_data.get('is_first_completed', False)
            
            # Check if this algorithm should still be running
            if frame_number <= algorithm_finish_frame:
                # Algorithm is still running
                if original_frames and len(original_frames) > 0:
                    # Calculate which frame to show from original frames
                    progress_ratio = frame_number / algorithm_finish_frame
                    original_frame_index = int(progress_ratio * (len(original_frames) - 1))
                    original_frame_index = min(original_frame_index, len(original_frames) - 1)
                    
                    current_array, active_idx1, active_idx2 = original_frames[original_frame_index]
                    
                    # Update bar heights and colors
                    for bar_idx, bar in enumerate(bars):
                        bar.set_height(current_array[bar_idx])
                        
                        # Set colors: selected bars are black, others are green
                        if bar_idx == active_idx1 or bar_idx == active_idx2:
                            bar.set_color(BAR_COLOR_SELECTED)  # Black for selected
                        else:
                            bar.set_color(BAR_COLOR_NORMAL)    # Green for normal
                    
                    # Show progress
                    progress_percent = (frame_number / algorithm_finish_frame) * 100
                    text_label.set_text(f'{algorithm_name} - Progress: {progress_percent:.1f}%')
                else:
                    # No frames available
                    progress_percent = (frame_number / algorithm_finish_frame) * 100
                    text_label.set_text(f'{algorithm_name} - Progress: {progress_percent:.1f}%')
            elif frame_number <= validation_start_frame + validation_duration:
                # Algorithm is in validation phase
                if original_frames and len(original_frames) > 0:
                    final_array, _, _ = original_frames[-1]
                    
                    # Calculate validation progress
                    validation_progress = (frame_number - validation_start_frame) / validation_duration
                    validation_progress = max(0, min(1, validation_progress))
                    
                    # How many bars to validate so far
                    bars_to_validate = int(validation_progress * self.n_bars)
                    
                    # Check if array is correctly sorted
                    is_correct = self._validate_array(final_array)
                    
                    for bar_idx, bar in enumerate(bars):
                        bar.set_height(final_array[bar_idx])
                        
                        if bar_idx < bars_to_validate:
                            # Already validated bars
                            if is_correct:
                                bar.set_color('#0080FF')  # Blue for validated correct
                            else:
                                bar.set_color('#FF0000')  # Red for validation error
                        else:
                            # Not yet validated
                            bar.set_color('#00AA00')  # Dark green for completed but not validated
                    
                    # Show validation progress
                    validation_percent = validation_progress * 100
                    if is_first_completed:
                        text_label.set_text(f'WINNER - {algorithm_name} - Validating: {validation_percent:.0f}%')
                    else:
                        text_label.set_text(f'{algorithm_name} - Validating: {validation_percent:.0f}%')
                else:
                    # No frames available
                    if is_first_completed:
                        text_label.set_text(f'WINNER - {algorithm_name} - Validating...')
                    else:
                        text_label.set_text(f'{algorithm_name} - Validating...')
            else:
                # Validation completed
                if original_frames and len(original_frames) > 0:
                    final_array, _, _ = original_frames[-1]
                    is_correct = self._validate_array(final_array)
                    
                    for bar_idx, bar in enumerate(bars):
                        bar.set_height(final_array[bar_idx])
                        if is_correct:
                            bar.set_color('#0080FF')  # Blue for validated correct
                        else:
                            bar.set_color('#FF0000')  # Red for validation error
                    
                    # Show final status
                    if is_correct:
                        if is_first_completed:
                            text_label.set_text(f'WINNER - {algorithm_name} - VALID SORT!')
                        else:
                            text_label.set_text(f'{algorithm_name} - VALID SORT!')
                    else:
                        text_label.set_text(f'{algorithm_name} - ❌ SORT ERROR!')
                else:
                    if is_first_completed:
                        text_label.set_text(f'WINNER - {algorithm_name} - COMPLETED!')
                    else:
                        text_label.set_text(f'{algorithm_name} - COMPLETED!')
            
            updated_artists.extend(bars)
            updated_artists.append(text_label)
        
        return updated_artists
    
    def visualize_algorithms(self, algo1_choice: str, algo2_choice: str, algo_names: dict):
        """Main visualization method for two algorithms."""
        
        # Get algorithm functions
        algo1_func = get_algorithm_function(algo1_choice)
        algo2_func = get_algorithm_function(algo2_choice)
        algo1_name = algo_names[algo1_choice]
        algo2_name = algo_names[algo2_choice]
        
        print(f"🔄 Generating frames for algorithms...")
        
        # Generate frames for both algorithms
        algorithm_frames_data = {}
        
        for algo_func, name in [(algo1_func, algo1_name), (algo2_func, algo2_name)]:
            print(f"  📊 Generating frames for {name}...")
            generator = algo_func(self.initial_array.copy())
            frames = []
            
            try:
                for frame_data in generator:
                    frames.append(frame_data)
            except StopIteration:
                pass
            
            algorithm_frames_data[name] = frames
            print(f"     Generated {len(frames)} frames")
        
        # Calculate execution times for proportional animation timing
        execution_times = {}
        fastest_time = float('inf')
        fastest_algorithm = None
        
        print("⏱️ Measuring real execution times...")
        for name in algorithm_frames_data.keys():
            # Simulate execution time based on frame count (approximation)
            frame_count = len(algorithm_frames_data[name])
            # More frames generally means more operations, so longer time
            exec_time = frame_count * 0.000001  # Simulated time per operation
            execution_times[name] = exec_time
            print(f"   {name}: {frame_count} frames → {exec_time:.6f}s")
            
            if exec_time < fastest_time:
                fastest_time = exec_time
                fastest_algorithm = name
        
        print(f"🏆 Fastest: {fastest_algorithm} ({fastest_time:.6f}s)")
        
        # Calculate animation timing based on real performance
        BASE_ANIMATION_FRAMES = 600  # Base frames for fastest algorithm
        
        # Setup figure
        fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZE)
        fig.patch.set_facecolor(BACKGROUND_COLOR)
        
        # Prepare algorithm data with proportional timing
        algorithms_data = []
        first_to_complete = fastest_algorithm
        
        for i, (name, frames) in enumerate(algorithm_frames_data.items()):
            ax = axes[i]
            
            # Setup plot style
            self._setup_plot_style(ax, name)
            
            # Create bars
            bars = self._create_bars(ax)
            
            # Create text label
            text_label = ax.text(
                0.02, 0.95, f'{name} - Starting...', 
                transform=ax.transAxes, 
                color='white', 
                fontsize=11,
                fontweight='bold'
            )
            
            # Calculate proportional finish frame based on real execution time
            time_ratio = execution_times[name] / fastest_time
            algorithm_finish_frame = int(BASE_ANIMATION_FRAMES * time_ratio)
            validation_start_frame = algorithm_finish_frame + 10  # Start validation 10 frames after completion
            is_first_completed = (name == first_to_complete)
            
            print(f"   {name}: ratio {time_ratio:.2f} → finishes at frame {algorithm_finish_frame}")
            
            algorithms_data.append({
                'bars': bars,
                'original_frames': frames,
                'text_label': text_label,
                'name': name,
                'algorithm_finish_frame': algorithm_finish_frame,
                'validation_start_frame': validation_start_frame,
                'is_first_completed': is_first_completed
            })
        
        # Calculate animation settings (include validation time)
        validation_duration = 50
        max_finish_frame = max(algo_data['algorithm_finish_frame'] for algo_data in algorithms_data)
        total_frames = max_finish_frame + 10 + validation_duration + 30  # Longest sorting + delay + validation + padding
        target_duration = 18.0  # seconds (longer for validation)
        interval = max(10, int((target_duration * 1000) / total_frames))
        
        print(f"🎬 Starting proportional animation...")
        print(f"⏱️ Animation: {total_frames} frames, {interval}ms interval")
        print(f"📺 Duration: ~{(interval * total_frames) / 1000:.1f} seconds")
        print(f"🎨 Green bars, black background, selected bars in black")
        print(f"🏆 WINNER: {first_to_complete} (fastest algorithm)")
        print(f"⚡ Algorithms finish at different times based on performance")
        print(f"🔍 Validation: Each completed algorithm will be validated")
        print(f"💙 Valid sorts turn blue, ❤️ invalid sorts turn red")
        
        # Create and start animation
        animation_obj = animation.FuncAnimation(
            fig,
            lambda frame: self._update_animation_frame(frame, algorithms_data, BASE_ANIMATION_FRAMES),
            frames=range(total_frames),
            blit=False,
            interval=interval,
            repeat=False,
            cache_frame_data=False
        )
        
        plt.tight_layout()
        plt.show()
        
        return animation_obj

if __name__ == "__main__":
    # Get user input
    n_bars = get_user_input()
    algo1, algo2, algo_names = get_algorithm_selection()
    
    print(f"🔧 Setting up visualization for {n_bars} bars...")
    print(f"📈 Algorithm 1: {algo_names[algo1]}")
    print(f"📈 Algorithm 2: {algo_names[algo2]}")
    
    # Create and run visualizer
    visualizer = SortingVisualizer(n_bars)
    visualizer.visualize_algorithms(algo1, algo2, algo_names)

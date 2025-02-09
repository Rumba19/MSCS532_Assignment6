# MSCS532 Assignment 6:  
## **Overview**
 This assignment focuses on implementing and analyzing the Quick Sort algorithm, specifically its deterministic and randomized variants. The project includes:
- Implementation of Deterministic Quicksort and Randomized Quicksort.
- Theoretical analysis of their time complexities.
- Empirical evaluation comparing both methods.
- Benchmarking results based on various types of input arrays (sorted, reverse-sorted, and random).

---

### **Prerequisites to run the script**
1. **Python**: Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/).
2. **Install Dependencies and How To Run**: Run the following command to install the required library (`numpy`):
    ```bash
   pip3 install numpy
    git clone https://github.com/Rumba19/MSCS532_Assignment5
    cd MSCS532_ASSIGNMENT5
    python3 quicksort.py

 
### **Findings and Observations**

 **Performance Comparison:**

- Deterministic Quicksort: Performs well for large datasets, ensuring stable sorting time, but struggles with inefficient pivot selection.
- Randomized Quicksort: Generally faster on average, benefiting from randomized pivot selection, though worst-case complexity remains .

**Empirical Results:**

- For random data, randomized QuickSort performs better in most cases.
- For nearly sorted data, deterministic QuickSort is more stable and prevents worst-case scenarios.
- Reverse sorted input significantly impacts deterministic QuickSort performance without careful pivot selection.

**Key Insights:**

- The choice of pivot greatly affects sorting efficiency.
- Randomization helps avoid worst-case scenarios in many cases.
- The deterministic approach provides predictability but may not always be optimal in practice.




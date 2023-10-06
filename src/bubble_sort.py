import streamlit as st
import time

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

# Streamlit UI
def main():
    st.title("Bubble Sort Visualization")
    st.sidebar.header("Sort Settings")

    # User input for array size
    array_size = st.sidebar.slider("Array Size", 5, 50, 10)

    # Generate a random unsorted array
    unsorted_array = list(range(array_size, 0, -1))

    st.write("Unsorted Array:", unsorted_array)

    # Visualization of the sorting process
    st.header("Sorting Animation")
    chart = st.bar_chart(unsorted_array)

    if st.sidebar.button("Sort"):
        st.sidebar.text("Sorting in progress...")
        for step in bubble_sort(unsorted_array):
            chart.bar_chart(step)
            time.sleep(0.2)  # Adjust the speed of the visualization

        st.sidebar.text("Sorting completed!")

if __name__ == "__main__":
    main()

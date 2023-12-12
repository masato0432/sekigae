# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Create a function to generate the seat arrangement
def generate_seat_arrangement():
    # Create a 7x6 grid of seats
    seats = np.arange(1, 43).reshape(7, 6)
    # Randomly shuffle the numbers from 1 to 41
    np.random.shuffle(seats)
    return seats

# Main function to run the web application
def main():
    # Set the title of the web app
    st.title("席替えの席を決める")

    # Add a button to trigger the seat arrangement generation
    if st.button("開始"):
        # Call the function to generate the seat arrangement
        seat_arrangement = generate_seat_arrangement()
        # Create a pandas DataFrame to display the seat arrangement as a table
        df = pd.DataFrame(seat_arrangement, columns=[f"Column {i+1}" for i in range(6)], index=[f"Row {i+1}" for i in range(7)])
        # Display the seat arrangement as a table
        st.write(df)

# Run the main function
if __name__ == "__main__":
    main()
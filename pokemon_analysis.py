
# Import Pandas to work with the Pokemon dataset
import pandas as pd

# Import Matplotlib to create charts
import matplotlib.pyplot as plt

# Import mplcursors to display values when hovering over the chart
import mplcursors


# Read the Pokemon CSV file
pokemon = pd.read_csv("Pokemon.csv")

# Display basic information about the Pokemon dataset
def show_dataset_info():
    print("\n===== DATASET INFORMATION =====")

    # Display the total number of Pokemon records
    print("Total Pokemon records:", len(pokemon))

    # Display the number of columns
    print("Number of columns:", len(pokemon.columns))

    # Select the columns needed for the analysis
    selected_data = pokemon[["Name", "Type 1", "Attack"]]

    # Display the first five Pokemon records
    print("\nFirst five Pokemon:")
    print(selected_data.head())

# Count how many Pokemon belong to each primary type
type_counts = pokemon["Type 1"].value_counts()

# Display Pokemon by type and answer the first question
def show_pokemon_by_type():
    print("\n===== POKEMON BY TYPE =====")

    # Display the number of Pokemon for each type
    print(type_counts)

    # Find the most common Pokemon type
    most_common_type = type_counts.idxmax()

    # Find how many Pokemon belong to the most common type
    most_common_count = type_counts.max()

    # Calculate the percentage of Pokemon with this type
    percentage = (most_common_count / len(pokemon)) * 100

    # Display the answer to the first question
    print("\nQuestion 1: Which Pokemon type appears most often?")
    print("Most common type:", most_common_type)
    print("Number of Pokemon:", most_common_count)
    print("Percentage:", round(percentage, 2), "%")

# Calculate and display attack statistics
def show_attack_stats():
    print("\n===== ATTACK STATISTICS =====")

    # Calculate the average attack value
    average_attack = pokemon["Attack"].mean()

    # Find the highest and lowest attack values
    highest_attack = pokemon["Attack"].max()
    lowest_attack = pokemon["Attack"].min()

    # Display the answer to the second question
    print("\nQuestion 2: What is the average attack value?")
    print("Average attack:", round(average_attack, 2))

    # Display additional attack statistics
    print("Highest attack:", highest_attack)
    print("Lowest attack:", lowest_attack)

# Display the 10 Pokemon with the highest attack values
def show_top_attack():
    print("\n===== TOP 10 POKEMON BY ATTACK =====")

    # Sort Pokemon by attack from highest to lowest
    sorted_pokemon = pokemon.sort_values(by="Attack", ascending=False)

    # Select the columns we want to display
    top_pokemon = sorted_pokemon[["Name", "Type 1", "Attack"]]

    # Display the first 10 Pokemon without the row index
    print(top_pokemon.head(10).to_string(index=False))

# Search for Pokemon by name and display their information
def search_pokemon():
    print("\n===== SEARCH POKEMON =====")

    # Ask the user to enter a Pokemon name
    name = input("Enter a Pokemon name: ")

    # Find Pokemon that match the name entered by the user
    results = pokemon[pokemon["Name"].str.contains(name, case=False, regex=False)]

    # Check if any Pokemon were found
    if results.empty:
        print("No Pokemon found.")
    else:
        # Select the Pokemon information to display
        selected_data = results[["Name", "Type 1", "Attack", "Defense", "Speed"]]

        # Display the search results
        print("\nSearch results:")
        print(selected_data.to_string(index=False))

# Calculate and display the average attack for each Pokemon type
def show_average_attack_by_type():
    print("\n===== AVERAGE ATTACK BY TYPE =====")

    # Group Pokemon by their primary type and calculate the average attack
    average_by_type = pokemon.groupby("Type 1")["Attack"].mean()

    # Sort the average attack values from highest to lowest
    average_by_type = average_by_type.sort_values(ascending=False)

    # Round the average values to two decimal places
    average_by_type = average_by_type.round(2)

    # Display the average attack for each type
    print(average_by_type)

    # Find the type with the highest average attack
    strongest_type = average_by_type.idxmax()

    # Display the answer to the third question
    print("\nQuestion 3: Which type has the highest average attack?")
    print("Pokemon type:", strongest_type)
    print("Average attack:", average_by_type.max())

# Create and display an interactive chart of Pokemon by type
def show_type_chart():
    print("\n===== POKEMON TYPE CHART =====")

    # Create a bar chart showing the number of Pokemon by type
    ax = type_counts.plot(kind="bar")

    # Add a title and labels to the chart
    plt.title("Number of Pokemon by Primary Type")
    plt.xlabel("Pokemon Type")
    plt.ylabel("Number of Pokemon")

    # Enable hover information on the bars
    cursor = mplcursors.cursor(ax.containers[0], hover=True)

    # Display the Pokemon type and quantity when hovering
    @cursor.connect("add")
    def show_bar_info(sel):
        pokemon_type = type_counts.index[sel.index]
        quantity = type_counts.iloc[sel.index]

        sel.annotation.set_text(
            f"{pokemon_type}\nQuantity: {quantity}"
        )

    # Adjust the chart layout
    plt.tight_layout()

    # Display the chart
    plt.show()

# Display the main menu and execute the selected option
def main():
    while True:
        print("\n===== POKEMON DATA ANALYSIS =====")
        print("1. View dataset information")
        print("2. Show Pokemon by type")
        print("3. Show average attack")
        print("4. Show top 10 Pokemon by attack")
        print("5. Search Pokemon by name")
        print("6. Show interactive chart")
        print("7. Show average attack by type")
        print("8. Exit")

        # Ask the user to choose an option
        choice = input("\nChoose an option: ")

        # Execute the selected function
        if choice == "1":
            show_dataset_info()

        elif choice == "2":
            show_pokemon_by_type()

        elif choice == "3":
            show_attack_stats()

        elif choice == "4":
            show_top_attack()

        elif choice == "5":
            search_pokemon()

        elif choice == "6":
            show_type_chart()

        elif choice == "7":
            show_average_attack_by_type()

        elif choice == "8":
            print("Thank you for using Pokemon Data Analysis!")
            break

        else:
            print("Invalid option. Please try again.")


# Start the program
main()


#"""
#Project: [India Water Analysis]
#Author: [Rachael Moseley]
#Date: [12/04/2024]

#Interactive data analysis program for [your topic].
#"""

# 2. Imports
import pandas as pd
import matplotlib.pyplot as plt


# 3. Constants
MENU_OPTIONS = {
    '1': 'Analyze entire dataset',
    '2': 'Station number and locations graph!',
    '3': 'Exit program'
}


# 4. Data Processing Functions
def load_data(filename):
    """Load and validate dataset"""
    try:
        df = pd.read_csv(filename)
        print(f"Loaded {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None



# 5. Analysis/Summary Functions
def analyze_data(df, feature=None):
    """Analyze data based on user selection"""
    if df is None or df.empty:
        print("No data to analyze at the moment.")
        return
    
    if feature:
        if feature not in df.columns:
            print(f"Feature '{feature}' not found in the dataset.")
            return
        print(f"\nAnalysis of '{feature}':")
        print(df[feature].head(5).to_string(index=False))

    else:
        print("\nFull dataset analysis:")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of colums: {df.shape[1]}")
        print("\nColumn names and their values:")

        for col in df.columns:
            print(f"\n{col}: {', '.join(map(str, df[col].head(5).values))}")

        
def graph(df):
   if df is None:
       print("NO data")
       return
   
   x_column = 'STATION CODE' 
   y_column = 'LOCATIONS'

   plt.figure(figsize=(15, 6))
   plt.plot(df[x_column], df[y_column], marker='o', color='blue')
   plt.xlabel(x_column)
   plt.ylabel(y_column)
   plt.title(f"{y_column} and {x_column}")
   plt.grid(True)
   plt.show()




# 6. Interactive Features
def display_menu():
    """Show main menu and get user choice"""
    print("\n=== Data Analysis Menu for Water Stations in India ===")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    return input("Enter your number choice: ")

# 7. Main Program
def main():
    df = load_data('water.csv')
    while True:
        choice = display_menu()
        if choice == '3':
            break
        if choice == '1':
           analyze_data(df)
        if choice == '2':
            graph(df)

    




if __name__ == "__main__":
    main()
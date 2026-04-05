from load_csv import load
import matplotlib.pyplot as plt


def plot_life_expectancy(path: str) -> None:
    """Load life expectancy CSV and plot the campus country's data over time."""
    df = load(path)
    if df is None:
        return
    row = df.loc[df["country"] == "United Arab Emirates"]

    years = row.columns[1:].astype(int)
    values = row.iloc[0, 1:].values.astype(float)

    plt.plot(years, values)
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("United Arab Emirates")
    plt.savefig('output.png')
    plt.show()


def main():
    """Entry point: run life expectancy plot."""
    path = "life_expectancy_years.csv"
    plot_life_expectancy(path)


if __name__ == "__main__":
    main()

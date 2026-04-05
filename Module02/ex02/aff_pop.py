from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def parse_pop(val):
    val = str(val).strip()
    if val.endswith('M'):
        return float(val[:-1]) * 1_000_000
    if val.endswith('k') or val.endswith('K'):
        return float(val[:-1]) * 1_000
    return float(val)


def format_population(val, _):
    if val >= 1_000_000:
        return f"{val / 1_000_000:.0f}M"
    if val >= 1_000:
        return f"{val / 1_000:.0f}K"
    return str(int(val))


def plot_population_comparison(path: str) -> None:
    """Load population CSV and plot UAE vs US population from 1800 to 2050."""
    df = load(path)
    if df is None:
        return
    uae = df.loc[df["country"] == "United Arab Emirates"]

    x_uae = uae.columns[1:uae.columns.get_loc("2050")].astype(int)
    y_uae = uae.iloc[
        0, 1:uae.columns.get_loc("2050")
    ].map(parse_pop).values.astype(float)

    us = df.loc[df["country"] == "United States"]

    x_us = us.columns[1:us.columns.get_loc("2050")].astype(int)
    y_us = us.iloc[
        0, 1:us.columns.get_loc("2050")
    ].map(parse_pop).values.astype(float)

    plt.plot(x_uae, y_uae, label="United Arab Emirates")
    plt.plot(x_us, y_us, label="United States")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(format_population)
    )
    plt.legend()
    plt.savefig('output.png')
    plt.show()


def main():
    """Main function to execute the population comparison plot."""
    path = "population_total.csv"
    plot_population_comparison(path)


if __name__ == "__main__":
    main()

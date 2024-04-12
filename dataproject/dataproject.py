import matplotlib.pyplot as plt
import seaborn as sns

def plot(data, x, y, by=None):
    """
    Plots the data as a scatter plot. If a facet_by column is provided, creates a FacetGrid.
    :param data: pandas DataFrame containing the data.
    :param x: str, the column name for the x-axis.
    :param y: str, the column name for the y-axis.
    :param by: str, optional, the column name to facet the grid by.
    """
    if by is None:
        # Simple scatter plot
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, data=data)
        mean_y = data[y].mean()
        median_y = data[y].median()
        plt.axhline(mean_y, color='red', linestyle='--', label = 'Mean')
        plt.axhline(median_y, color='blue', linestyle=':', label='Median')
        plt.title(f"Scatter Plot of {y} vs {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend()
        plt.show()
    else:
        # FacetGrid scatter plot
        g = sns.FacetGrid(data, col=by, height=5, aspect=1)
        g.map_dataframe(sns.scatterplot, x, y)
        # Add a line for the mean of y in each facet
        def add_mean_median_line(data, **kwargs):
            plt.axhline(y=data[y].mean(), color='red', linestyle='--', label='Mean')
            plt.axhline(y=data[y].median(), color='blue', linestyle=':', label='Median')
        g.map_dataframe(add_mean_median_line)
        g.set_axis_labels(x, y)
        g.set_titles(f"{by}: {{col_name}}")
        g.add_legend()
        plt.show()
# --------------------------------------------------------------------------- #
# Purpose: Create a scientific-style plot for multiple datasets.
# 
# Author: Matheus Ferreira Silva
# GitHub: https://github.com/MatheusFS-dev
# Last Modified: 23 December 2024
#
# --------------------------------------------------------------------------- #

import matplotlib.pyplot as plt
from typing import List, Optional, Tuple

def plot_scientific(
    x: List[float],
    y_datasets: List[List[float]],
    labels: Optional[List[str]] = None,
    x_label: str = "X-axis",
    y_label: str = "Y-axis",
    title: str = "Scientific Plot",
    x_integer: bool = False,
    y_log: bool = False,
    markers: Optional[List[str]] = None,
    line_styles: Optional[List[str]] = None,
    legend_loc: str = "best",
    grid: bool = True,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    save_path: Optional[str] = None,
    dpi: int = 300
) -> None:
    """
    Plots multiple Y datasets against a shared X-axis with scientific paper styling.

    Args:
        x (List[float]): List of X-axis values.
        y_datasets (List[List[float]]): List of lists containing Y-axis datasets.
        labels (Optional[List[str]]): Labels for each dataset for the legend.
        x_label (str): Label for the X-axis. Default is "X-axis".
        y_label (str): Label for the Y-axis. Default is "Y-axis".
        title (str): Title of the plot. Default is "Scientific Plot".
        x_integer (bool): Force X-axis to display only integer values. Default is False.
        y_log (bool): Use logarithmic scale for the Y-axis. Default is False.
        markers (Optional[List[str]]): List of marker styles for each dataset.
        line_styles (Optional[List[str]]): List of line styles for each dataset.
        legend_loc (str): Location of the legend. Default is "best".
        grid (bool): Whether to display a grid. Default is True.
        xlim (Optional[Tuple[float, float]]): Limits for the X-axis as (min, max). Default is None.
        ylim (Optional[Tuple[float, float]]): Limits for the Y-axis as (min, max). Default is None.
        save_path (Optional[str]): Path to save the plot as a file. Default is None.
        dpi (int): Resolution of the saved plot in dots per inch. Default is 300.

    Returns:
        None: Displays the plot and optionally saves it as an image.
    """
    # Validate input dimensions
    if any(len(y) != len(x) for y in y_datasets):
        raise ValueError("All Y datasets must have the same length as the X dataset.")

    # Initialize the plot
    plt.figure(figsize=(8, 6))
    
    # Plot each dataset
    for i, y in enumerate(y_datasets):
        label = labels[i] if labels and i < len(labels) else f"Dataset {i + 1}"
        marker = markers[i] if markers and i < len(markers) else 'o'
        line_style = line_styles[i] if line_styles and i < len(line_styles) else '-'
        plt.plot(x, y, label=label, marker=marker, linestyle=line_style)

    # Configure axes and title
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(title, fontsize=14, weight='bold')
    plt.legend(loc=legend_loc, fontsize=10)
    
    # Configure axis limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Configure X-axis for integers only
    if x_integer:
        plt.xticks(ticks=range(int(min(x)), int(max(x)) + 1))
    
    # Enable logarithmic scale for Y-axis if requested
    if y_log:
        plt.yscale('log')
    
    # Add grid if requested
    if grid:
        plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Final styling
    plt.tight_layout()

    # Save plot if path is provided
    if save_path:
        plt.savefig(save_path, dpi=dpi, format="png")
    
    # Show plot
    plt.show()

# Example code
if __name__ == "__main__":
    # Example: Plotting three datasets with markers, line styles, and log scale
    x = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    y2 = [1, 2, 3, 4, 5]
    y3 = [2, 3, 5, 7, 11]

    plot_scientific(
        x=x,
        y_datasets=[y1, y2, y3],
        labels=["Linear Growth", "Constant Growth", "Prime Numbers"],
        x_label="Time (s)",
        y_label="Value",
        title="Example Plot with Line Styles and Logarithmic Scale",
        x_integer=True,
        # xlim=(0, 6),
        ylim=(0, 6),
        y_log=False,
        markers=['o', 's', '^'],  # Circle, square, and triangle markers
        line_styles=['-', '--', ':'],  # Solid, dashed, and dotted line styles
        save_path="example_plot_with_styles.png"
    )

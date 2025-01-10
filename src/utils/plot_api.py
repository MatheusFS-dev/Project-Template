# ---------------------------------------------------------------------------- #
#                      Authored by Matheus Ferreira Silva                      #
#                           github.com/MatheusFS-dev                           #
# ---------------------------------------------------------------------------- #    

import matplotlib.pyplot as plt
from typing import List, Optional, Tuple
import seaborn as sns
import numpy as np


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
    dpi: int = 300,
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
        marker = markers[i] if markers and i < len(markers) else "o"
        line_style = line_styles[i] if line_styles and i < len(line_styles) else "-"
        plt.plot(x, y, label=label, marker=marker, linestyle=line_style)

    # Configure axes and title
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.title(title, fontsize=14, weight="bold")
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
        plt.yscale("log")

    # Add grid if requested
    if grid:
        plt.grid(visible=True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Final styling
    plt.tight_layout()

    # Save plot if path is provided
    if save_path:
        plt.savefig(save_path, dpi=dpi, format="png")

    # Show plot
    plt.show()


def plot_histogram(
    datasets: List[List[float]],
    bins: int = 10,
    density: bool = False,
    labels: Optional[List[str]] = None,
    colors: Optional[List[str]] = None,
    edgecolors: Optional[List[str]] = None,
    alpha: float = 0.7,
    x_label: str = "X-axis",
    y_label: str = "Frequency",
    title: str = "Histogram",
    legend_loc: str = "best",
    grid: bool = True,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    save_path: Optional[str] = None,
    dpi: int = 300,
) -> None:
    """
    Plots a histogram for one or more datasets with scientific styling.

    Args:
        datasets (List[List[float]]): List of datasets to plot histograms for.
        bins (int): Number of bins in the histogram. Default is 10.
        density (bool): If True, normalizes the histogram so the area equals 1. Default is False.
        labels (Optional[List[str]]): Labels for each dataset for the legend. Default is None.
        colors (Optional[List[str]]): Colors for each dataset. Default is None.
        edgecolors (Optional[List[str]]): Edge colors for each dataset. Default is None.
        alpha (float): Transparency level of bars (0: fully transparent, 1: opaque). Default is 0.7.
        x_label (str): Label for the X-axis. Default is "X-axis".
        y_label (str): Label for the Y-axis. Default is "Frequency".
        title (str): Title of the histogram. Default is "Histogram".
        legend_loc (str): Location of the legend. Default is "best".
        grid (bool): Whether to display a grid. Default is True.
        xlim (Optional[Tuple[float, float]]): Limits for the X-axis as (min, max). Default is None.
        ylim (Optional[Tuple[float, float]]): Limits for the Y-axis as (min, max). Default is None.
        save_path (Optional[str]): Path to save the histogram as a file. Default is None.
        dpi (int): Resolution of the saved histogram in dots per inch. Default is 300.

    Returns:
        None: Displays the histogram and optionally saves it as an image.
    """
    # Initialize the plot
    plt.figure(figsize=(8, 6))

    # Plot each dataset as a histogram
    for i, data in enumerate(datasets):
        label = labels[i] if labels and i < len(labels) else f"Dataset {i + 1}"
        color = colors[i] if colors and i < len(colors) else None
        edgecolor = edgecolors[i] if edgecolors and i < len(edgecolors) else None
        plt.hist(
            data,
            bins=bins,
            density=density,
            alpha=alpha,
            label=label,
            color=color,
            edgecolor=edgecolor,
        )

    # Configure axes and title
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label if not density else "Density", fontsize=12)
    plt.title(title, fontsize=14, weight="bold")

    # Configure axis limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Add grid if requested
    if grid:
        plt.grid(visible=True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Add legend if labels are provided
    if labels:
        plt.legend(loc=legend_loc, fontsize=10)

    # Final styling
    plt.tight_layout()

    # Save histogram if path is provided
    if save_path:
        plt.savefig(save_path, dpi=dpi, format="png")

    # Show histogram
    plt.show()


def plot_boxplot_scientific(
    dataset: np.ndarray,
    x_label: str = "Columns",
    y_label: str = "Values",
    title: str = "Boxplot of Dataset Columns",
    figsize: Tuple[int, int] = (12, 8),
    box_color: str = "gray",
    flier_color: str = "black",
    flier_size: int = 6,
    grid: bool = True,
    grid_style: str = "--",
    grid_alpha: float = 0.7,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    tick_rotation: int = 0,
    dpi: int = 300,
    save_path: Optional[str] = None,
    hide_xlabels: bool = False,
) -> Optional[str]:
    """
    Generates a highly configurable scientific-style boxplot.

    Args:
        dataset (np.ndarray): The dataset as a 2D NumPy array.
        x_label (str): Label for the X-axis. Default is "Columns".
        y_label (str): Label for the Y-axis. Default is "Values".
        title (str): Title of the plot. Default is "Boxplot of Dataset Columns".
        figsize (Tuple[int, int]): Size of the figure in inches. Default is (12, 8).
        box_color (str): Color of the boxes in the boxplot. Default is "gray".
        flier_color (str): Color of outlier points. Default is "black".
        flier_size (int): Size of the outlier points. Default is 6.
        grid (bool): Whether to show grid lines. Default is True.
        grid_style (str): Style of the grid lines. Default is "--".
        grid_alpha (float): Transparency of the grid lines. Default is 0.7.
        xlim (Optional[Tuple[float, float]]): Limits for the X-axis. Default is None.
        ylim (Optional[Tuple[float, float]]): Limits for the Y-axis. Default is None.
        tick_rotation (int): Rotation angle for X-axis tick labels. Default is 45.
        dpi (int): DPI for the saved plot image. Default is 300.
        save_path (Optional[str]): File path to save the plot. If None, the plot is displayed.
        hide_xlabels (bool): Whether to hide X-axis labels. Default is False.
    
    Returns:
        Optional[str]: The file path of the saved plot, or None if not saved.
    """
    # Create the plot
    plt.figure(figsize=figsize)
    sns.boxplot(
        data=dataset,
        orient="v",
        color=box_color,
        fliersize=flier_size,
        linewidth=1.5,
        flierprops=dict(marker='o', color=flier_color, markerfacecolor=flier_color),
    )

    # Configure titles and labels
    plt.title(title, fontsize=18, weight="bold")
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)

    # Configure axis limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Configure ticks
    plt.xticks(fontsize=12, rotation=tick_rotation)
    plt.yticks(fontsize=12)

    # Hide X-axis labels if requested
    if hide_xlabels:
        plt.xticks([])

    # Configure grid
    if grid:
        plt.grid(visible=True, linestyle=grid_style, linewidth=0.5, alpha=grid_alpha)

    # Save or show the plot
    if save_path:
        plt.savefig(save_path, dpi=dpi, bbox_inches="tight")   
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
        # ylim=(0, 12),
        y_log=True,
        markers=["o", "s", "^"],  # Circle, square, and triangle markers
        line_styles=["-", "--", ":"],  # Solid, dashed, and dotted line styles
        save_path="example_plot_with_styles.png",
    )

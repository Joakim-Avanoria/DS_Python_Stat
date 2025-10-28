import pandas as pd

def _cat_for_plot(s, missing_label="Okänd"):
    if hasattr(s, "astype"):
        s = s.astype("object")
    try:
        return s.fillna(missing_label)
    except Exception:
        return s

def _num_for_plot(s):
    try:
        return pd.to_numeric(s, errors="coerce").fillna(0)
    except Exception:
        return s

def bar(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    x = _cat_for_plot(x)
    y = _num_for_plot(y)
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax

def line(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    y = _num_for_plot(y)

    data = pd.DataFrame({"x": pd.to_datetime(x), "y": y}).dropna()
    data = data.sort_values("x")

    if data["x"].duplicated().any():
        data = (data
                .groupby(data["x"].to_period("M"))["y"]
                .sum()
                .reset_index()
        )
        data["x"] = data["x"].dt.to_timestamp()

    ax.plot(data["x"], data["y"], marker="o", linestyle="-")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    return ax

def box_h(ax, values, title, xlabel, grid: bool = True):
    values = _num_for_plot(values)
    ax.boxplot(values, vert=False)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(grid, axis="x")
    return ax
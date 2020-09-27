import matplotlib.colors as colors
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))


def use_paper_style():
    """Load custom matplotlib style sheet."""
    plt.style.use("paper.mplstyle")


def use_draft_style():
    """Load custom matplotlib style sheet."""
    plt.style.use("draft.mplstyle")

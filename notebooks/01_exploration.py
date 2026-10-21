# %%
# VS Code supports notebook-style cells in Python files via the #%% markers.
from pathlib import Path
import sys

ROOT = Path.cwd()
if not (ROOT / "src").exists():
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "src"))

from research.analysis import make_demo_data
data = make_demo_data()
data.head()

# %%
data.describe()

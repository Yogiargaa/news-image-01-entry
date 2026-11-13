import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
candidates = [os.path.join(here, "entry.png"),
              os.path.join(os.getcwd(), "entry.png")]
src = next(p for p in candidates if os.path.exists(p))
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))

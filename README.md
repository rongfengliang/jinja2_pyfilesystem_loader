# jinja2 pyfilesystem simple  loader 

## Usage

```code
from pyfs_loader import PyFilesystemLoader
loader = import("osfs://",search_path=template_dir)
env = j2.Environment(loader=loader)
```
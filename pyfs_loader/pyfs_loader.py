import fs
import jinja2
from jinja2.loaders import BaseLoader
class PyFilesystemLoader(BaseLoader):
    def __init__(self, fs_url,**kwargs):
        self.fs = fs.open_fs(fs_url)
        self.search_path = kwargs.get("search_path", None)
        
    def get_source(self, environment, template):
        path = template
        if self.search_path:
           path = self.search_path + "/" + template
           print("path with search_path",path)
        if not self.fs.exists(path):
            raise jinja2.TemplateNotFound(template)
        
        with self.fs.open(path, 'r') as f:
            source = f.read()
        
        return source, path, lambda: self.fs.getinfo(path).modified
    
    def list_templates(self):
        return [f.path for f in self.fs.walk.files(self.search_path if self.search_path else "/")]

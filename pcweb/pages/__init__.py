from pcweb.route import Route

from .blog import blog_routes
from .changelog import changelog
from .docs import doc_routes
from .docs.guide import guide
from .faq import faq
from .index import index
from .page404 import page404

routes = [
    *[r for r in locals().values() if isinstance(r, Route)],
    *blog_routes,
    *doc_routes,
]

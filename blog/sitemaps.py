from django.contrib.sitemaps import Sitemap
from blog.models import Post


class MyBlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.post_on

    @property
    def get_sitemap_dict(cls):
        sitemaps = {
            'posts': cls,
        }

        return sitemaps

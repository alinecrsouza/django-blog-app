import datetime
from haystack import indexes
from blog.models import Post

# SearchIndex for Post
# SearchIndex objects are the way Haystack determines what data should be placed in the search
# index and handles the flow of data in.
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    author = indexes.CharField(model_attr='author')
    category = indexes.CharField(model_attr='category')
    content = indexes.CharField(model_attr='content')
    #created_at = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())
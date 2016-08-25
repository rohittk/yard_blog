from __future__ import unicode_literals

from django.db.models import Model, CharField, TextField, ForeignKey


class Blog(Model):
    blog_title = CharField(max_length=50, null=False)
    blog_content = TextField(max_length=1000, null=False)

    def __unicode__(self):
        return self.blog_title


class Tags(Model):
    blog_fk = ForeignKey('blog.Blog')
    tags = CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.tags

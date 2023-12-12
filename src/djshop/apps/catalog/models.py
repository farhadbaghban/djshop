from django.db import models
from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    title =models.CharField(max_length=255,db_index=True)
    description = models.CharField(max_length=1024,null=True,blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
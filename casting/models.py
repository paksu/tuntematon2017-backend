from django.db import models


class Actor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    avatar_url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('created_at',)


class Casting(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=200, null=True, blank=True)

    koskela = models.ForeignKey(Actor, related_name="koskela", related_query_name="koskela", null=True)
    hietanen = models.ForeignKey(Actor, related_name="hietanen", related_query_name="hietanen", null=True)
    lammio = models.ForeignKey(Actor, related_name="lammio", related_query_name="lammio", null=True)
    rokka = models.ForeignKey(Actor, related_name="rokka", related_query_name="rokka", null=True)
    lahtinen = models.ForeignKey(Actor, related_name="lahtinen", related_query_name="lahtinen", null=True)
    lehto = models.ForeignKey(Actor, related_name="lehto", related_query_name="lehto", null=True)
    maatta = models.ForeignKey(Actor, related_name="maatta", related_query_name="maatta", null=True)
    rahikainen = models.ForeignKey(Actor, related_name="rahikainen", related_query_name="rahikainen", null=True)
    kariluoto = models.ForeignKey(Actor, related_name="kariluoto", related_query_name="kariluoto", null=True)
    sarastie = models.ForeignKey(Actor, related_name="sarastie", related_query_name="sarastie", null=True)
    kaarna = models.ForeignKey(Actor, related_name="kaarna", related_query_name="kaarna", null=True)

    class Meta:
        ordering = ('created_at',)

from django.template.defaultfilters import slugify

def slugifyUniquely(name, model, slugfield="slug"):
    suffix = 0
    potential = base = slugify(name)
    while True:
        if suffix:
           potential = "-".join([base, str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
            return potential
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1
                                                                                                                                            
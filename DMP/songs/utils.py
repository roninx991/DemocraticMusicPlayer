from django.utils.text import slugify
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slugg = new_slug
    else:
        slugg = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug_Field=slugg).exists()
    if qs_exists:
        new_slug = "{slugg}-{randstr}".format(
                    slugg,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug)
    return slugg

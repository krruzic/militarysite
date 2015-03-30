from django import template

register = template.Library()


# # tag to get field's verbose name in template
# @register.simple_tag
# def get_verbose_name(object):
#     return object.verbose_name.upper()

# tag to get the value of a field by name in template
@register.simple_tag
def get_value_from_key(object, key):
<<<<<<< HEAD
    # is it necessary to check isinstance(object, dict) here?
    return object[key]
=======
    return object[key]
>>>>>>> a9ad96fcc681d15937f98267eba4d98d3ced58fe

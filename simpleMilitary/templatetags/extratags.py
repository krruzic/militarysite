# tag to get field's verbose name in template
@register.simple_tag
def get_verbose_name(object):
    return object.verbose_name

# tag to get the value of a field by name in template
@register.simple_tag
def get_value_from_key(object, key):
    # is it necessary to check isinstance(object, dict) here?
    return object[key.name]
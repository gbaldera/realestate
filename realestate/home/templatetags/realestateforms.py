from django.template import Library

register = Library()

@register.filter
def widget_with_classes(widget, classes):
    #import ipdb; ipdb.set_trace()
    widget.field.widget.attrs['class'] = classes
    return widget
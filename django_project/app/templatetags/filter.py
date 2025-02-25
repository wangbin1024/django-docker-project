from django import template

register = template.Library()


@register.filter(name="status_to_string")
def convert_status_to_string(status: int) -> str:
    if status == 0:
        return "Pending"
    elif status == 1:
        return "Approved"
    else:
        return "Rejected"

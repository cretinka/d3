from django import template
import re

register = template.Library()

@register.filter(name='censor')
def censor(value):
    censored_words = ['дурак', 'мудак', 'редиска', 'идиот', 'придурок']
    censored_value = value
    for word in censored_words:
        censored_value = re.sub(r'\b' + re.escape(word) + r'\b', '*' * len(word), censored_value, flags=re.IGNORECASE)
    return censored_value

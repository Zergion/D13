from django import template

register = template.Library()


@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("охренеть", "В ШОКЕ")
    value = value.replace("афигенно", "ЗДОРОВО")
    value = value.replace("фигня", "ПЛОХО")
    return value


@register.filter(name='Censor1')
def Censor1(value, arg):
    if ("охренеть" in value) or ("афигенно" in value) or ("фигня" in value):
        arg = 'Вы используете плохие слова'
        return arg
    else:
        return value
import arabic_reshaper
from bidi.algorithm import get_display


def rtl(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

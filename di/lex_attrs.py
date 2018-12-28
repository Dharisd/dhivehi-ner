# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM


_num_words = set("""
  ސުމެއް
އެކެއް
ދޭއް
ތިނެއް
ހަތަރެއް
ފަހެއް
ހައެއް
ހަތެއް
އަށެއް
ނުވައެއް
ދިހައެއް
އެގާރަ
ބާރަ
ތޭރަ
ސާދަ
ފަނަރަ
ސޯޅަ
ސަތާރަ
އަށާރަ
ނަވާރަ
ވިހި
އެކާވީސް
ބާވީސް
ތޭވީސް
ސައުވީސް
ފަންސަވީސް
ސައްބީސް
ހަތާވީސް
އަށާވީސް
ނަވާވީސް
ތިރީސް
ސާޅީސް
ފަންސާސް
ފަސްދޮޅަސް
ހަތްދިހަ
އައްޑިހަ
ނުވަދިހަ
ސަތޭކަ
ހާސް
މިލިޔަން
ބިލިޔަން
ޓްރލިއަން
ކުއަޑްރިލިޔަން
ގްޖިލިޔަން
ބަޒިލިޔަން
  """.split())

def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words:
        return True
    return False


LEX_ATTRS = {
    LIKE_NUM: like_num
}

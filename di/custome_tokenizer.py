

STOP_WORDS = ("""
ތަކަށްވެސް
ގައިވާ
ފައިވާ
ކަމާއި
މިއީ
އެވެ
ވެސް
އެ
ކަމަށް
މި	
އަދި	
ވަނީ
އަށް
ކަމަށެވެ
ގައި	
އިން
ގޮތުގައި
ތަކުގައި
އާއި
ވަނަ
އެއީ
ބައެއް
އެކު
ގޮތުން
ކަމެއް
ތެރޭގައި
ކުރިން
އޮތް
ފަހު
ހުރި
އެއް
އޭގެ
ފައި
އަންނަ
ކަމަށާއި
ކޮށް
ތައް
""".split())



def find_suffix(compound,suffixes =STOP_WORDS, ):
    for word in suffixes:
        if len(compound) > len(word) and word in compound:
            split = list(compound.partition(word))
            return split
            
 


text = "ދިމާކޮށް"
t = find_suffix(text)
print(text[:-t])

print(t)
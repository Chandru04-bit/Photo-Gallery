with open("gallery.html", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    'data-title="Princess Castle & Balloon Arches"',
    'data-title="Colourful Celebration Confetti Special"'
).replace(
    'alt="Princess Castle Theme"',
    'alt="Colourful Celebration Confetti Special"'
).replace(
    '<h5>Princess Castle Theme</h5>',
    '<h5>Celebration Confetti</h5>'
).replace(
    '<span>Birthday • Coimbatore</span>',
    '<span>Celebration Event • Coimbatore</span>'
)

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated gallery.html card 2 title to Celebration Confetti!")

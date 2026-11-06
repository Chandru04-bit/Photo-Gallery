with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'Pastel Chiffon & Neon Backdrop',
    'Floral Blossom Ring Engagement Stage'
).replace(
    'alt="Pastel Chiffon Backdrop"',
    'alt="Floral Blossom Ring Engagement Stage"'
).replace(
    '<h5>Pastel Chiffon Backdrop</h5>',
    '<h5>Floral Blossom Ring</h5>'
).replace(
    'Enchanted Jungle Safari Birthday',
    'Enchanted Garden Birthday Stage'
).replace(
    'alt="Enchanted Jungle Safari"',
    'alt="Enchanted Garden Birthday Stage"'
).replace(
    '<h5>Enchanted Safari Theme</h5>',
    '<h5>Enchanted Garden Theme</h5>'
)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated gallery.html successfully!')

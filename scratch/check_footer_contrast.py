with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

start = css.find("/* Footer")
if start != -1:
    print(css[start:start+1800])

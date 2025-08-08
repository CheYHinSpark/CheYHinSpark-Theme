# generate color panels
def rgb_to_hex(rgb_weight, base_step):
    r = rgb_weight[0] * base_step[1] + base_step[0]
    g = rgb_weight[1] * base_step[1] + base_step[0]
    b = rgb_weight[2] * base_step[1] + base_step[0]
    # RGB to hex
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


w_rgb = [[4,1,0],[4,3,0],[3,4,0],[1,4,0],[0,4,1],[0,4,3],
         [0,3,4],[0,1,4],[1,0,4],[3,0,4],[4,0,3],[4,0,1]]

base_and_step = [[32, 32],
                 [40, 40],
                 [50, 50],
                 [90, 40],
                 [122, 32],
                 [90, 25],
                 [90, 30],
                 [90, 36],
                 [120, 30],
                 [145, 25],]


length = 4
h = len(base_and_step) * length
w = len(w_rgb) * length

# writting svg file
file_content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<svg width=\"" + \
                str(w) + "\" height=\"" + str(h) + "\" viewbox=\"0 0 " + \
                str(w) + " " + str(h) + "\" xmlns=\"http://www.w3.org/2000/svg\">\n"

for x in range(len(w_rgb)):
    for y in range(len(base_and_step)):
        file_content += "<rect x=\"" + str(x * length) + "\" y=\"" + str(y * length) + \
                        "\" width=\"" + str(length) + "\" height=\"" + str(length) + \
                        "\" fill=\"" + rgb_to_hex(w_rgb[x], base_and_step[y]) + "\"/>\n"

file_content += "</svg>"

with open('color_panel.svg', 'w', encoding='utf-8') as file:
    file.write(file_content)

print(file_content)

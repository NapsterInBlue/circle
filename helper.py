from PIL import ImageDraw, Image

def draw_rectangle(color_list):
    '''
    Make a long rectangle, composed of the colors
    detailed in color_list, a list of (R, G, B) tuples
    '''
    n = len(color_list)

    im = Image.new('RGBA', (100*n, 100))
    draw = ImageDraw.Draw(im)

    for idx, color in enumerate(color_list):
        # ensure that numbers are all ints
        color = tuple([int(x) for x in color])
        
        # draw the colors by array-indexing
        draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))],
                       fill=tuple(color))

    return im
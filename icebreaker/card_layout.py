from matplotlib import pyplot as plt
import numpy as np
from bokeh import palettes
from bokeh import plotting as bkplt

def create_card(text, colour, title="", rows=1, cols=1, subplot=1):
    sbp = plt.subplot(rows, cols, subplot)
    plt.text(0.5, 0.5, text, 
    horizontalalignment='center', verticalalignment='center', 
    fontsize=80, color=colour, 
    bbox=dict(edgecolor=colour, facecolor=colour, alpha=0.25, pad=25))
    if title:
        plt.title(title, fontsize=25)
    sbp.axes.set_axis_off()

def layout_cards(data, group='', test=False, rows=5, cols=2, cards_per_page=10):
    _set = 1
    plt.figure(figsize=(8, 12))
    subplot_num=1
    for num, colour in data:
        if test:
            if group == '1':
                _key_char = list('135')[np.random.randint(3)]
            elif group == '2':
                _key_char = list('246')[np.random.randint(3)]
            _start_code = '%05x' % np.random.randint(16**6)
            _code = _start_code[0] + _key_char + _start_code[1:]
            create_card(str(num), colour, title=_code, rows=rows, cols=cols, subplot=subplot_num)
        else:
            create_card(str(num), colour, title=group, rows=rows, cols=cols, subplot=subplot_num)
        subplot_num += 1
        if subplot_num > cards_per_page:
            plt.subplots_adjust(top=0.95, bottom=0, hspace=0.25, wspace=0.5)
            if group:
                filename = group.replace(' ', '_') + '-' + str(_set) + '.svg'
            else:
                filename = 'cards-' + str(_set) + '.svg'
            plt.savefig(filename)
            _set += 1
            plt.figure(figsize=(8, 12))
            subplot_num=1
    plt.subplots_adjust(top=0.95, bottom=0, hspace=0.25, wspace=0.5)
    if group:
        filename = group.replace(' ', '_') + '-' + str(_set) + '.svg'
    else:
        filename = 'cards-' + str(_set) + '.svg'
    plt.savefig(filename)

n = 25
(g1mean, g1std)   = (33,16)
(g2mean, g2std)   = (67,16)
(g1ymean, g1ystd) = (2.5,1)
(g2ymean, g2ystd) = (6,1)

colours = ['#ff0000', '#dd0024', '#bb0048', '#91006d', 
           '#6d0091', '#4800bb', '#2400dd', '#0000ff']

group1_x = np.array([int(x) for x in np.random.normal(g1mean, g1std, size=n)])
group2_x = np.array([int(x) for x in np.random.normal(g2mean, g2std, size=n)])
group1_y = np.array([abs(int(x)) for x in np.random.normal(g1ymean, g1ystd, size=n)])
group2_y = np.array([abs(int(x)) for x in np.random.normal(g2ymean, g2ystd, size=n)])
g1_colour_picks = [colours[i] for i in group1_y]
g2_colour_picks = [colours[i] for i in group2_y]
g1 = zip(group1_x, g1_colour_picks)
g2 = zip(group2_x, g2_colour_picks)

layout_cards(g1, group='Group 1')
layout_cards(g2, group='Group 2')

test1_x = np.array([int(x) for x in np.random.normal(g1mean, g1std, size=n)])
test2_x = np.array([int(x) for x in np.random.normal(g2mean, g2std, size=n)])
test1_y = np.array([abs(int(x)) for x in np.random.normal(g1ymean, g1ystd, size=n)])
test2_y = np.array([abs(int(x)) for x in np.random.normal(g2ymean, g2ystd, size=n)])
t1_colour_picks = [colours[i] for i in test1_y]
t2_colour_picks = [colours[i] for i in test2_y]
t1 = zip(test1_x, t1_colour_picks)
t2 = zip(test2_x, t2_colour_picks)

layout_cards(t1, '1', test=True)
layout_cards(t2, '2', test=True)

fig3 = bkplt.figure(title='HUB data', tools='', toolbar_location=None, y_range=colours, x_range=[0,100])
fig3.circle(group1_x, g1_colour_picks, color='#00ff00')
fig3.circle(group2_x, g2_colour_picks, color='#0000ff')
fig3.triangle(test1_x, t1_colour_picks, color='#00ff00')
fig3.triangle(test2_x, t2_colour_picks, color='#0000ff')
bkplt.show(fig3)
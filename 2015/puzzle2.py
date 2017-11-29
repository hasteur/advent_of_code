
def paper_sizing(length, width, height):
    """
        Figure out how much paper is needed using formula:
        2(lw + wh + hl) + min(lw,wh,hl)
        @length - Length of box
        @width - Width of box
        @height - height of box
    """
    lw = length*width
    wh = width*height
    hl = height*length
    return 2*(lw+wh+hl)+min(lw,wh,hl)
def ribbon_length(length,width,height):
    """
        Figure out how much ribbon is needed using the formula:
        (l*w*h)+2(l+w+h -max(l,w,h))
        @length - Length of box
        @width - Width of box
        @height - height of box
    """
    return (length*width*height)+2*(length+width+height - max(length,width,height))
total_paper = 0
total_ribon = 0
fh = open('puzzle2.txt','r')
for line in fh:
    (l,w,h) = line.split('x')
    total_paper += paper_sizing(int(l),int(w),int(h))
    total_ribon += ribbon_length(int(l),int(w),int(h))
    
print "Total Paper: %i" % total_paper
print "Total Ribon: %i" % total_ribon

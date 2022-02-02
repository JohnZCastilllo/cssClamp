# visit this link for more
# https://www.aleksandrhovhannisyan.com/blog/fluid-type-scale-with-css-clamp/

def calculate(maxF,minF,maxB,minB):
    
    # m for the viewport width
    # b for the constant added to m
    
    m = (maxF - minF) / (maxB - minB)
    b = minF - (m * minB)
    
    print(m)
    #checking if correct result
    #note use result that have not been converted
    print('Correct for min: ',m*minB+b == minF)
    print('Correct for max: ',m*maxB+b == maxF)
    

    b = round(b,2)
    m = round(m*100,2)

    # print integer value
    print("clamp(%dpx, %svw + %dpx, %dpx)" % (minF,m,b,maxF))
    
#max font, min font, max Breakpoint, minimum breakpoint
calculate(17,10,1440,375)

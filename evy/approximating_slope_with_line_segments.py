// click Run

// setup grid
origin_x := 10
origin_y := 10
scale := 10
xmin := (0 - origin_x) / scale
xmax := (100 - origin_x) / scale
ymin := (0 - origin_y) / scale
ymax := (100 - origin_y) / scale
gridn 10 "grey"
draw_axes false

color "green"
draw_x_squared_function

step := 0.001
for y := range 0 10 step
    from_x := sqrt (y)
    to_x := sqrt (y + step)
    line_btw_coords from_x y to_x y+step "red"
end

func draw_x_squared_function
    for x := range xmin xmax 0.01
        y := x * x
        plot x y
    end
end

func plot x:num y:num
    move origin_x+x*scale origin_y+y*scale
    circle 0.1
end

func zoom_graph from:num to:num
    clear
    scale = 80 / (to - from)
    origin_x = 10
    origin_y = 10
    xmin = from
    xmax = to
    ymin = from
    ymax = to
    gridn 10 "grey"
    draw_axes true
end

// draws a line converting our graph coords to evy canvas coords
// also draws the lines for the x and y components
func line_btw_coords x1:num y1:num x2:num y2:num col:string
    // draw desired line
    width 0.5
    color col
    move origin_x+x1*scale origin_y+y1*scale
    line origin_x+x2*scale origin_y+y2*scale

    // draw x component
    width 0.25
    color "grey"
    move origin_x+x1*scale origin_y+y1*scale
    line origin_x+x2*scale origin_y+y1*scale
    // draw y component
    line origin_x+x2*scale origin_y+y2*scale
end

func draw_axes zoom:bool
    width 0.5
    move 0 origin_y
    line 100 origin_y
    move origin_x 0
    line origin_x 100

    font {size:5 align:"center" baseline:"middle"}
    move origin_x origin_y
    if !zoom
        text "0"
    end

    // print x-axis numbers
    for i := range xmin xmax+1 1/scale*10
        if i != 0
            if zoom
                move origin_x+i*scale-xmin*scale origin_y-3
            else
                move origin_x+i*scale origin_y-3
            end
            label := sprint i
            text label
        end
    end

    // print y-axis numbers
    for i := range ymin ymax+1 1/scale*10
        if i != 0
            if zoom
                move origin_x-3 origin_y+i*scale-ymin*scale
            else
                move origin_x-3 origin_y+i*scale
            end
            label := sprint i
            text label
        end
    end
end


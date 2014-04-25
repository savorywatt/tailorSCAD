use<sphere.scad>

translate([-100, 0, 0])
import("./bin/sphere.stl");

translate([100, 0, 0])
import("./bin/cube.stl");


cube_width = 100;

simple_sphere(cube_width);

tailorSCAD
==========

A modest library to attempt to build SCAD based projects using configuration files.

A general overview is here

https://www.youtube.com/watch?v=XYstpSbyPak

The basic flow is

config A builds object A
config B uses object A when it builds Object B
config C uses A & B to build C etc.

You define a config file that allows your openscad files to be 'rendered' and then used elsewhere. Each config file also allows for optional parameters to be injected while you are rendering. This allows you to create small objects and then render them to STL using configurable parameters based on a defined config file. So, if you are using 3 different scad files in different repositories you can have a single config in one repository that will build STLs from the other repository and then make those stl's available to you in your repo, even if those files have conflicting variable names (an issue if you bring those scripts into your local project.

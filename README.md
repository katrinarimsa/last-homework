# Final assignment
## Situation description 
Final year mechanical engineering student Artyom had a challenging day today. For his bachelor thesis, he had to execute
a tensile test experiment on a tin (Sn) sample. Unfortunately, the tensile test machine data system was dysfunctional and
was not able to obtain and analyze the data automatically. Thus, Artyom's only option was to gather the data and perform the appropriate 
analysis manually. Due to a possible human error, Artyom repeated the experiment 3 times and gathered 18 measurements. 
His main task now is to plot a stress-strain curve using the obtained data. Let's make his life easier and develop a code 
that plots the curve for him.  
Plot requirements:
1) Asks for user input
2) Make sure the user has provided only positive numbers (if-statement)
3) Sorts the data in ascending order (loop)
4) Considers the second value for each point
5) Measurements are in a class
6) Plotting the graph as a method in class
7) Pytest for sorting and positive number functions is implemented

## The project description  
The project asks for the user input of the yield stress and strain, tensile stress and strain and fracture 
stress and strain values from three experiments. Then, after verifying that all input is positive, it sorts the data and 
plots the stress-strain curve (strain (in mm) - independent, stress (in MPa) - dependent). In the plotted graph, material's 
deformation in response to a tensile, compressive, or torsional load is represented. 
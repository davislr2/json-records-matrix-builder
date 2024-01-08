# json-records-matrix-builder
Python solution for generating a head-to-head records matrix from a JSON file containing sports teams' Win-Loss records.  Developed as part of an engineering internship prompt for Sports Reference."

The json_to_matrix method takes in a json file object, creates an empty 2D dict keyed on the team names, and uses a nested for loop to add the wins for each team against every other. 

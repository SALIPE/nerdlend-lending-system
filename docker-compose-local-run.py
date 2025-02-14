import re

# Input file and output file paths
input_file = "docker-compose.yml"
output_file = "docker-compose-updated.yml"

def uncomment_build_sections(input_path, output_path):
    with open(input_path, "r") as file:
        lines = file.readlines()
    
    uncommented_lines = []
    inside_build_section = False
    
    for line in lines:
        stripped_line = line.lstrip()
        
        # Check if the current line starts a build section
        if stripped_line.startswith("# build:"):
            uncommented_lines.append(line.replace("# ", "", 1))
            inside_build_section = True
        # Check if we are in a build section and encounter a context line
        elif inside_build_section and stripped_line.startswith("#   context:"):
            uncommented_lines.append(line.replace("# ", "", 1))
            inside_build_section = False
        else:
            uncommented_lines.append(line)
            inside_build_section = False  # Ensure to reset if not part of the section

    # Write the updated content to the output file
    with open(output_path, "w") as file:
        file.writelines(uncommented_lines)

    print(f"Uncommented build sections written to {output_path}")

# Execute the function and run docker-compose
uncomment_build_sections(input_file, output_file)

import os
os.system(f"docker compose -f {output_file} up --build")

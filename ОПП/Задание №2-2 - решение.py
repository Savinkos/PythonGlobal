def merge_files(files, output_file):
    file_contents = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            file_contents.append((file, len(lines), lines))
    
    file_contents.sort(key=lambda x: x[1])
    
    with open(output_file, 'w') as out:
        for file_name, line_count, lines in file_contents:
            out.write(f"{file_name}\n")
            out.write(f"{line_count}\n")
            out.writelines(lines)
            out.write("\n")  

files_to_merge = ["1.txt", "2.txt", "3.txt"]
output_file_path = "result.txt"
merge_files(files_to_merge, output_file_path)

# Walk through all directories
for root, dirs, files in os.walk(os.getcwd()):
    
    # Look through each file
    for file in files:
        
        # Check if the filename is secret.txt
        if file=='secret.txt':
        
            # Print the file contents
            with open(os.path.join(root,file)) as f:
                
                print(f.read())

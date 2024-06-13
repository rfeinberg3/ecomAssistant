import os

if __name__ == '__main__':
    
    # Path to data files
    data_dir = os.path.join('..', 'DataScraper', 'outputs')

    for file_path in os.listdir(data_dir):
        if file_path.endswith('.json'):
            old_file_path = os.path.join(data_dir, file_path)
            
            # Define the new filename (modify as needed)
            new_filename = file_path.replace(' ', '_')
            new_filename = new_filename.replace('\n', '')
            
            new_file_path = os.path.join(data_dir, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
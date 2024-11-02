import os
import shutil

# Folder paths
txtp_folder = r"PATH TO .TXTP FILES"
source_wem_folder = r" PATH TO YOUR GAME DUMP\Client\Content\Aki\WwiseAudio_Generated\Media\en"
destination_wem_folder = r"PATH OF DESTINATION"

# Create the destination folder if it doesn't exist
os.makedirs(destination_wem_folder, exist_ok=True)

# Iterate through each .txtp file in the txtp_folder
for txtp_file in os.listdir(txtp_folder):
    if txtp_file.endswith(".txtp"):
        txtp_path = os.path.join(txtp_folder, txtp_file)

        # Get the first line of the txtp file
        with open(txtp_path, 'r') as file:
            first_line = file.readline().strip()
        
        # Extract the .wem file name
        if first_line.startswith("wem/"):
            wem_name = first_line.split(" ")[0].replace("wem/", "")
            wem_source_path = os.path.join(source_wem_folder, wem_name)

            # Destination path with the txtp file name (without the .txtp extension)
            wem_dest_path = os.path.join(destination_wem_folder, f"{os.path.splitext(txtp_file)[0]}.wem")
            
            # Copy the wem file, renaming it
            if os.path.exists(wem_source_path):
                shutil.copy2(wem_source_path, wem_dest_path)
                print(f"Copied: {wem_source_path} to {wem_dest_path}")
            else:
                print(f".wem file not found: {wem_source_path}")
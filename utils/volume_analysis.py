import nibabel as nib
import numpy as np
import os

def calculate_volume(nifti_file):
    """Calculate the volume of a structure from a NIFTI file"""
    try:
        img = nib.load(nifti_file)
        data = img.get_fdata()
        # Count non-zero voxels and multiply by voxel dimensions
        voxel_volume = np.prod(img.header.get_zooms())
        print(img.header.get_zooms())
        return np.sum(data > 0) * voxel_volume
    except (FileNotFoundError, nib.filebasedimages.ImageFileError) as e:
        print(f"Error loading {nifti_file}: {e}")
        return 0
    

def get_nifti_path(volume_num, organ):
    """Construct path to NIFTI file based on volume number and organ type"""
    filename = f"volume_{volume_num}"
    if organ.lower() == 'lung':
        return f"../output/{filename}/{filename}_Auto_Lung.nii.gz"
    elif organ.lower() == 'heart':
        return f"../output/{filename}/{filename}_Heart.nii.gz"
    else:
        raise ValueError(f"Unsupported organ type: {organ}")

def compare_volumes(volume_numbers, organ_type, threshold_pct=1.0, output_file="None"):
    """
    Compare organ volumes across different scans
    
    Args:
        volume_numbers: List of volume numbers to compare
        organ_type: Type of organ ('heart', 'lung', or ['heart', 'lung'] for both)
        threshold_pct: Threshold percentage for logging differences
        output_file: File to write results when difference is below threshold
    """
    if not volume_numbers or len(volume_numbers) < 1:
        print("Error: Need at least one volume number to analyze")
        return

    # Convert single organ string to list for uniform processing
    if isinstance(organ_type, str):
        organ_types = [organ_type]
    else:
        organ_types = organ_type
    
    # Print combined header if analyzing multiple organs
    if len(organ_types) > 1:
        print(f"--- Analysis for {' and '.join([org.capitalize() for org in organ_types])} ---")
    elif len(organ_types) == 1:
        print(f"--- Analysis for {organ_types[0].capitalize()} ---")
    
    # Initialize data structure to store volumes
    all_results = {vol: {} for vol in volume_numbers}
    
    # Calculate volumes for each scan and organ
    for organ in organ_types:
        for vol_num in volume_numbers:
            nifti_file = get_nifti_path(vol_num, organ)
            volume = calculate_volume(nifti_file)
            all_results[vol_num][organ] = volume
    
    # Print volumes grouped by volume number
    for vol_num in volume_numbers:
        print(f"Volume {vol_num}:")
        for organ in organ_types:
            print(f"{organ.capitalize()} volume: {all_results[vol_num][organ]:.2f} cubic mm")

    # Compare differences between scans
    if len(volume_numbers) > 1:
        for i in range(len(volume_numbers)):
            for j in range(i + 1, len(volume_numbers)):
                vol1, vol2 = volume_numbers[i], volume_numbers[j]
                print(f"Difference between volume_{vol1} and volume_{vol2}:")
                
                for organ in organ_types:
                    volume_diff = all_results[vol2][organ] - all_results[vol1][organ]
                    
                    # Avoid division by zero
                    if all_results[vol1][organ] == 0:
                        percent_change = float('inf')
                    else:
                        percent_change = (volume_diff/all_results[vol1][organ])*100
                    
                    print(f"{organ.capitalize()} volume change: {volume_diff:.2f} cubic mm ({percent_change:.2f}%)")
                    
                    # Log significant differences based on threshold
                    if output_file != "None":
                        if abs(percent_change) < threshold_pct:
                            TempList.append(vol2)
                            organ_output_file = f"{organ}_{output_file}" if len(organ_types) > 1 else output_file
                            with open(organ_output_file, 'a') as f:
                                # f.write(f"Volume difference between volume_{vol1} and volume_{vol2} is less than {threshold_pct}%\n")
                                # f.write(f"{organ.capitalize()} volume change: {volume_diff:.2f} cubic mm ({percent_change:.2f}%)\n\n")
                                f.write(f"volume_{vol1} and volume_{vol2} difference: {percent_change:.2f}%\n")
                    
            print()

def record_volume_size(vol_num, organ, output_file="volume_sizes.txt"):
    """Record the volume of an organ to a text file"""
    nifti_file = get_nifti_path(vol_num, organ)
    # Calculate the volume using the existing function
    volume = calculate_volume(nifti_file)
    
    # Write the volume information to the text file
    with open(output_file, 'a') as f:
        f.write(f"{organ}_volume_{vol_num}: {volume:.2f} cubic mm\n")

if __name__ == "__main__":
    
    TempList = []
    same_lung_list_volume_12  = [11, 21, 22, 30, 31, 40, 41, 51, 52, 60, 70, 100, 101, 110, 122, 132, 140, 150, 171, 173]
    same_heart_list_volume_12 = [1, 11, 12, 21, 22, 30, 31, 40, 41, 52, 60, 81, 82, 100, 101, 122, 130, 132, 141, 143, 150, 151, 160, 161, 162, 171, 172, 173]
    
    same_lung_list_volume_18  = [6, 7, 8, 15, 16, 18, 28, 34, 35, 36, 44, 45, 46, 64, 95, 96, 107, 116, 117, 135, 137, 145, 146, 147, 154, 155, 156, 164, 165, 166, 167, 177]
    same_heart_list_volume_18 = [4, 5, 6, 7, 17, 18, 25, 26, 27, 28, 34, 35, 36, 37, 48, 58, 66, 67, 77, 78, 88, 89, 96, 97, 104, 105, 106, 107, 116, 117, 135, 136, 137, 147, 148, 155, 166, 167, 176, 177]

    # for i in same_lung_list_volume_18:
        # compare_volumes([18, i], 'heart',  100, 'heart_volume_analysis.txt')
        # compare_volumes([18, i], 'lung', 1, 'lung_volume_analysis.txt')
    
    # for i in range(1, 182):
        # compare_volumes([18, i], 'heart', 100.0, 'heart_volume_analysis.txt')
        # compare_volumes([18, i], 'lung', 100.0, 'lung_volume_analysis.txt')
        # record_volume_size(i,'heart', 'heart_volume_sizes.txt')
        # record_volume_size(i,'lung', 'lung_volume_sizes.txt')

    # compare_volumes([12, 18], 'lung')

    # print(calculate_volume(get_nifti_path(18, 'lung')))

    # print(TempList)

    print(calculate_volume('./Testing/20xsphere.nii.gz'))

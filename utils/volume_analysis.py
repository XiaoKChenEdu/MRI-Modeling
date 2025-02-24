import nibabel as nib
import numpy as np

def calculate_volume(nifti_file):
    """Calculate the volume of a structure from a NIFTI file"""
    img = nib.load(nifti_file)
    data = img.get_fdata()
    # Count non-zero voxels and multiply by voxel dimensions
    voxel_volume = np.prod(img.header.get_zooms())
    return np.count_nonzero(data) * voxel_volume

def compare_volumes(volume_numbers):
    results = {}
    
    for vol_num in volume_numbers:
        filename = f"volume_{vol_num}"
        heart_file = f"../output/{filename}/{filename}_Heart.nii.gz"
        lung_file = f"../output/{filename}/{filename}_Auto_Lung.nii.gz"
        
        heart_volume = calculate_volume(heart_file)
        lung_volume = calculate_volume(lung_file)
        
        results[vol_num] = {
            'heart': heart_volume,
            'lung': lung_volume
        }
        
        print(f"\nVolume {vol_num}:")
        print(f"Heart volume: {heart_volume:.2f} cubic mm")
        print(f"Lung volume: {lung_volume:.2f} cubic mm")
    
    # Compare differences
    if len(volume_numbers) > 1:
        print("\nVolume differences between scans:")
        for i in range(len(volume_numbers)):
            for j in range(i + 1, len(volume_numbers)):
                vol1, vol2 = volume_numbers[i], volume_numbers[j]
                heart_diff = results[vol2]['heart'] - results[vol1]['heart']
                lung_diff = results[vol2]['lung'] - results[vol1]['lung']
                
                print(f"\nDifference between volume_{vol2} and volume_{vol1}:")
                print(f"Heart volume change: {heart_diff:.2f} cubic mm ({(heart_diff/results[vol1]['heart']*100):.2f}%)")
                print(f"Lung volume change: {lung_diff:.2f} cubic mm ({(lung_diff/results[vol1]['lung']*100):.2f}%)")

if __name__ == "__main__":
    volume_numbers = [18, 12]  # Added a third volume number
    compare_volumes(volume_numbers)

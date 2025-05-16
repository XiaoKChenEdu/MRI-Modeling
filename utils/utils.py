from vedo import show, Volume
import nibabel as nib
import matplotlib.pyplot as plt

def visualize_mri_3d(data, filename, slice=0, timeseries=True, bg='white'):
    """
    Visualize 3D MRI data using interactive volume rendering.
    This function creates a 3D visualization of MRI data using the Volume renderer.
    It handles both 3D volumes and 4D timeseries data.
    Parameters
    ----------
    data : numpy.ndarray
        Input MRI data array. Can be 3D (volume) or 4D (timeseries) array
    filename : str
        Name of the file/title to display on visualization
    slice : int, optional
        For 4D data, specifies which slice to visualize in timeseries mode (default is 0)
    timeseries : bool, optional
        If True, visualizes 4D data as timeseries of selected slice
        If False, visualizes first timepoint of all slices (default is True)
    bg : str, optional
        Background color for visualization (default is 'black')
    """
    if len(data.shape) == 3:
        title = f'{filename}'
        vol = Volume(data, spacing=xyzspacing)
    else:
        if timeseries is False:
            timepoint = int(input(f"Enter the timepoint (0-{data.shape[3]-1}): "))
            while timepoint < 0 or timepoint >= data.shape[3]:
                print(f"Invalid timepoint. Please enter a number between 0 and {data.shape[3]-1}")
                timepoint = input(f"Enter the timepoint (0-{data.shape[3]-1}): ")
            title = f'{filename} All Slice at Time {timepoint}'
            vol = Volume(data[:,:,:,timepoint], spacing=(1,1,3))
        else:
            title = f'{filename} Slice {slice}'
            vol = Volume(data[:,:,slice,:], spacing=(1,1,3))
    
    show(vol, bg=bg, title=title)

    return 0
    
def visualize_mri(data, filename, slice=0, timeseries=True):
    """
    Visualizes 3D or 4D MRI data as an animated sequence.
    This function creates an animated visualization of MRI data, handling both 3D
    (x, y, time) and 4D (x, y, slice, time) data formats. It can display either
    time series data for a specific slice or spatial slices at a fixed time point.
    Parameters
    ----------
    data : numpy.ndarray
        3D or 4D array containing MRI data
        For 3D: dimensions should be (x, y, time)
        For 4D: dimensions should be (x, y, slice, time)
    filename : str
        Base filename used for saving the animation and display purposes
    slice : int, optional
        Slice number to visualize in 4D data when viewing time series (default=0)
    timeseries : bool, optional
        If True, displays temporal evolution of a single slice (default=True)
        If False, displays spatial slices at a fixed time point
    """
    import matplotlib.animation as animation
    
    fig = plt.figure()
    ims = []

    if len(data.shape) == 3:
        savefilename = filename
        for t in range(data.shape[2]):
            im = plt.imshow(data[:, :, t], cmap='gray', animated=True)
            plt.title(f'{filename} Time 0-{t}')
            ims.append([im])
    else:
        if timeseries is False:
            savefilename = filename
            timepoint = int(input(f"Enter the timepoint (0-{data.shape[3]-1}): "))
            while timepoint < 0 or timepoint >= data.shape[3]:
                print(f"Invalid timepoint. Please enter a number between 0 and {data.shape[3]-1}")
                timepoint = input(f"Enter the timepoint (0-{data.shape[3]-1}): ")
            for t in range(data.shape[2]):
                im = plt.imshow(data[:, :, t, timepoint], cmap='gray', animated=True)
                plt.title(f'{filename} Time{timepoint} Slice 0-{t}')
                ims.append([im])
        else:
            savefilename = f'{filename}_slice{slice}' 
            for t in range(data.shape[3]):
                im = plt.imshow(data[:, :, slice, t], cmap='gray', animated=True)
                plt.title(f'{filename} Slice{slice} Time 0-{t}')
                ims.append([im])
    
    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)
    savegif = True if input("Save as gif (y/n)? ").lower() == 'y' else False
    if savegif:
        ani.save(f'{savefilename}.gif', writer='pillow')
        print(f'GIF saved as {savefilename}.gif')
    plt.show()

    return 0

def extract_and_save_3d_slice(data, filename, slice):
    """
    Extract and save 3D slice(s) from a 4D MRI data array as NIfTI file(s).
    This function takes a 4D data array from an MRI scan and either extracts 
    a single 3D slice or all slices, saving them as new NIfTI files.
    
    Parameters
    ----------
    data : numpy.ndarray
        4D array containing MRI data with dimensions (x, y, slice, time)
    filename : str
        Base filename for the output NIfTI file(s) (without extension)
    slice : int
        Index of the slice to extract when not extracting all slices
    """
    extract_all = False if input("Extract all slices (y/n)? ").lower() == 'n' else True
    
    if extract_all:
        for s in range(data.shape[2]):
            data_3d = data[:, :, s, :]
            new_img = nib.Nifti1Image(data_3d, img.affine)
            nib.save(new_img, f"{filename}_3d_slice{s}.nii.gz")
            print(f"3D slice {s} saved as {filename}_3d_slice{s}.nii.gz")
    else:
        data_3d = data[:, :, slice, :]
        new_img = nib.Nifti1Image(data_3d, img.affine)
        nib.save(new_img, f"{filename}_3d_slice{slice}.nii.gz")
        print(f"3D slice saved as {filename}_3d_slice{slice}.nii.gz")

    return 0

if __name__ == "__main__":

    filename = input("Enter the filename: ")
    path_nifti = f"{filename}.nii.gz"
    
    img = nib.load(path_nifti)
    data = img.get_fdata()
    xyzspacing = img.header.get_zooms()
    
    if len(data.shape) == 4:
        timeseries = False if input("View by time series (y/n)? ").lower() == 'n' else True
        
        if timeseries is True:
            slice = int(input(f"Enter the slice number (0-{data.shape[2]-1}): "))
            while slice < 0 or slice >= data.shape[2]:
                print(f"Invalid slice number. Please enter a number between 0 and {data.shape[2]-1}")
                slice = int(input(f"Enter the slice number (0-{data.shape[2]-1}): "))
        
        print("Choose an option:")
        print("1. Visualize MRI")
        print("2. Visualize 3D MRI")
        print("3. Extract and save 3D slice")
        option = int(input("Enter option (1-3): "))
        while option not in [1, 2, 3]:
            print("Invalid option. Please choose 1-3")
            option = int(input("Enter option (1-3): "))
    else :
        print("Choose an option:")
        print("1. Visualize MRI")
        print("2. Visualize 3D MRI")
        option = int(input("Enter option (1-2): "))
        timeseries = True
        while option not in [1, 2]:
            print("Invalid option. Please choose 1-2")
            option = int(input("Enter option (1-2): "))

    if option == 1:
        visualize_mri(data, filename, slice, timeseries)
    elif option == 2:
        visualize_mri_3d(data, filename, slice, timeseries)
    elif option == 3:
        extract_and_save_3d_slice(data, filename, slice)
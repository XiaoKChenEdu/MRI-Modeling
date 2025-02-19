from vedo import show, Volume, Text2D
import nibabel as nib
import os

# Define a list of 20 visually distinguishable colors
COLORS_20 = [
    'red', 'blue', 'green', 'yellow', 'purple',
    'cyan', 'orange', 'magenta', 'brown', 'pink',
    'gold', 'lightgreen', 'navy', 'coral', 'violet',
    'turquoise', 'salmon', 'olive', 'skyblue', 'maroon'
]

def visualize_mri_3d_mesh(mri_files, colors=None):
    """
    Visualize multiple MRI files in the same 3D plot using isosurfaces
    mri_files: list of file paths
    colors: list of colors for each structure
    """
    if colors is None:
        colors = ['red', 'blue', 'green']
    
    volumes = []
    # Create legend text
    legend_text = ""
    
    for file, color in zip(mri_files, colors):
        img = nib.load(file)
        data = img.get_fdata()
        vol = Volume(data, spacing=(1,1,3))
        mesh = vol.isosurface(0.5)
        mesh.smooth(niter=20)
        mesh.color(color)
        mesh.alpha(0.6)
        volumes.append(mesh)
        # Add to legend text
        structure_name = os.path.splitext(os.path.basename(file))[0]
        legend_text += f"{structure_name}: {color}\n"
    
    # Create legend using Text2D
    legend = Text2D(legend_text, pos='top-right', c='white', bg='black', alpha=0.8, font='Arial')
    volumes.append(legend)
    
    show(volumes, bg='black', axes=1)
    
def print_info(mri_file, patient_name):
    img = nib.load(mri_file)
    data = img.get_fdata()
    print(f'{patient_name} : {data.shape}')

if __name__ == "__main__":

    filename = "volume_0"
    folder_path = f"./output/{filename}"
    mri_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.nii.gz') and f.startswith(filename)]
    
    colors = COLORS_20[:len(mri_files)]
    
    # for file in mri_files:
    #     print_info(file, os.path.basename(file))
    
    visualize_mri_3d_mesh(mri_files, colors)

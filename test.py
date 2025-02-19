from vedo import show, Volume, Text2D, Plotter
import nibabel as nib
import imageio.v2 as imageio
import glob
import os

def create_mri_3d_gif():
    colors = ['red', 'yellow']
    
    frames = []
    for i in range(12, 19):
        filename = f"volume_{i}"
        path_nifti_heart = f"./output/{filename}/{filename}_Heart.nii.gz"
        path_nifti_lung = f"./output/{filename}/{filename}_Auto_Lung.nii.gz"
        
        mri_files = [path_nifti_heart, path_nifti_lung]
        volumes = []
        for file, color in zip(mri_files, colors):
            img = nib.load(file)
            data = img.get_fdata()
            vol = Volume(data, spacing=(1,1,3))
            mesh = vol.isosurface(0.5)
            # mesh.rotate(angle=-90, axis=(0,0,1))  # Rotate axis = (x, y, z)
            mesh.smooth(niter=20)
            mesh.color(color)
            mesh.alpha(0.6)
            volumes.append(mesh)    
        
        # Render the scene and capture the frame
        plt = Plotter(offscreen=True, axes=1)
        txt = Text2D(f"Volume {i}", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
        plt.show(volumes + [txt], bg='black', interactive=False, elevation=-90)
        plt.screenshot(f'frame_{i:03d}.png')
        plt.clear()
        volumes.clear()
    
    # Create GIF from the saved frames
    
    frames = []
    for filename in sorted(glob.glob('frame_*.png')):
        frames.append(imageio.imread(filename))
    
    imageio.mimsave('mri_visualization.gif', frames, duration=1000, loop=0)
    
    # Clean up temporary files
    for filename in glob.glob('frame_*.png'):
        os.remove(filename)

def visualize_mri_3d_mesh(mri_files, colors=None):
    """
    Visualize multiple MRI files in the same 3D plot using isosurfaces
    mri_files: list of file paths
    colors: list of colors for each structure
    """
    if colors is None:
        colors = ['red', 'blue', 'green']
    
    volumes = []
    for file, color in zip(mri_files, colors):
        img = nib.load(file)
        data = img.get_fdata()
        # Set spacing to (x,y,z) for x y z mm in different directions
        vol = Volume(data, spacing=(1,1,3))
        mesh = vol.isosurface(0.5)  # Value between 0 and 1
        mesh.smooth(niter=20)  # Smooth the surface
        mesh.color(color)
        mesh.alpha(0.6)  # Set transparency
        volumes.append(mesh)
    
    show(volumes, bg='black', axes=1, elevation=-90)
    volumes.clear()
    
def print_info(mri_file, patient_name):
    img = nib.load(mri_file)
    data = img.get_fdata()
    print(f'{patient_name} : {data.shape}')

if __name__ == "__main__":

    # filename = "volume_90"

    # path_nifti_heart = f"./output/{filename}/{filename}_Heart.nii.gz"
    # path_nifti_lung = f"./output/{filename}/{filename}_Auto_Lung.nii.gz"
    
    # mri_files = [path_nifti_heart, path_nifti_lung]
    # colors = ['red', 'yellow'] 

    # visualize_mri_3d_mesh(mri_files, colors)

    create_mri_3d_gif()
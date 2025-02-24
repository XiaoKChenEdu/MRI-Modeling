from vedo import Volume, Text2D, Plotter
import nibabel as nib
import imageio.v2 as imageio
import glob
import os

def create_mri_3d_gif():
    colors = ['red', 'yellow']
    
    frames = []
    for i in range(12, 19):
        filename = f"volume_{i}"
        path_nifti_heart = f"../output/{filename}/{filename}_Heart.nii.gz"
        path_nifti_lung = f"../output/{filename}/{filename}_Auto_Lung.nii.gz"
        
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
        plt.screenshot(f'../img/frame_{i:03d}.png')
        plt.clear()
        volumes.clear()
    
    # Create GIF from the saved frames
    
    frames = []
    for filename in sorted(glob.glob('../img/frame_*.png')):
        frames.append(imageio.imread(filename))
    
    imageio.mimsave('../img/mri_visualization.gif', frames, duration=1000, loop=0)
    
    # Clean up temporary files
    for filename in glob.glob('../img/frame_*.png'):
        os.remove(filename)

if __name__ == "__main__":

    create_mri_3d_gif()
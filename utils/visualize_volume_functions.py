from vedo import Volume, Plotter, Text2D, merge
import nibabel as nib

def visualize_skin(volume_path):
    """
    Create a 3D visualization of the body outline using Plotter
    Args:
        volume_path: path to the .nii.gz file
    """
    # Load the volume
    img = nib.load(volume_path)
    data = img.get_fdata()
    
    # Normalize the data to 0-1 range
    data = (data - data.min()) / (data.max() - data.min())
    
    # Create volume with appropriate spacing
    vol = Volume(data, spacing=(1,1,3))
    
    # Create isosurface mesh
    mesh = vol.isosurface(0.1) # 0.1 is the threshold value for showing the skin
    mesh.smooth(niter=20)
    mesh.color('wheat')
    mesh.alpha(0.9)
    
    # Create plotter instance with proper lighting
    plt = Plotter(bg='black', size=(1000, 800), axes=1)
    txt = Text2D("MRI Visualization", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
    plt.add([mesh, txt])
    
    # Set camera position
    plt.camera.Elevation(-90)
    plt.camera.Azimuth(0)
    
    # Show the visualization with default lighting
    plt.show(interactive=True)
    

def visualize_bone(volume_path):
    """
    Create a 3D visualization of the body outline using Plotter
    Args:
        volume_path: path to the .nii.gz file
    """
    # Load the volume
    img = nib.load(volume_path)
    data = img.get_fdata()
    
    # Normalize the data to 0-1 range
    data = (data - data.min()) / (data.max() - data.min())
    
    # Create volume with appropriate spacing
    vol = Volume(data, spacing=(1,1,3))
    
    # Create isosurface mesh
    mesh = vol.isosurface(0.75) # 0.75 is the threshold value for showing the bones
    mesh.smooth(niter=20)
    mesh.color('wheat')
    mesh.alpha(0.9)
    
    # Create plotter instance with proper lighting
    plt = Plotter(bg='black', size=(1000, 800), axes=1)
    txt = Text2D("MRI Visualization", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
    plt.add([mesh, txt])
    
    # Set camera position
    plt.camera.Elevation(-90)
    plt.camera.Azimuth(0)
    
    # Show the visualization with default lighting
    plt.show(interactive=True)
    

def visualize_heart_lung(heart_path, lung_path):
    """
    Create a 3D visualization of the heart and lungs
    Args:
        heart_path: path to the heart segmentation .nii.gz file
        lung_path: path to the lung segmentation .nii.gz file
    """
    # Load the volumes
    heart_img = nib.load(heart_path)
    lung_img = nib.load(lung_path)
    
    # Get data
    heart_data = heart_img.get_fdata()
    lung_data = lung_img.get_fdata()
    
    # Create volumes
    heart_vol = Volume(heart_data, spacing=(1,1,3))
    lung_vol = Volume(lung_data, spacing=(1,1,3))
    
    # Create meshes
    heart_mesh = heart_vol.isosurface(0.5)
    lung_mesh = lung_vol.isosurface(0.5)
    
    # Apply styling
    heart_mesh.smooth(niter=20).color('red').alpha(0.8)
    lung_mesh.smooth(niter=20).color('pink').alpha(0.6)
    
    # Create plotter
    plt = Plotter(bg='black', size=(1000, 800), axes=1)
    txt = Text2D("MRI Visualization", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
    plt.add([heart_mesh, lung_mesh, txt])
    
    # Set camera
    plt.camera.Elevation(-90)
    plt.camera.Azimuth(0)
    
    plt.show(interactive=True)

def visualize_skin_heart_lung(volume_path, heart_path, lung_path):
    """
    Create a 3D visualization of the body outline, heart, and lungs
    Args:
        volume_path: path to the body volume .nii.gz file
        heart_path: path to the heart segmentation .nii.gz file
        lung_path: path to the lung segmentation .nii.gz file
    """
    # Load the volumes
    skin_img = nib.load(volume_path)
    heart_img = nib.load(heart_path)
    lung_img = nib.load(lung_path)
    
    # Get data and normalize
    skin_data = skin_img.get_fdata()
    skin_data = (skin_data - skin_data.min()) / (skin_data.max() - skin_data.min())
    
    heart_data = heart_img.get_fdata()
    lung_data = lung_img.get_fdata()
    
    # Create volumes
    skin_vol = Volume(skin_data, spacing=(1,1,3))
    heart_vol = Volume(heart_data, spacing=(1,1,3))
    lung_vol = Volume(lung_data, spacing=(1,1,3))
    
    # Create meshes
    skin_mesh = skin_vol.isosurface(0.1)
    heart_mesh = heart_vol.isosurface(0.5)
    lung_mesh = lung_vol.isosurface(0.5)
    
    # Apply styling
    skin_mesh.smooth(niter=20).color('wheat').alpha(0.3)
    heart_mesh.smooth(niter=20).color('red').alpha(0.8)
    lung_mesh.smooth(niter=20).color('pink').alpha(0.6)
    
    # Create plotter
    plt = Plotter(bg='black', size=(1000, 800), axes=1)
    txt = Text2D("MRI Visualization", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
    plt.add([skin_mesh, heart_mesh, lung_mesh, txt])
    
    # Set camera
    plt.camera.Elevation(-90)
    plt.camera.Azimuth(0)
    
    plt.show(interactive=True)

def visualize_skin_bone_heart_lung(volume_path, heart, lung):
    """
    Create a 3D visualization of the body outline, bones, heart, and lungs
    Args:
        volume_path: path to the body volume .nii.gz file
        heart: path to the heart segmentation .nii.gz file
        lung: path to the lung segmentation .nii.gz file
    """
    # Load the volumes
    skin_img = nib.load(volume_path)
    heart_img = nib.load(heart)
    lung_img = nib.load(lung)
    
    # Get data and normalize
    skin_data = skin_img.get_fdata()
    skin_data = (skin_data - skin_data.min()) / (skin_data.max() - skin_data.min())
    
    heart_data = heart_img.get_fdata()
    lung_data = lung_img.get_fdata()
    
    # Create volumes
    skin_vol = Volume(skin_data, spacing=(1,1,3))
    heart_vol = Volume(heart_data, spacing=(1,1,3))
    lung_vol = Volume(lung_data, spacing=(1,1,3))
    
    # Create meshes
    skin_mesh = skin_vol.isosurface(0.1)
    bone_mesh = skin_vol.isosurface(0.75)
    heart_mesh = heart_vol.isosurface(0.5)
    lung_mesh = lung_vol.isosurface(0.5)
    
    # Apply styling
    skin_mesh.smooth(niter=20).color('wheat').alpha(0.3)
    bone_mesh.smooth(niter=20).color('ivory').alpha(1)
    heart_mesh.smooth(niter=20).color('red').alpha(1)
    lung_mesh.smooth(niter=20).color('pink').alpha(1)
    
    # Create plotter
    plt = Plotter(bg='black', size=(1000, 800), axes=1)
    txt = Text2D("MRI Visualization", pos='top-middle', s=1.5, c='white', bg='black', alpha=0.7)
    plt.add([skin_mesh, bone_mesh, heart_mesh, lung_mesh, txt])
    
    # Set camera
    plt.camera.Elevation(-90)
    plt.camera.Azimuth(0)

    plt.show(interactive=True)  

def save_mesh_to_stl(mesh, name, decimation_factor):
    """
    Save a mesh to STL file with decimation
    Args:
        mesh: vedo mesh object
        name: output filename (without extension)
        decimation_factor: factor to reduce the number of triangles (0-1)
    """
    # Decimate the mesh to reduce polygon count
    decimated_mesh = mesh.decimate(decimation_factor)
    decimated_mesh.write(f'{name}.stl')

def export_stl(filename, volume_path, heart, lung, output_dir, decimation_factor=1,):
    """
    Create and export 3D meshes of the body outline, bones, heart, and lungs as STL files
    Args:
        volume_path: path to the body volume .nii.gz file
        heart: path to the heart segmentation .nii.gz file
        lung: path to the lung segmentation .nii.gz file
        output_dir: directory to save STL files
        decimation_factor: factor to reduce the number of triangles (0-1)
    """
    # Load the volumes
    skin_img = nib.load(volume_path)
    heart_img = nib.load(heart)
    lung_img = nib.load(lung)
    
    # Get data and normalize
    skin_data = skin_img.get_fdata()
    skin_data = (skin_data - skin_data.min()) / (skin_data.max() - skin_data.min())
    
    heart_data = heart_img.get_fdata()
    lung_data = lung_img.get_fdata()
    
    # Create volumes
    skin_vol = Volume(skin_data, spacing=(1,1,3))
    heart_vol = Volume(heart_data, spacing=(1,1,3))
    lung_vol = Volume(lung_data, spacing=(1,1,3))
    
    # Create meshes
    skin_mesh = skin_vol.isosurface(0.1)
    bone_mesh = skin_vol.isosurface(0.75)
    heart_mesh = heart_vol.isosurface(0.5)
    lung_mesh = lung_vol.isosurface(0.5)
    
    # Apply smoothing and decimation
    skin_mesh.smooth(niter=20)
    bone_mesh.smooth(niter=20)
    heart_mesh.smooth(niter=20)
    lung_mesh.smooth(niter=20)
    
    # Create output directory if it doesn't exist
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Save meshes as STL
    os.makedirs(f'{output_dir}/{filename}', exist_ok=True)
    combined_mesh = merge([skin_mesh, bone_mesh, heart_mesh, lung_mesh])
    combined_mesh_no_bone = merge([skin_mesh, heart_mesh, lung_mesh])
    save_mesh_to_stl(skin_mesh, f'{output_dir}/{filename}/{filename}_skin', decimation_factor)
    save_mesh_to_stl(bone_mesh, f'{output_dir}/{filename}/{filename}_bone', decimation_factor)
    save_mesh_to_stl(heart_mesh, f'{output_dir}/{filename}/{filename}_heart', decimation_factor)
    save_mesh_to_stl(lung_mesh, f'{output_dir}/{filename}/{filename}_lung', decimation_factor)
    save_mesh_to_stl(combined_mesh_no_bone, f'{output_dir}/{filename}/{filename}_combined_no_bone', decimation_factor)
    save_mesh_to_stl(combined_mesh, f'{output_dir}/{filename}/{filename}_combined', decimation_factor)
    
    print(f"STL files have been saved to {output_dir}/{filename}")

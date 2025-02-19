# MRI Visualization and Analysis Tools

A collection of Python tools for analyzing and visualizing MRI data, with a focus on heart and lung segmentation visualization.

## Features

- 3D visualization of MRI volumes
- Volume calculation for segmented structures
- Multi-structure visualization with customizable colors
- Export capabilities to STL format
- GIF creation for time-series visualization
- Support for both single volumes and time-series data

## Main Components

- `volume_analysis.py`: Calculate and compare volumes of segmented structures
- `visualize_volume.py`: Advanced 3D visualization of MRI data with multiple visualization modes
- `utils.py`: Utility functions for basic MRI visualization and data handling
- `creategif.py`: Tools for creating animated GIFs from MRI sequences
- `complex3d.py`: Complex 3D visualization with multiple structures

## Requirements

- nibabel
- numpy
- vedo
- matplotlib
- imageio

## Usage

1. Place your NIFTI files (.nii.gz) in the appropriate input directories
2. Use the visualization tools to explore the data:
   ```python
   python visualize_volume.py  # For 3D visualization
   python volume_analysis.py   # For volume calculations
   ```

3. For creating animations:
   ```python
   python creategif.py
   ```

## File Structure

```
MRI/
├── input/
│   └── volumes/          # Raw MRI volumes
├── output/
│   └── volume_*/         # Segmentation results
└── output_stl/           # Exported 3D models
```

## Data Format

- Input files should be in NIFTI format (.nii.gz)
- Segmentation files should follow the naming convention: `volume_XX_<Structure>.nii.gz`

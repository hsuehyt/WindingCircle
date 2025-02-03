# Winding Circle Generator

A Python script for generating customizable, organic, randomly winding closed circles in Autodesk Maya. Perfect for creating natural-looking paths, rollercoaster-like trails, or artistic curves.

## Features

- **Customizable Parameters**: 
  - Radius
  - Winding frequency
  - Irregularity (random distortion in radius)
  - Vertical irregularity (up-and-down distortion)
  - Random seed for reproducibility
- **User-Friendly Interface**: A simple Maya UI with sliders to adjust parameters dynamically.
- **Organic Design**: Generates natural-looking, winding closed curves with randomness.

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/hsuehyt/WindingCircle.git
   ```
2. Open Autodesk Maya.
3. Open the Script Editor (found in the bottom right corner).
4. Paste the script from `winding_circle.py` into the Python tab.

## Usage

1. Run the script in Maya's Script Editor.
2. A UI window will appear with adjustable sliders for:
   - **Radius**: The overall size of the circle (default: `100`, max: `9999`).
   - **Winding**: The number of loops or twists in the circle.
   - **Irregularity**: Random distortion in the radius for an organic look.
   - **Vertical Irregularity**: Up-and-down randomness along the Y-axis.
   - **Seed**: Ensures repeatable randomness.
3. Adjust the sliders and click **Create** to generate the winding circle.

## Parameters Explained

- **Radius**: Controls the size of the circle.
- **Winding**: The number of full loops around the circle.
- **Irregularity**: Adds randomness to the circle's radius for an organic shape.
- **Vertical Irregularity**: Adds randomness to the vertical movement for undulations.
- **Seed**: A random seed for predictable, repeatable results.

## Example

```python
create_winding_circle(radius=100, winding=7, irregularity=0.5, vertical_irregularity=0.4, seed=123)
```

This generates a winding circle with:
- Radius = `100`
- 7 twists around the circle
- Random distortions in radius and height for a natural look.

## Preview

![Preview of winding circle in Maya](path-to-preview-image.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
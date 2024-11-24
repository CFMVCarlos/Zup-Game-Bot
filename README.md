# Programming Click Mouse  

This project automates mouse clicks to complete a sequence of levels in the game **Zup!**, available on [Steam](https://store.steampowered.com/app/533300/Zup/). By leveraging Python, it simulates precise mouse interactions at specific screen coordinates, enabling seamless and efficient gameplay automation.  

---

## Features  
- **Automated Mouse Clicks**: Automate predefined sequences of clicks to progress through game levels.  
- **Real-Time Mouse Coordinates**: Retrieve and display the current position of the mouse cursor.  
- **Modular and Extensible**: Includes reusable utility functions for efficient automation and customization.  

---

## Project Structure  

- **`Levels.py`**:  
  Implements the `run_levels` function, which automates mouse clicks across multiple game levels.  

- **`getMouse.py`**:  
  Displays the current mouse position in real-time when a mouse click is detected.  

- **`ZUP.py`**:  
  The main script that initiates and manages gameplay automation for all predefined levels.  

- **`common.py`**:  
  A utility module containing shared functions for mouse control, including:  
  - `level_template_click`: Manages level-specific automation sequences.  
  - `mouse_click`: Simulates a single mouse click with optional coordinate conversion for different screen resolutions.  

---

## Setup and Usage  

### Prerequisites  
1. Install Python (version 3.7 or later is recommended).  
2. Install required dependencies using the following command:  
   ```bash  
   pip install -r requirements.txt  
   ```  

### Running the Scripts  

#### 1. Display Mouse Position  
Use `getMouse.py` to identify screen coordinates for automation. Each mouse click will print the current cursor position to the console, making it ideal for debugging and customization.  
   ```bash  
   python getMouse.py  
   ```  

#### 2. Automate Gameplay  
Run the main script `ZUP.py` to initiate the automation. This script performs the following tasks:  
- Resets the game state.  
- Executes level-specific click sequences.  
- Retries levels if necessary, based on timeout or unmet conditions.  
   ```bash  
   python ZUP.py  
   ```  

---

## Core Functions  

### `run_levels` (in `Levels.py`)  
Automates mouse clicks across multiple game levels, with customizable timing and positional parameters.  

### `display_mouse_position` (in `getMouse.py`)  
Displays the current mouse cursor position in the console when the mouse is clicked.  

### `level_template_click` (in `common.py`)  
Handles the automation logic for individual levels, including:  
- Resetting the game state.  
- Simulating multiple clicks with precise timing.  
- Implementing retries for unmet conditions or timeouts.  

### `mouse_click` (in `common.py`)  
Simulates a mouse click at a specified position, with built-in support for screen resolution scaling.  

---

## Additional Notes  

- **Customizable Click Sequences**: The click positions, delays, and conditions can be easily modified in `Levels.py` to suit different levels or UI layouts.  
- **Screen Resolution Adaptability**: The `convert_coords` function ensures compatibility with various screen resolutions by scaling coordinates dynamically.  

---

## Contributing  

Contributions are welcome! Here's how you can help:  
- **Fork this repository**: Create a branch for your changes.  
- **Submit a pull request**: Share your improvements for review.  

For significant changes, open an issue to discuss your ideas before implementation.  

---

## License  

This project is licensed under the [MIT License](LICENSE).  

---

## Author  

Developed by [Carlos Valente](https://github.com/CFMVCarlos).  

Feel free to reach out with any questions, suggestions, or collaboration opportunities!  
---

# Image Brightness Analysis in Google Colab

This guide explains how to measure the brightness of an image using Google Colab by counting how many pixels have a **lightness value greater than 0.663**. You can either upload the image manually or download it directly within the notebook.

---

## 🔹 Option 1: Upload an Image from Your Computer

1. First, download your target image locally:

   * Open the image in your browser.
   * Right-click and select **"Save Image As..."**
   * Save it in a known location (e.g., as `image.webp`).

2. Go to [Google Colab](https://colab.research.google.com/).

3. Create a new notebook.

4. Paste the following code into a cell:

```python
import numpy as np
from PIL import Image
from google.colab import files
import colorsys

# Upload the image file
uploaded_file = list(files.upload().keys())[0]
image = Image.open(uploaded_file)

# Normalize and compute lightness
rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness > 0.663)

print(f'Number of pixels with lightness > 0.663: {light_pixels}')
```

5. Run the cell (`Shift + Enter`), then upload your image when prompted.

6. The notebook will output the number of pixels exceeding the lightness threshold.

---

## 🔹 Option 2: Download and Analyze the Image in Colab

1. Open [Google Colab](https://colab.research.google.com/).

2. Create a new notebook.

3. In a cell, paste this command to download the image (replace the URL with your own if needed):

```python
!wget https://exam.sanand.workers.dev/lenna.webp -O image.webp
```

4. Run the cell to download the image.

5. In a new cell, paste and run the following code:

```python
import numpy as np
from PIL import Image
import colorsys

# Load and process the image
image = Image.open("image.webp")

rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness > 0.663)

print(f'Number of pixels with lightness > 0.663: {light_pixels}')
```

---

## ✅ Output

The notebook will display a message like:

```
Number of pixels with lightness > 0.663: 12345
```

---

## 💡 Notes

* The lightness value is based on the HLS (Hue, Lightness, Saturation) color model.
* Values are normalized to the range \[0, 1] using NumPy.
* You can change the threshold (`0.663`) to adjust brightness sensitivity.

---

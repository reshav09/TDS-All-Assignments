

---

## Approach

This section explains how to prepare and verify a target image for optimal compression, focusing on keeping the final output under **400 bytes** using WebP.

### Steps:

1. **Download the Target Image**

   * Obtain the original image from its source or repository.
   * Save it locally in a suitable format (e.g. PNG or JPEG).

2. **Analyze & Compress the Image**

   * Use the provided `image_analysis.py` script to:

     * Analyze the image properties (dimensions, size, color distribution, etc.)
     * Compress the image using the WebP format with **lossless** mode enabled
   * The script should produce output files such as:

     * `compressed_q2image_lossless.webp`
     * Other variants (e.g. lossy or lower-quality versions)

3. **Test the Lossless Version First**

   * Prioritize using the `compressed_q2image_lossless.webp` file.
   * If that does **not** meet the file size constraint (i.e. it's over 400 bytes), then:

     * Try alternative outputs from the compression script
     * Adjust compression settings (e.g. lower quality, resize)

4. **Verify File Size**

   * After selecting the image:

     * Use a command like `ls -lh` or `stat` to confirm file size

     ```bash
     stat -c%s compressed_q2image_lossless.webp
     ```

     * Ensure that the final image is **< 400 bytes**
   * Only use the image if this constraint is satisfied

---

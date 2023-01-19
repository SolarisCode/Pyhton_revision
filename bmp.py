"""A module for dealing with BMP bitmap image files."""

def _int32_to_bytes(x):
    """Convert integer to 4 bytes in little-endian format"""
    # & Bitwise-and.
    # >> Bitwise-right-shift.
    return bytes((x & 0xff,
                 x >> 8 & 0xff,
                 x >> 16 & 0xff,
                 x >> 24 & 0xff))

def write_grayscale(filename, pixels):
    """Creat and write a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.
        pixels: a rectangular image stored as a sequence of rows.
                Each row must be a itrable series of integers in
                the raange 0-255.

    Raises:
        ValueError: If any of the integer values out of the range.
                    Or the elements in each row aren't equal in count.
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])
    for row in pixels:
        if len(row) != width:
            raise ValueError("The rows have different length.")

    with open(filename, "wb") as bmp:
        #BMP header
        bmp.write(b"BM")

        size_bookmark = bmp.tell() # The next bytes hold the file size in 32-bit integer.
        bmp.write(b"\x00\x00\x00\x00") # Zero placeholder for now (little_endain).

        bmp.write(b"\x00\x00") # Unused 16-bit integer.
        bmp.write(b"\x00\x00") # Unused 16-bit integer.

        pixel_offset_bookmark = bmp.tell() # The next 4 bytes hold the offset to the
        bmp.write(b"\x00\x00\x00\x00")     # pixel data. Zero placeholder for now.

        #Image header.
        bmp.write(b"\x28\x00\x00\x00") # Image header size in bytes - 40 decimal.
        # We the implementation details func (_int32_to_bytes) to convert integer to
        # bytes in 32-bit littel-endain format.
        bmp.write(_int32_to_bytes(width))  # Image width in pixel.
        bmp.write(_int32_to_bytes(height)) # Image height in pixel.
        # The reset of the header is fixed in all 8-bit grayscal BMP images.
        bmp.write(b"\x01\x00") # Number of image planes.
        bmp.write(b"\x08\x00") # Bits per pixel 8-bit for grayscale.
        bmp.write(b"\x00\x00\x00\x00") # No compression.
        bmp.write(b"\x00\x00\x00\x00") # Zero for uncompressed images.
        bmp.write(b"\x00\x00\x00\x00") # Unused pixels per meter.
        bmp.write(b"\x00\x00\x00\x00") # Unused pixels per meter.
        bmp.write(b"\x00\x00\x00\x00") # Use while color table.
        bmp.write(b"\x00\x00\x00\x00") # All colors are important.

        # Color palette - a linear grayscale.
        for c in range(256):
            bmp.write(bytes((c, c, c, 0))) # Blue, Green, Red, Zero.

        # Pixel data.
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b"\x00" * ((4 - (len(row) % 4)) % 4) # Pad row to multiple of 4 bytes
            bmp.write(padding)

        # EOF file.
        eof_bookmark = bmp.tell()

        # Fill in the file size placeholder.
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in the pixel offset placeholder.
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))
        

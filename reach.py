def create_large_empty_file(filename, size_in_bytes):
    """
    Creates a large, empty file of a specified size.

    Args:
        filename (str): The name of the file to create.
        size_in_bytes (int): The desired size of the file in bytes.
    """
    try:
        with open(filename, 'wb') as f:
            f.truncate(size_in_bytes)
        print(f"Successfully created '{filename}' with size {size_in_bytes} bytes.")
    except IOError as e:
        print(f"Error creating file '{filename}': {e}")


# Example usage:
# Create a 100 MB file (100 * 1024 * 1024 bytes)
create_large_empty_file('large_empty_file.bin', 100 * 1024 * 1024)
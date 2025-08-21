def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{filename}'.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

    # Modify content - let's convert it to uppercase
    modified_content = content.upper()

    # Write the modified content to a new file
    output_filename = "output.txt"
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"✅ Modified content written to '{output_filename}'")
    except Exception as e:
        print(f"❌ Failed to write to '{output_filename}': {e}")

if __name__ == "__main__":
    main()

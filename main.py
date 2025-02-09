import base64
import os
import pyperclip
import sys

def get_mime_type(file_path):
	ext = os.path.splitext(file_path)[1].lower()
	if ext == '.png':
		return 'image/png'
	elif ext in ['.jpg', '.jpeg']:
		return 'image/jpeg'
	else:
		raise ValueError(f"Unsupported file extension: {ext}")

def image_to_base64(file_path):
	with open(file_path, 'rb') as image_file:
		encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
	return encoded_string

def main():
	if len(sys.argv) != 2:
		print("Usage: python main.py <image_file_path>")
		sys.exit(1)

	image_path = sys.argv[1]

	try:
		mime_type = get_mime_type(image_path)
		base64_string = image_to_base64(image_path)
		markdown_image = f"data:{mime_type};base64,{base64_string}"

		pyperclip.copy(markdown_image)
		print("The Base64 string has been copied to the clipboard.")

	except Exception as e:
		print(f"Error: {e}")

if __name__ == '__main__':
	main()

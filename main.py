import gradio as gr


description = """<center><img src='https://res.cloudinary.com/wonder4kids/image/upload/v1656014135/icon_ljflgz.png' height=200px width = 200px >
	<center><h2 align = 'center'>
	This Application is developed by <a href="https://github.com/HridayAg0102"> HRIDAY AGRAWAL </a>
	</h2>"""

def encrypt(data, key):
	shift = sum([ord(key[i])*(i+1) for i in range(len(key))]) % 26
	encrypted_result = ""
	for i in range(len(data)):
		encrypted_result += chr(ord(data[i]) - shift)

	return encrypted_result

def decrypt(encrypted_data, key):
	shift = sum([ord(key[i])*(i+1) for i in range(len(key))]) % 26
	decrypted_result = ''
	for i in range(len(encrypted_data)):
		decrypted_result += chr(ord(encrypted_data[i]) + shift)
	return decrypted_result


demo1 = gr.Interface(fn = encrypt, inputs = ['text', 'text'], outputs=gr.Textbox(label="Encrypted Text", lines=4),
	title = 'Encrypt Data',
	description = description)
demo2 = gr.Interface(fn = decrypt, inputs = ['text', 'text'], outputs=gr.Textbox(label="Decrypted Text", lines=4),
	 title = 'Decrypt Data',
	description = description)

print('This is a simple Cryptographic Web Application for me to learn how to create webapps in python :)')

final_interface = gr.TabbedInterface([demo1, demo2], tab_names=['Encrypt data', 'Decrypt data']).launch(
	favicon_path = './icon.png', share = True)

import codecs
import os

codecs.register_error('none', lambda e: ('?', e.end))


def utf8_to_sjis(files, in_dir, out_dir):
	os.makedirs(out_dir, exist_ok=True)
	
	for f in files:
		utf8_to_sjis_one(f, in_dir, out_dir)


def utf8_to_sjis_one(file, in_dir, out_dir):
	
	with open(f'{in_dir}/{file}', mode='r', encoding='utf-8') as fi:
		with open(f'{out_dir}/{file}', mode='w', encoding='sjis', errors='none') as fo:
			fo.write(fi.read())


if __name__=='__main__':
	files = [
		'test_file.csv'
	]
	in_dir = 'in_utf8'
	out_dir = 'sjis'
	utf8_to_sjis(files, in_dir, out_dir)



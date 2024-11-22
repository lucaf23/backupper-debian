from setuptools import setup, find_packages

setup(
	name="backupper",
	version="1.0.2",
	description="Un semplice Python script per gestire i backups",
	author="Luca Ferrari",
	author_email="luca10.ferrari@edu.unife.it",
	url="https://github.com/lucaf23/backupper",
	packages=find_packages(),
	py_modules=["backupper"],
	entry_points={
		"console_scripts": [
			"backupper=backupper:main",
		],
	},
	install_requires=[ "pyzipper" ],
	classifiers=[
		"Programmin Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)

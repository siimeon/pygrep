pygrep
======

Python grep tool

Python tool for searching character sequence

Basic usage: python pygrep.py fileSource separator
Advanced usage: python pygrep.py fileSource separator options

Advanced options:

	-f Return full lines
	-c[number] Return character count after separator
	-h[number] Choose witch match will be returned. If 0 last is returned
	-a Return all lines
		(Defaultly first line with separator is returned)

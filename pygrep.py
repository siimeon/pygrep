'''
pygrep.py - Python grep tool
----------------------------
Basic: python pygrep.py [fileSource] [separator]
Advanced: python pygrep.py [fileSource] [separator] [options]
Advanced options:
	-f 	full lines
	-a  all lines from file
	-c 	characters after separator 
'''
import sys
version = 0.11

def pygrep(fileSource, separator):
	fileAccess = open(fileSource, 'r')
	lines = fileAccess.read().split('\n')
	fileAccess.close()
	for i in lines:
		if separator in i:
			return i.split(separator).pop()
	return ''

def advanced_pygrep(fileSource, separator, allFile, fullLines, charsCount, hit):
	fileAccess = open(fileSource, 'r')
	lines = fileAccess.read().split('\n')
	fileAccess.close()
	retValue = []
	for i in lines:
		if separator in i:
			value = ''
			if fullLines == True:
				value = i
			else:
				value = i.split(separator).pop()
				if charsCount != 0:
					value = value.strip()[:charsCount]
			retValue.append(value)
			if allFile == False:
				return retValue.pop()
	strvalue = ''
	if hit == -1:
		for j in range(len(retValue)):
			if j != 0:
				strvalue += '\n'
			strvalue += retValue[j]
	else:
		try:
			if hit == 0:
				return retValue.pop()
			else:
				return retValue[hit-1]
		except:
			print 'Error'
			sys.exit()
	return strvalue


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'pygrep - Python grep tool'
		print '-------------------------------------------------------------------'
		print 'Python tool for searching character sequence'
		print ''
		print 'Basic usage: python pygrep.py [fileSource] [separator]'
		print 'Advanced usage: python pygrep.py [fileSource] [separator] [options]'
		print '-------------------------------------------------------------------'
		print 'Advanced options:'
		print '-f Return full lines'
		print '-c[number] Return character count after separator'
		print '-h[number] Choose witch match will be returned. If 0 last is returned'
		print '-a Return all lines'
		print '   (Defaultly first line with separator is returned)'
	if len(sys.argv) == 2 and sys.argv[1] in ['-v', 'version', '-version']:
		print 'pygrep.py '+str(version)
	if len(sys.argv) == 3:
		print pygrep(sys.argv[1], sys.argv[2])
	if len(sys.argv) > 3 and len(sys.argv) < 7:
		fileSource = sys.argv[1]
		separator = sys.argv[2]
		charsCount = 0
		hit = -1
		allFile = False
		fullLines = False
		for i in range(len(sys.argv)-3):
			if sys.argv[i+3] == '-f':
				fullLines = True
			if sys.argv[i+3] == '-a':
				allFile = True
			if sys.argv[i+3].startswith('-c'):
				tmp = sys.argv[i+3]
				charsCount = int(tmp.split('-c').pop())
			if sys.argv[i+3].startswith('-h'):
				tmp = sys.argv[i+3]
				hit = int(tmp.split('-h').pop())
				allFile = True
		print advanced_pygrep(fileSource, separator, allFile, fullLines, charsCount, hit)

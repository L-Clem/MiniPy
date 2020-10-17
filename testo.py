import ui
import matplotlib.pyplot as plt

#v = ui.load_view()
#v.present('sheet')


def button_tapped(sender):
	'@type sender: ui.Button'
	# Get the button's title for the following logic:
	t = sender.title
	global shows_result
	# Get the labels:
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if t in '0123456789':
		if shows_result or label.text == '0':
			# Replace 0 or last result with number:
			label.text = t
		else:
			# Append number:
			label.text += t
	elif t == '.' and label.text[-1] != '.':
		# Append decimal point (if not already there)
		label.text += t
	elif t in '+-÷×':
		if label.text[-1] in '+-÷×':
			# Replace current operator
			label.text = label.text[:-1] + t
		else:
			# Append operator
			label.text += t
	elif t == 'AC':
		# Clear All
		label.text = '0'
	elif t == 'C':
		# Delete the last character:
		label.text = label.text[:-1]
		if len(label.text) == 0:
			label.text = '0'
	elif t == '=':
		# Evaluate the result:
		try:
			label2.text = label.text + ' ='
			expr = label.text.replace('÷', '/').replace('×', '*')
			label.text = str(eval(expr))
		except (SyntaxError, ZeroDivisionError):
			label.text = 'ERROR'
		shows_result = True
	if t != '=':
		shows_result = False
		label2.text = ''


j = int(input('Capital de départ  '))
g = int(input('Pourcentage de départ  '))
p = int(input('Pourcentage en moins  '))
k = 1
euros = []

while g > 0:
	i = ((j*g)/100)
	h = j+i
	x = int(h)
	print(g ,':', k,':', x)
	euros.append(x)
	j =+ h
	g -= p
	k += 1
#print(euros)
plt.plot(euros)
plt.ylabel('Argent en €')
plt.xlabel('Temporalité')
plt.show()
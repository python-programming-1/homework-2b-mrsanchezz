import sys
import random


ans = ['r', 'p', 's', 'sc', 'y', 'n']
ansD = {'r':'rock', 'p':'paper','s':'scissors'}
win = ['pr','sp','rs']
lose = ['rp','ps','sr']
draw = ['rr','pp','ss']

winCnt = 0
loseCnt = 0
drawCnt = 0

rounds = []

while True:
	print('Make a move! (r/s/p) or enter sc for score')
	player = input()

	if player not in ans[0:4]:
		print('Invalid move, must be r, s, or p! Or sc for score')
		continue
	elif player == 'sc':
		print('Score: human {}, computer {}'.format(winCnt,loseCnt))
		continue

	rounds.append(player)
	if len(rounds) >= 3:
		if rounds[-1] == rounds[-2] and rounds[-2] == rounds[-3]:
			if rounds[-1] == 'r':
				computer = 'p'
			elif rounds[-1] == 'p':
				computer = 's'
			else:
				computer = 'r'
	else:
		computer = random.choice(ans[0:3])

	print('You chose {} and the computer chose {}.'.format(ansD[player],ansD[computer]))

	outcome = player+computer

	if outcome in win:
		print('You win!')
		winCnt = winCnt + 1
	elif outcome in lose:
		print('You lose!')
		loseCnt = loseCnt + 1
	else:
		print('Draw!')
		drawCnt = drawCnt + 1

	print('Score: human {}, computer {}'.format(winCnt,loseCnt))

	valid_ans = False
	while not valid_ans:
		print('Do you want to play again? (y/n)')
		play = input()

		if play not in ans[-3:]:
			print('Invalid input, must be y or n! Or sc for score')
			continue
		elif play == 'sc':
			print('Score: human {}, computer {}'.format(winCnt,loseCnt))
			continue

		valid_ans = True

		if play == 'y':
			continue
		elif play == 'n':
			print('Thanks bye!')
			sys.exit()
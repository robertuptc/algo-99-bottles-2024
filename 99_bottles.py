def bottle_song(num):
	for b_num in reversed(range(num)):
		if b_num > 0:
			print(f"{b_num + 1} bottles of beer on the wall, {b_num + 1} bottles of beer.")
			if b_num > 1:
				print(f"Take one down and pass it around, {b_num} bottles of beer on the wall.")
			else: 
				print(f"Take one down and pass it around, {b_num} bottle of beer on the wall.")
		else:
			print(f"{b_num + 1} bottle of beer on the wall, {b_num + 1} bottle of beer.")
			print(f"Take one down and pass it around, no more bottles of beer on the wall.")
			print("No more bottles of beer on the wall, no more bottles of beer.\n\
Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song(5)

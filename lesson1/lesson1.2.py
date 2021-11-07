seconds=int(input("Time amount"))
if seconds < 60:
    print(f"00:00:{seconds:02}")
elif seconds < 3600:
    print(f"00:{seconds // 60:2}:{seconds % 60:02}")
else :
    print(f"{seconds // 3600:02}:{seconds % 3600 // 60:02}:{seconds % 60:02}")

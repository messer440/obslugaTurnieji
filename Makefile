.PHONY: main clean

main:
	src/scripts/recompUI.sh
clean:
	rm src/db/players/*
	rm src/db/tournaments*

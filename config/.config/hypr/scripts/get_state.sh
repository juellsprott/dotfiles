LOCK="/tmp/exit.lock"
if [ -f "$LOCK" ]; then
	rm $LOCK
	exit 0
else
	touch $LOCK
	exit 1
fi
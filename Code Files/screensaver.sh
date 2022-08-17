#!/bin/bash
process() {
while read input; do
	case "$input" in
		UNBLANK*) killall omxplayer.bin ;;
		BLANK*) omxplayer --loop --no-osd --no-keys --aspect-mode stretch "/home/pi/BMO/BMO_Idle_loop_ColorAdjust.mp4" & ;;
	esac
done
}

/usr/bin/xscreensaver-command -watch | process

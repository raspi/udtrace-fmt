# udtrace-fmt

Formatter for [udtrace](https://github.com/laf0rge/udtrace) (https://git.gnumonks.org/udtrace)

First capture Unix domain socket traffic with `udtrace`, for example list all X11 windows:

    LD_PRELOAD=./libudtrace.so xwininfo -tree -root 2> trace.txt

Then we can format it to more readable hex dump:

    % python main.py trace.txt

For example X11 Unix domain socket handshake:

```
---- Packet #1: fd:3 type:writev W  len: 12 (0x0c)
6c 00 0b 00 00 00 12 00   10 00 00 00              | lØ.ØØØ.Ø  .ØØØ

---- Packet #2: fd:3 type:writev W  len: 18 (0x12)
4d 49 54 2d 4d 41 47 49   43 2d 43 4f 4f 4b 49 45  | MIT-MAGI  C-COOKIE
2d 31                                              | -1

---- Packet #3: fd:3 type:writev W  len: 2 (0x02)
00 00                                              | ØØ

---- Packet #4: fd:3 type:writev W  len: 16 (0x10)
7b 4c 57 8b e9 1d ca 6e   32 c3 74 03 07 17 1e a1  | {LW.é.Ên  2Ãt....¡

---- Packet #5: fd:3 type:recv R  len: 8 (0x08)
01 00 0b 00 00 00 4b 03                            | .Ø.ØØØK.

---- Packet #6: fd:3 type:recv R  len: 2047 (0x7ff)
8c a5 b8 00 00 00 40 09   ff ff 1f 00 00 01 00 00  | .¥¸ØØØ@⇥  ÿÿ.ØØ.ØØ
14 00 ff ff 01 07 00 00   20 20 08 ff 00 00 00 00  | .Øÿÿ..ØØ    .ÿØØØØ
54 68 65 20 58 2e 4f 72   67 20 46 6f 75 6e 64 61  | The X.Or  g Founda
74 69 6f 6e 01 01 20 00   00 00 00 00 04 08 20 00  | tion.. Ø  ØØØØ.. Ø

--- snipped ---
```

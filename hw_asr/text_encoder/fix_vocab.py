fin = open("hw_asr/text_encoder/librispeech-vocab.txt", "r")
fout = open("hw_asr/text_encoder/librispeech-fixed-vocab.txt", "w+")

while line := fin.readline():
    line = line.lower().replace("'", "")
    print(line, end="", file=fout)

fin.close()
fout.close()

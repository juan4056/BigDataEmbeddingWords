with open('/home/jaoks/Downloads/clean/clean.txt') as file:
    line = "asdasdasd"
    while line:
        line = file.readline()
        if len(line) > 1:
            parser = line[line.index(',')+1:]
            tag = line[:line.index(',')]
            if len(parser) >= 8:
                with open('purified.txt', 'a') as the_file:
                    the_file.write(tag+','+parser)
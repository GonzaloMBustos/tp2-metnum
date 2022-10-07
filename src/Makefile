CC = g++
CFLAGS =  -pedantic -O3 -lm -Wall -Wextra
.PHONY: all
all: tp2

valgrind: 
	valgrind --leak-check=full  --undef-value-errors=yes ./tp2

all: tp2

tp2: main_cpp.o eigen_cpp.o utils_cpp.o
	$(CC) $(CFLAGS) $^ -o $@ $(LDLIBS)

main_cpp.o: main.cpp eigen.h types.h
	$(CC) $(CFLAGS) -c $< -o $@

eigen_cpp.o: eigen.cpp eigen.h types.h
	$(CC) $(CFLAGS) -c $< -o $@

utils_cpp.o: utils.cpp utils.h types.h
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean

clean:
	rm -f *.o
	rm -f tp1
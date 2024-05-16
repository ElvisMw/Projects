CC = gcc
CFLAGS = -Wall -Wextra -std=c99

# Object files
OBJ = main.o dbms.o

# Executable
TARGET = dbms

# Source files
SRCS = main.c dbms.c

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(TARGET) $(OBJ)

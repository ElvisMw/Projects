CC = gcc
CFLAGS = -Wall -Wextra -std=c99
LIBS =
OBJS = cook_app.o recipes.o

all: cook_app

cook_app: $(OBJS)
	$(CC) -o cook_app $(OBJS) $(LIBS)

cook_app.o: cook_app.c recipes.h
	$(CC) -c cook_app.c $(CFLAGS)

recipes.o: recipes.c recipes.h
	$(CC) -c recipes.c $(CFLAGS)

clean:
	rm -f cook_app $(OBJS)

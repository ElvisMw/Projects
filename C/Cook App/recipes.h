#ifndef RECIPES_H
#define RECIPES_H

typedef struct {
    const char *name;
    const char *ingredients;
    const char *instructions;
} Recipe;

void populate_recipes(Recipe recipes[]);

#endif /* RECIPES_H */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "recipes.h"

#define NUM_RECIPES 20

/**
 * @brief Display a single recipe.
 *
 * @param recipe Pointer to the recipe to display.
 */
void display_recipe(const Recipe *recipe) {
    printf("\nRecipe: %s\n", recipe->name);
    printf("Ingredients: %s\n", recipe->ingredients);
    printf("Instructions: %s\n", recipe->instructions);
}

/**
 * @brief Recommend recipes based on the current time and meal type.
 *
 * @param recipes Array of recipes.
 * @param num_recipes Number of recipes in the array.
 * @param meal_time Meal type ("breakfast", "lunch", or "supper").
 */
void recommend_meal(Recipe recipes[], int num_recipes, const char *meal_time) {
    time_t current_time; // Variable to hold current time
    struct tm *local_time_info; // Structure to hold local time information
    int current_hour;

    // Get current time
    time(&current_time);
    local_time_info = localtime(&current_time);
    current_hour = local_time_info->tm_hour;

    // Recommend recipes based on meal time
    if ((current_hour >= 6 && current_hour < 11) && (strcmp(meal_time, "breakfast") == 0)) {
        printf("Recommended %s recipes:\n", meal_time);
        for (int i = 0; i < num_recipes; i++) {
            if (strstr(recipes[i].name, "Breakfast") != NULL) {
                printf("%d. %s\n", i + 1, recipes[i].name);
            }
        }
    } else if ((current_hour >= 11 && current_hour < 15) && (strcmp(meal_time, "lunch") == 0)) {
        printf("Recommended %s recipes:\n", meal_time);
        for (int i = 0; i < num_recipes; i++) {
            if (strstr(recipes[i].name, "Lunch") != NULL) {
                printf("%d. %s\n", i + 1, recipes[i].name);
            }
        }
    } else if ((current_hour >= 15 && current_hour < 21) && (strcmp(meal_time, "supper") == 0)) {
        printf("Recommended %s recipes:\n", meal_time);
        for (int i = 0; i < num_recipes; i++) {
            if (strstr(recipes[i].name, "Supper") != NULL) {
                printf("%d. %s\n", i + 1, recipes[i].name);
            }
        }
    } else {
        printf("It's not %s time yet!\n", meal_time);
    }
}

/**
 * @brief Main function to run the cooking app.
 *
 * @return 0 on successful execution.
 */
int main() {
    Recipe recipes[NUM_RECIPES];
    populate_recipes(recipes);

    printf("Welcome to the Cooking App!\n");

    time_t current_time;
    time(&current_time);
    printf("Current Time: %s", asctime(localtime(&current_time))); // Print current time

    recommend_meal(recipes, NUM_RECIPES, "breakfast");
    recommend_meal(recipes, NUM_RECIPES, "lunch");
    recommend_meal(recipes, NUM_RECIPES, "supper");

    return 0;
}

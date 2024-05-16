#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dbms.h"

/**
 * The main function acts as a simple command line interface for the database.
 * It demonstrates the basic CRUD operations.
 */
int main() {
    int id, age;
    char name[MAX_NAME_LENGTH];

    // Prompt user for record information
    printf("Enter ID: ");
    scanf("%d", &id);
    printf("Enter Name: ");
    scanf("%s", name); // Modified to accept string input
    printf("Enter Age: ");
    scanf("%d", &age);

    // Create record
    struct Record newRecord = {id, "", age}; // Initialize name field to empty string
    strcpy(newRecord.name, name); // Copy the input name into the structure
    addRecordToFile(newRecord);

    // Retrieve record
    struct Record retrievedRecord = getRecordById(id);
    if (retrievedRecord.id != -1) {
        printf("Record found: ID=%d, Name=%s, Age=%d\n", retrievedRecord.id, retrievedRecord.name, retrievedRecord.age);
        // Print in the specified format
        printf("ID=%d, Name=%s, Age=%d\n", retrievedRecord.id, retrievedRecord.name, retrievedRecord.age);
    } else {
        printf("Record not found.\n");
    }

    return 0;
}

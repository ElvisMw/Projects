/**
 * @file dbms.c
 * @brief Implementation of functions for interacting with the database file
 *
 * This file contains the implementation of functions for adding, retrieving,
 * updating, and deleting records from the database file. It also contains the
 * definitions of the structures used to represent records.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dbms.h"

/**
 * @brief Adds a new record to the database file
 *
 * This function adds a new record to the database file. It takes a Record
 * structure as a parameter and appends it to the end of the file.
 *
 * @param record The Record structure to add to the database
 */
void addRecordToFile(struct Record record) {
    FILE *file = fopen("database.txt", "a");
    if (file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }
    fprintf(file, "%d,%s,%d\n", record.id, record.name, record.age);
    fclose(file);
}

/**
 * @brief Retrieves a record from the database file by ID
 *
 * This function retrieves a record from the database file by its ID. If the
 * record is not found, it returns a default Record structure with the ID set
 * to -1.
 *
 * @param id The ID of the record to retrieve
 * @return The Record structure representing the record with the given ID
 */
struct Record getRecordById(int id) {
    struct Record record;
    FILE *file = fopen("database.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }
    while (fscanf(file, "%d,%[^,],%d\n", &record.id, record.name, &record.age) != EOF) {
        if (record.id == id) {
            fclose(file);
            return record;
        }
    }
    fclose(file);
    // Return a default record if not found
    record.id = -1;
    return record;
}

/**
 * @brief Updates an existing record in the database file
 *
 * This function updates an existing record in the database file. It takes a
 * Record structure as a parameter and updates the record with the same ID in the
 * file. If the record is not found, it prints an error message.
 *
 * @param newRecord The updated Record structure
 */
void updateRecord(struct Record newRecord) {
    FILE *file = fopen("database.txt", "r+");
    if (file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }
    struct Record record;
    long pos;
    while (fscanf(file, "%d,%[^,],%d\n", &record.id, record.name, &record.age) != EOF) {
        if (record.id == newRecord.id) {
            pos = ftell(file) - strlen(record.name) - sizeof(int);
            fseek(file, pos, SEEK_SET);
            fprintf(file, "%d,%s,%d\n", newRecord.id, newRecord.name, newRecord.age);
            fclose(file);
            return;
        }
    }
    fclose(file);
    printf("Record not found.\n");
}

/**
 * @brief Deletes a record from the database file
 *
 * This function deletes a record from the database file. It takes the ID of the
 * record to delete as a parameter and removes the record from the file. If the
 * record is not found, it prints an error message.
 *
 * @param id The ID of the record to delete
 */
void deleteRecord(int id) {
    FILE *temp = fopen("temp.txt", "w");
    if (temp == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }
    FILE *file = fopen("database.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }
    struct Record record;
    while (fscanf(file, "%d,%[^,],%d\n", &record.id, record.name, &record.age) != EOF) {
        if (record.id != id) {
            fprintf(temp, "%d,%s,%d\n", record.id, record.name, record.age);
        }
    }
    fclose(file);
    fclose(temp);
    remove("database.txt");
    rename("temp.txt", "database.txt");
}

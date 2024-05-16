#ifndef DBMS_H
#define DBMS_H

/**
 * @file dbms.h
 * @brief Header file for the database module
 *
 * This file contains the definitions of the functions and structures used in the
 * database module. It also defines the maximum length of a record name.
 */

#define MAX_NAME_LENGTH 50 /**< Maximum length of a record name */

/**
 * @struct Record
 * @brief Structure to represent a record in the database
 *
 * This structure contains the ID, name, and age of a record.
 */
struct Record {
    int id;                 /**< Unique identifier for the record */
    char name[MAX_NAME_LENGTH]; /**< Name of the record */
    int age;                /**< Age of the record */
};

/**
 * @brief Adds a new record to the database file
 *
 * This function adds a new record to the database file. It takes a Record
 * structure as a parameter and appends it to the end of the file.
 *
 * @param record The Record structure to add to the database
 */
void addRecordToFile(struct Record record);

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
struct Record getRecordById(int id);

/**
 * @brief Updates an existing record in the database file
 *
 * This function updates an existing record in the database file. It takes a
 * Record structure as a parameter and updates the record with the same ID in the
 * file. If the record is not found, it prints an error message.
 *
 * @param newRecord The updated Record structure
 */
void updateRecord(struct Record newRecord);

/**
 * @brief Deletes a record from the database file
 *
 * This function deletes a record from the database file. It takes the ID of the
 * record to delete as a parameter and removes the record from the file. If the
 * record is not found, it prints an error message.
 *
 * @param id The ID of the record to delete
 */
void deleteRecord(int id);

#endif /* DBMS_H */

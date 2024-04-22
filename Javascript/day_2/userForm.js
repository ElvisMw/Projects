#!/usr/bin/node

const readline = require('readline');

/**
 * Calculates the age based on the date of birth.
 *
 * @param {string} dateOfBirth The date of birth in the format of 'YYYY-MM-DD'.
 * @returns {number} The age of the person based on the current year.
 */
const calculateAge = (dateOfBirth) => {
    const today = new Date();
    const birthDate = new Date(dateOfBirth);
    let age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}

/**
 * Determines the job qualification based on the age of the person.
 *
 * @param {number} age The age of the person.
 * @returns {string} The job qualification of the person, either 'qualified' or 'not qualified'.
 */
const determineJobQualification = (age) => {
    return age >= 25 ? "qualified" : "not qualified";
}

/**
 * Formats the gender and marital status of the person.
 *
 * @param {string} gender The gender of the person, either 'male' or 'female'.
 * @param {string} maritalStatus The marital status of the person, either 'single', 'married', or 'divorced'.
 * @returns {string} The formatted gender and marital status of the person.
 */
const formatGenderAndMaritalStatus = (gender, maritalStatus) => {
    const title = (gender === "male") ? "Mr." : (maritalStatus === "married") ? "Mrs." : "Miss";
    return title;
}

// Main function to gather user input and display result
const jobQualificationScript = () => {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Enter your name: ", (name) => {
        rl.question("Enter your date of birth (YYYY-MM-DD): ", (dateOfBirth) => {
            rl.question("Enter your gender (male/female): ", (gender) => {
                rl.question("Enter your marital status (single/married/divorced): ", (maritalStatus) => {
                    rl.close();

                    const age = calculateAge(dateOfBirth);
                    const qualification = determineJobQualification(age);
                    const title = formatGenderAndMaritalStatus(gender, maritalStatus);

                    const message = `Hello ${title} ${name}, you are ${age} years old and you are ${qualification} for the job position.`;
                    console.log(message);
                });
            });
        });
    });
}

// Call the main function to start the script
jobQualificationScript();
